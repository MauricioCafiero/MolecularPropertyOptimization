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
          'devstral-2:123b', 'cogito-2.1:671b', 
          'nemotron-3-nano:30b', 'gemini-3-flash-preview', 'kimi-k2:1t']

# 'deepseek-v3.2', 'qwen3-next', 'qwen3-coder:480b', 'qwen3-vl:235b', 'qwen3.5', 'glm-5', 
# r'glm-4.6', r'kimi-k2.5', 'kimi-k2:1t', 'ministral-3:14b', 'minimax-m2.1',


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
{HL_task_specific_prompt}
'''
print('created_prompt')
#first_prompt = 'HMGCR'
first_prompt = 'Lowest possible HOMO LUMO gap.'

for model in models:

    client = Client(host = 'https://ollama.com',
                headers={'Authorization': f'Bearer {key}'})
    
    messages = []
    messages.append({
               'role': 'system', 'content': sys_message
            })
    messages.append({
                'role': 'user', 'content': first_prompt
            })

    res = client.chat(model, messages=messages)
    answer = res.message.content

    print(answer)

    path = "../results/HL/ZERO_SHOT/ollama_replies.md"
    with open(path, 'a', encoding = 'utf-8') as f:
        f.write(f'# {model} =========================================================\n')
        f.write(answer + '\n\n')