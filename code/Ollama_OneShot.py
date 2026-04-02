from ollama import Client
import sys
import os
import platform

sys.path.append('code')
from docking_module import *
#from HL_module import *

def get_api_key():
    '''
    Fetch API key based on the operating system.
    - Linux/Mac: Uses environment variable OLLAMA_API_KEY
    - Windows: Uses command line argument or environment variable
    '''
    current_os = platform.system()

    if current_os in ['Linux', 'Darwin']:  # Darwin is macOS
        # Linux/Mac: Use environment variable
        key = os.environ.get('OLLAMA_API_KEY')
        if not key:
            raise ValueError(
                "OLLAMA_API_KEY environment variable not set.\n"
                "Set it with: export OLLAMA_API_KEY='your-api-key'"
            )
        return key

    elif current_os == 'Windows':
        # Windows: Try command line arg first, then environment variable
        if len(sys.argv) > 1:
            key = sys.argv[1]
        else:
            key = os.environ.get('OLLAMA_API_KEY')

        if not key:
            raise ValueError(
                "API key not provided. Either:\n"
                "1. Pass it as a command line argument: python ollama_cloud.py <key>\n"
                "2. Set OLLAMA_API_KEY environment variable"
            )
        return key

    else:
        # Unknown OS: try environment variable as fallback
        key = os.environ.get('OLLAMA_API_KEY')
        if not key:
            raise ValueError(
                f"Unsupported OS: {current_os}. "
                "Set OLLAMA_API_KEY environment variable."
            )
        return key


key = get_api_key()

models = ['deepseek-v3.1:671b', 'gpt-oss:120b', 'gpt-oss:20b', 
          'devstral-2:123b', 'cogito-2.1:671b', 'minimax-m2', 
          'nemotron-3-nano:30b', 'gemini-3-flash-preview']

# 'deepseek-v3.2', 'qwen3-next', 'qwen3-coder:480b', 'qwen3-vl:235b', 'qwen3.5', 'glm-5', 
# r'glm-4.6', r'kimi-k2.5', 'kimi-k2:1t', 'ministral-3:14b', 

  with open('adversarial_set.md', 'r') as f:
    context = f.read()
  first_prompt = f'''
  Here is a list of molecules and their docking scores:
  {context}\n'''

sys_message = SystemMessage(content=f'''
{task_specific_prompt}

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
''')
print('created_prompt')

for model in models:

    client = Client(host = 'https://ollama.com',
                headers={'Authorization': f'Bearer {key}'})
    
    messages = []
    messages.append({
                'role': 'user', 'content': first_prompt
            })

    res = client.chat(model, messages=messages)
    answer = res.message.content

    print(answer)

    path = "../results/ONE_SHOT/ollama_replies.md"
    with open(path, 'a', encoding = 'utf-8') as f:
        f.write(f'# {model} =========================================================\n')
        f.write(answer + '\n\n')
