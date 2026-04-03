import sys
import os
from anthropic import Anthropic
from openai import OpenAI
#from google.colab import userdata

anthropic_key = os.getenv("ANTHROPIC_KEY")
#anthropic_key = userdata.get("ANTHROPIC_KEY")
ant_client = Anthropic(api_key=anthropic_key)

openai_key = os.getenv("OPENAI_API_TOKEN")
#openai_key = userdata.get("OPENAI_API_KEY")
openai_client = OpenAI(api_key=openai_key)

with open('adversarial_set.md', 'r') as f:
    context = f.read()
first_prompt = f'''
  Here is a list of molecules and their docking scores:
  {context}\n'''


dock_task_specific_prompt = '''# You are a drug design assistant. In the first user message you will
see a list of molecule SMILES strings and docking scores.
The lower the docking score (the more negative), the more affinity the
molecule has for the protein in question. Your task is to use the information 
in the list to learn trends about what makes a molecule a good binder, and then 
use those trends to suggest new molecules that should have better docking scores 
(more negative) than the ones in the list.'''

HL_task_specific_prompt = '''# You are a materials science assistant. In the first user
message you will see a list of molecule SMILES strings and their corresponding HOMO-LUMO gaps.
Your task is to use the information in the list to learn trends about what makes a molecule 
have a small or large HOMO-LUMO gap, and then use those trends to suggest new molecules 
that should have the smallest possible HOMO-LUMO gap.
'''

sys_message = f'''
{HL_task_specific_prompt}

## You will first:
- Read the list of molecule SMILES and scores
- Ascertain any features of the molecules that contribute to the desired score. For example, if,
from one molecule to the next, the addition of an O group makes the score better.
- Gather all of these trends across all of the molecules.

## Once you have ascertained the trends:
- Use the trends you learned to suggest 1-5 new molecules that obey the trends you found
and which should have a better score than the molecules in the list.
- Provide reasoning as to why you created those new molecules.
- Estimate the new scores.
'''
print('created_prompt')

def get_openai_response():
  '''
  '''
  adversary_message = openai_client.responses.create(
      model="gpt-5.2",
      instructions = sys_message,
      input=first_prompt
    )
    
  response = adversary_message.output_text
  return response

def get_ant_response():
  '''
  '''
  adversary_message = ant_client.messages.create(
    model="claude-haiku-4-5-20251001",
    max_tokens=4000,
    system = sys_message,
    messages=[
        {"role": "user", "content": first_prompt},])

  response = adversary_message.content[0].text

  return response

for model in [get_openai_response, get_ant_response]:
  answer = model() 
  print(answer)

  path = "../results/ONE_SHOT/gtp_ant_replies.md"
  with open(path, 'a', encoding = 'utf-8') as f:
      f.write(f'# {model} =========================================================\n')
      f.write(answer + '\n\n')
