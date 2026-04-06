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

dock_task_specific_prompt = '''# You are a drug design assistant. Your task is to design a new molecules
with the best possible docking score (the most negative) to a particular protein target, given in the first user message.
You will deliver up to five potential molecules in SMILES format, along with reasoning for why you chose those molecules 
and an estimate of their docking scores.
'''

HL_task_specific_prompt = '''# You are a materials science assistant. Your task is to design new molecules with a particular
HOMO-LUMO gap (more information in the first user message). You will deliver up to five potential molecules in SMILES format, 
along with reasoning for why you chose those molecules and an estimate of their HOMO-LUMO gaps.
'''

sys_message = f'''
{dock_task_specific_prompt}
'''
print('created_prompt')
first_prompt = 'HMGCR'

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

for model, name in zip([get_openai_response, get_ant_response], ['OpenAI', 'Anthropic']):
  answer = model() 
  print(answer)

  path = "../results/ONE_SHOT/gtp_ant_replies.md"
  with open(path, 'a', encoding = 'utf-8') as f:
      f.write(f'# {name} =========================================================\n')
      f.write(answer + '\n\n')
