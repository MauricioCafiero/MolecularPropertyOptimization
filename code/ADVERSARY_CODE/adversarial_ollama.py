from langchain_openai.chat_models import ChatOpenAI
from langchain_anthropic.chat_models import ChatAnthropic
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
#from google.colab import userdata
from langchain_core.tools import tool
from langgraph.graph import START, StateGraph
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode, tools_condition
import gradio as gr
import os
from PIL import Image
from collections import Counter
from typing import Annotated, TypedDict
import time, sys
from anthropic import Anthropic
from openai import OpenAI
from ollama import Client as ollama_client

sys.path.append('code')
from MolPropOp import *
#from lipinski_module import *
from docking_module import *

tools = [grow_cycle, replace_groups, make_random_list, related, lipinski]

#anthropic_key = os.getenv("ANTHROPIC_KEY")
#client = Anthropic(api_key=anthropic_key)

openai_key = os.getenv("OPENAI_API_TOKEN")
client = OpenAI(api_key=openai_key)

from google.colab import userdata
ollama_key = userdata.get('ollama_key')
models = ['deepseek-v3.1:671b', 'gpt-oss:120b', 'gpt-oss:20b',
          'devstral-2:123b', 'cogito-2.1:671b',
          'nemotron-3-nano:30b', 'gemini-3-flash-preview',
          'kimi-k2:1t', 'kimi-k2.5']

model = models[-1]

# google_key = os.getenv('GEMINI_API')
# model =  ChatGoogleGenerativeAI(
#     model='gemini-3-flash-preview', api_key=google_key).bind_tools(tools)

def adversary(prompt: str):
    adversary_message = client.messages.create(
    model="claude-haiku-4-5-20251001",
    max_tokens=2000,
    system = '''
    You are a drug design assistant. You will recieve a proposal from  another model
    of novel molecules it has designed to bind to a particular protein target. The proposal will 
    include reasoning as to why the model thinks those molecules will bind well, and estimated 
    docking scores for each molecule. Your task is to analyze the proposal and find any flaws 
    in the reasoning or estimation of the docking scores. You should then suggest modifications 
    to the proposed molecules that would make them more likely to bind well, and provide reasoning 
    for why those modifications would help.

    The other model has access to the following tools, and you may suggest that it use these tools to 
    gather more information or test out modifications to the proposed molecules:

    - grow_cycle: starts with a molecule SMILES and adds substituents to it, docks them, and returns 
                  a list of molecules and scores. 

    - replace_groups: starts with a molecule SMILES and replaces specific groups in it with new groups, 
                      returning a list of new molecules and scores. 
    
    - make_random_list: this tool generates a list of substituents of specified length (num_items). 
    
    - related: this tool generates a list of molecules that are structurally related to a given molecule, 
                and may be useful for exploring the chemical space around promising molecules.

    - lipinski: this tool evaluates a list of molecules for their drug-likeness based on Lipinski's rule of five.
    ''',
    messages=[
        {"role": "user", "content": prompt},])

    response = adversary_message.content[0].text

    return response

sys_message = f'''
{task_specific_prompt}

## You will first:
- Read the list of molecule SMILES and scores
- Ascertain any features of the molecules that contribute to the desired score. For example, if,
from one molecule to the next, the addition of an O group makes the score better.
- Gather all of these trends across all of the molecules.

## If you need additional information to ascertain the trends, such as more modified
molecules and their docking scores, you have tools you can call to generate new
molecules and get their docking scores. You can use these tools as many times as you want
to gather information on the trends. *NOTE: if you choose to add a phenyl group to a molecule,
use the SMILES 'c7ccccc7', so that it does not interfere with other rings in the molecule that
may already use numbers 1-6 in their SMILES notation. 

The tools you have available include:
                            
- grow_cycle: starts with a molecule SMILES and adds substituents to it, docks them, and returns 
              a list of molecules and scores. You can use this tool to further explore modifications
              to promising molecules that you find in the input data. You can provide a list of
              substituents to add, or use the predefined sets: e_withdraw (electron withdrawing),
              e_donate (electron donating), withdraw_with_linkers (electron withdrawing with linkers), 
              donate_with_linkers (electron donating with linkers). You can also generate a random list 
              of substituents with the make_random_list tool and use that as input to grow_cycle.

- replace_groups: starts with a molecule SMILES and replaces specific groups in it with new groups, returning a list of new
                  molecules and scores. This tool allows you to test specific hypotheses about how replacing certain
                  groups in a molecule might affect binding affinity. You can specify which groups to replace and
                  what to replace them with, or use the predefined sets of substituents mentioned above. You can also 
                  generate a random list of substituents with the make_random_list tool and use that as input to replace_groups.

- make_random_list: this tool generates a list of substituents of specified length (num_items). It draws from the predefined lists:
                    e_withdraw (electron withdrawing), e_donate (electron donating), withdraw_with_linkers 
                    (electron withdrawing with linkers), donate_with_linkers (electron donating with linkers). 
                    Use this tool when you want to get a broad sense of how different modifications affect binding affinity, 
                    without having a specific hypothesis in mind.

- related: this tool generates a list of molecules that are structurally related to a given molecule, and
           may be useful for exploring the chemical space around promising molecules you find in the input 
           data. It returns a list of related molecules and a few properties.

- lipinski: this tool evaluates a list of molecules for their drug-likeness based on Lipinski's rule of five, 
            which is a set of guidelines for determining whether a molecule is likely to be an orally active 
            drug in humans. This tool can help you ensure that the molecules you are proposing not only have 
            good docking scores but also have properties that make them more likely to be successful as drugs.
            QED (quantitative estimate of drug-likeness) is a score between 0 and 1 that summarizes how 
            drug-like a molecule is, with 1 being the most drug-like. A higher QED score indicates that a 
            molecule has properties that are more consistent with known drugs, such as appropriate molecular 
            weight, lipophilicity, and number of hydrogen bond donors and acceptors.

## Once you have ascertained the trends:
- Use the trends you learned to suggest 1-5 new molecules that obey the trends you found
and which should have a better score than the molecules in the list.
- Provide reasoning as to why you created those new molecules.
- Estimate the new scores.

## You may ask the user for clarification if needed, but try to use the tools to gather as much information as you
can before asking for clarification.

## In further turns, you will also receive feedback from an adversary model that is trying to find flaws 
in your reasoning and suggest improvements to your proposed molecules. You should use this feedback to 
refine your understanding of the trends, run new experiments with the tools to gather more information, 
and improve your proposed molecules in subsequent turns.

## If you have identified good potential hits, evaluate the Lipinski properties of the proposed molecules 
and use that information to further refine your proposals, keeping in mind that you want to propose molecules 
that not only have good docking scores but also have good drug-like properties. 

## Once you have reached a point where you think you have proposed the best possible molecules based on 
the trends, tool results and the adversary feedback, reply with only one word: "Done". This will signal that you have 
finished the task and will not propose any more molecules.
'''

global messages
messages = [{'role': 'system', 'content': sys_message}]

#@spaces.GPU
def start_chat():
  '''
  '''
  global chat_history, messages, reasoning
  chat_history = []
  reasoning = []
  messages = [{'role': 'system', 'content': sys_message}]

#@spaces.GPU
def chat_turn(prompt: str):
  '''
  '''
  global chat_history, messages, reasoning
  
  client = ollama_client(host = 'https://ollama.com',
            headers={'Authorization': f'Bearer {ollama_key}'})

  available_functions = {
    'grow_cycle': grow_cycle,
    'replace_groups': replace_groups,
    'make_random_list': make_random_list,
    'related': related,
    'lipinski': lipinski
  }

  messages.append({'role': 'user', 'content': prompt})

  while True:
      response = client.chat(
          model=model,
          messages=messages,
          tools=[grow_cycle, replace_groups, make_random_list, related, lipinski],
          think=True,
      )
      messages.append(response.message)
      print('------------------------------------------------------------------------')
      print("Thinking: ", response.message.thinking)
      print('------------------------------------------------------------------------')
      print("Content: ", response.message.content)
      print('------------------------------------------------------------------------')
      if response.message.tool_calls:
        for tc in response.message.tool_calls:
          if tc.function.name in available_functions:
            print(f"Calling {tc.function.name} with arguments {tc.function.arguments}")
            result = available_functions[tc.function.name](**tc.function.arguments)
            print(f"Result: {result}")
            print('------------------------------------------------------------------------')
            # add the tool result to the messages
            messages.append({'role': 'tool', 'tool_name': tc.function.name, 'content': str(result)})
      else:
        # end the loop when there are no more tool calls
        break

  return '', None, messages[-1]['content']

def get_initial_prompt(protein):
  '''
  '''
  scoring_args[1] = protein
  #random_list, excluded_list = make_random_list(10)
  #first_list = sub_cycle(random_list, scoring_args)
  #context = ''
  #for smiles, score in first_list:
  #    context += f"{smiles}: {score}\n"

  with open('adversarial_set.md', 'r') as f:
    context = f.read()
  first_prompt = f'''
  Here is a list of molecules and their docking scores:
  {context}\n'''

  blank, img, mes = chat_turn(first_prompt)
  #print(mes[-1])
  
  #chat_history.append({'role': 'user', 'content': 'User sent protein name'})
  #chat_history.append({'role': 'assistant', 'content': 'Assistant running sub_cycle'})
  #chat_history.append({'role': 'user', 'content': first_prompt})
  #chat_history.append({'role': 'assistant', 'content': mes[-1]})

  return mes

start_chat()

date_string = time.strftime("%Y-%m-%d_%H-%M-%S")
filename = f'../results/DeepSeek_FIRST/adversary_design_{date_string}.md'
with open(filename, 'w') as f:
    f.write(f'# Adversarial Design Session - {date_string}\n\n')

text_av = get_initial_prompt('HMGCR')
with open(filename, 'a') as f:
    f.write('# Initial model response:\n')
    f.write(text_av + '\n') 

while text_av != 'Done':

    ant_response = adversary(text_av)
    with open(filename, 'a') as f:
        f.write('\n# Adversary feedback:\n')
        text_av = ant_response+'\n'
        f.write(text_av)

    _, _, text_av = chat_turn(ant_response)
    with open(filename, 'a') as f:
        f.write('\n# Model response:\n')
        f.write(text_av + '\n')