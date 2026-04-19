from rdkit import Chem
from rdkit.Chem import Draw, QED

def scoring_function(smiles: str):
  '''
    calculates a property of the molecule based on the scoring_args. 
    If the calculation fails, returns -999.
  '''
  
  mol = Chem.MolFromSmiles(smiles)
  qed = QED.default(mol)

  p = QED.properties(mol)

  lipinski_hash = {'mw': 0, 'alogp': 1, 'hba': 2, 'hbd': 3, 'psa': 4, 'rb': 5, 'ar': 6, 'um': 7}

  alogp = p[lipinski_hash['alogp']]

  return qed, alogp, mol

knowns = [r'O=C(O)C[C@H](O)C[C@H](O)CCn2c(c(c(c2c1ccc(F)cc1)c3ccccc3)C(=O)Nc4ccccc4)C(C)C',
           r'OC(=O)C[C@H](O)C[C@H](O)\C=C\c1c(C(C)C)nc(N(C)S(=O)(=O)C)nc1c2ccc(F)cc2',
           r'O=C(O[C@@H]1[C@H]3C(=C/[C@H](C)C1)\C=C/[C@@H]([C@@H]3CC[C@H]2OC(=O)C[C@H](O)C2)C)C(C)(C)CC',
           r'O=C(O[C@@H]1[C@H]3C(=C/[C@H](C)C1)\C=C/[C@@H]([C@@H]3CC[C@H]2OC(=O)C[C@H](O)C2)C)[C@@H](C)CC',
           r'O=C(O)C[C@H](O)C[C@H](O)/C=C/c2c(c1ccccc1n2C(C)C)c3ccc(F)cc3',
           r'O=C(O)C[C@H](O)C[C@H](O)CC[C@H]2[C@H](/C=C\C1=C\[C@@H](O)C[C@H](OC(=O)[C@@H](C)CC)[C@@H]12)C']

names = ['Atorvastatin',
         'Rosuvastatin',
         'Simvastatin',
         'Lovastatin',
         'Fluvastatin',
         'Pravastatin']

alogp_list = []
qed_list = []
for name, smiles in zip(names, knowns):
    print(f'Processing {name}...')
    qed, alogp, mol = scoring_function(smiles)
    alogp_list.append(alogp)
    qed_list.append(qed)
    legs = f'{name}: QED={qed:.2f}, logP={alogp:.2f}'

    with open(f'../results/lipinski_known_results.txt', 'a') as f:
        f.write(f'{name}:\n')
        f.write(f'{smiles}: {legs}\n')
        f.write('---------------------------------------------------------------------------------\n')

    print(f'Finished processing {name}')

average_alogp = sum(alogp_list) / len(alogp_list)
average_qed = sum(qed_list) / len(qed_list)

with open(f'../results/lipinski_known_results.txt', 'a') as f:
    f.write(f'Average logP: {average_alogp:.2f}\n')
    f.write(f'Average QED: {average_qed:.2f}\n')
