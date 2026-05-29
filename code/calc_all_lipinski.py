from rdkit import Chem
from rdkit.Chem import Draw, QED
from all_mol_lists import *

def scoring_function(smiles: str):
  '''
    calculates a property of the molecule based on the scoring_args. 
    If the calculation fails, returns -999.
  '''
  try:
    mol = Chem.MolFromSmiles(smiles)
    qed = QED.default(mol)

    p = QED.properties(mol)

    lipinski_hash = {'mw': 0, 'alogp': 1, 'hba': 2, 'hbd': 3, 'psa': 4, 'rb': 5, 'ar': 6, 'um': 7}

    alogp = p[lipinski_hash['alogp']]

    return qed, alogp, mol
  
  except Exception as e:
      print(f"Error processing {smiles}: {e}")
      return -999, -999, None

for name, list in hash_lists.items():
    print(f'Processing {name}...')
    legs = ''
    for smiles in list:
        qed, alogp, mol = scoring_function(smiles)
        legs += f'{smiles} : properties\n'
        legs += f'aLogP = {alogp:.2f}, QED = {qed:.2f}\n'

    with open(f'../results/lipinski_results_all.txt', 'a') as f:
        f.write(f'{name}:\n')
        f.write(legs)
        f.write('----------------------------------------------------------\n')

    print(f'Finished processing {name}')

