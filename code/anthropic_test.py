from anthropic import Anthropic

anthropic_key = os.getenv("ANTHROPIC_KEY")

client = Anthropic(api_key=anthropic_key)

chat_history = []

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

elita_message = client.messages.create(
model="claude-haiku-4-5-20251001",
max_tokens=2000,
messages=[
    {"role": "user", "content": first_prompt},
]
)

elita_text = elita_message.content[0].text

print(elita_text)