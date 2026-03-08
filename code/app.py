from langchain_openai.chat_models import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from google.colab import userdata
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

from google.colab import userdata

sys.path.append('MolecularPropertyOptimization/code')
from frag_grow_colab import *

#get key from secrets
openai_key = userdata.get('OPENAI_API_KEY')
#openai_key = os.getenv("OPENAI_API_KEY")

tools = [grow_cycle, replace_groups, add_ring, remove_ring, make_random_list, list_rings]

model = ChatOpenAI(model_name="gpt-5.2", api_key=openai_key).bind_tools(tools)

class State(TypedDict):
  messages: Annotated[list, add_messages]

def model_node(state: State) -> State:
  res = model.invoke(state['messages'])
  return {'messages': res}

builder = StateGraph(State)
builder.add_node('model', model_node)
builder.add_node('tools', ToolNode(tools))
builder.add_edge(START, 'model')
builder.add_conditional_edges('model', tools_condition)
builder.add_edge('tools',  'model')

graph = builder.compile()
sys_message = SystemMessage(content='''
# You are a drug design assistant. In the first user message you will
see a list of molecule SMILES strings and docking scores.
The lower the docking score (the more negative), the more affinity the
molecule has for the protein in question.

## You will first:
- Read the list of molecule SMILES and scores
- Ascertain any features of the molecules that make them a good binder. For example, if,
from one molecule to the next, the addition of an O group makes the affinity stronger.
- Gather all of these trends across all of the molecules.

## If you need additional information to ascertain the trends, such as more modified
molecules and their docking scores, you have tools you can call to generate new
molecules and get their docking scores. You can use these tools as many times as you want
to gather information on the trends.

the tools include:
                            
- grow_cycle: starts with a molecule SMILES and adds substituents to it, docks them, and returns 
              a list of molecules and scores. You can use this tool to further explore modifications
              to promising molecules that you find in the input data. You can provide a list of
              substituents to add, or use the predefined sets: e_withdraw (electron withdrawing),
              e_donate (electron donating), withdraw_with_linkers (electron withdrawing with linkers), 
              donate_with_linkers (electron donating with linkers).

- replace_groups: starts with a molecule SMILES and replaces specific groups in it with new groups, returning a list of new
                  molecules and scores. This tool allows you to test specific hypotheses about how replacing certain
                  groups in a molecule might affect binding affinity. You can specify which groups to replace and
                  what to replace them with, or use the predefined sets of substituents mentioned above.

## Once you have ascertained the trends:
- Use the trends you learned to suggest 1-5 new molecules that obey the trends you found
and which should have more affinity than the molecules in the list.
- Provide reasoning as to why you created those new molecules.
- Estimate the new docking scores.

## You may ask te user for clarification if needed, but try to use the tools to gather as much information as you
can before asking for clarification.
''')

global messages
messages = [sys_message]

#@spaces.GPU
def start_chat():
  '''
  '''
  global chat_history, messages, reasoning
  chat_history = []
  reasoning = []
  messages = [sys_message]

#@spaces.GPU
def chat_turn(prompt: str):
  '''
  '''
  global chat_history, messages, reasoning
  human_message = HumanMessage(content=prompt)
  messages.append(human_message)
  local_history = [prompt]

  input = {
      'messages' : messages
  }

  for c in graph.stream(input):
    try:
      ai_mes = c['model']['messages'].content
      messages.append(AIMessage(ai_mes))
      if ai_mes != '':
        print(f'message is {ai_mes}')
        local_history.append(ai_mes)
    except:
      pass
    try:
      if os.path.exists('current_image.png'):
        if os.path.getmtime('current_image.png') > time.time() - 30:
          img = Image.open('current_image.png')
        else:
          img = None
      else:
        img = None
    except:
      img = None
    try:
      reasoning.append(c['tools']['messages'][0].content)
    except:
      pass

  if len(local_history) != 2:
    local_history.append('no message')

  #chat_history.append({'role': 'user', 'content': local_history[0]})
  #chat_history.append({'role': 'assistant', 'content': local_history[1]})
  chat_history.append(local_history)
  return '', img, chat_history

random_list = make_random_list(10)
first_list = sub_cycle(random_list)
context = ''
for smiles, score in first_list:
    context += f"{smiles}: {score}\n"

first_prompt = f'''
Here is a list of molecules and their docking scores:
{context}\n'''

start_chat()
chat_turn(first_prompt)


with gr.Blocks(fill_height=True) as MoleculeDesignApp:
  top = gr.Markdown('''
              # Molecule Design with AI and Docking
              ''')


  chat = gr.Chatbot()
  with gr.Row(equal_height = True):
    msg = gr.Textbox(label = 'query', scale = 8)
    sub_button = gr.Button("Submit", scale = 2)
  clear = gr.ClearButton([msg, chat])
  img_box = gr.Image()
  reasoning_box = gr.Textbox(label="Tool logs", lines = 20)
  msg.submit(chat_turn, [msg], [msg, img_box, chat]).then(send_reasoning, [], [reasoning_box])
  sub_button.click(chat_turn, [msg], [msg, img_box, chat])
  clear.click(start_chat, [], [])

  @gr.render(inputs=top)
  def get_speech(args):
    audio_file = 'MoDrAg_hello.mp3'
    with open(audio_file, 'rb') as audio_bytes:
                audio = base64.b64encode(audio_bytes.read()).decode("utf-8")
    audio_player = f'<audio src="data:audio/mpeg;base64,{audio}" controls autoplay></audio>'
    talk_ele = gr.HTML(audio_player)

MoleculeDesignApp.launch(mcp_server = True)