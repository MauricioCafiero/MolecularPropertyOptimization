from ollama import Client
import sys
import os
import platform


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

with open('HMGCR_input_set.md', 'r') as f:
    context = f.readlines()

context = '\n'.join(context)

first_prompt = f'''
# You are a drug design assistant. Below you will
see a list of molecule SMILES strings and docking scores.
The lower the docking score (the more negative), the more affinity the
molecule has for the protein in question. Your task is to use the information 
in the list to learn trends about what makes a molecule a good binder, and then 
use those trends to suggest new molecules that should have better docking scores 
(more negative) than the ones in the list.

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

Here is the list of molecules and their docking scores:
{context}\n
'''
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

    path = "model_replies.md"
    with open(path, 'a', encoding = 'utf-8') as f:
        f.write(f'# {model} =========================================================\n')
        f.write(answer + '\n\n')
