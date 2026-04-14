from ollama import Client
import sys
import os
import platform
from rdkit import Chem
from rdkit.Chem import QED, Draw


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

scoring_args = [2.5, 'alogp']

def lipinski(smiles: str):
  '''
    calculates the aLogP of the molecule based on the scoring_args. 
    If the calculation fails, returns -999.

    Args:
    - smiles (str): The SMILES string of the molecule to be scored.
    Returns:
    - score (float): The calculated aLogP score of the molecule, or -999 if the calculation fails.
  '''
  
  mol = Chem.MolFromSmiles(smiles)
  qed = Chem.QED.default(mol)

  p = Chem.QED.properties(mol)

  lipinski_hash = {'mw': 0, 'alogp': 1, 'hba': 2, 'hbd': 3, 'psa': 4, 'rb': 5, 'ar': 6, 'um': 7}

  try:
    score = p[lipinski_hash[scoring_args[1]]]
  except:
    score = -999

  return score

key = get_api_key()

models = ['deepseek-v3.1:671b', 'gpt-oss:120b', 'gpt-oss:20b', 
          'devstral-2:123b', 'cogito-2.1:671b', 
          'nemotron-3-nano:30b', 'gemini-3-flash-preview',
          'kimi-k2:1t', 'kimi-k2.5']

model = models[-1]
client = Client(host = 'https://ollama.com',
            headers={'Authorization': f'Bearer {key}'})

available_functions = {
  'lipinski': lipinski
}

initial_input = input("Enter your question: ")
messages = [{'role': 'user', 'content': initial_input}]

while True:
    response = client.chat(
        model=model,
        messages=messages,
        tools=[lipinski],
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
  # continue the loop with the updated messages