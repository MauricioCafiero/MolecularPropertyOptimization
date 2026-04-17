from dockstring import load_target
import os
from math import isclose
from rdkit import Chem
from rdkit.Chem import QED

num_cores = os.cpu_count()
print(f'Using {num_cores} cores for docking.')

def docking(smiles: str):
  '''
    docks a molecule to the target and returns the docking score. If the docking fails, returns 0.0.
  '''
  target = load_target(target_name)
  try:
    score, aux = target.dock(smiles, num_cores)
  except:
    score = 0.0
    aux = None
  return score, aux

def lipinski(smiles: str):
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

target_name = 'HMGCR'

kimi_k2 = ['Cc1c(C)c2c(c3c(F)c(O)c(C(=O)N)c(C)c13)C(C)=C(C(=O)[O-])O2',
           'Cc1c(C)c2c(c3c(O)c(C(=O)N)c(C)c(C)c13)C(C)=C(C(=O)[O-])O2',
           'Cc1c(C)c2c(c3c(O)c(C(=O)N)c(C)c(F)c13)C(C)=C(C(=O)[O-])O2' ]


deepseek = ['O=c1c(F)c(-c2cnc(F)c(C)c2)oc2cccc(C(C(F)(F)O))c12', 
            'O=c1c(F)c(-c2cnc(F)c(C)c2)oc2c(OC)ccc(C(C(F)(F)O))c12', 
            'O=c1c(F)c(-c2cnc(F)c(C)c2)oc2c(C(=O)N)ccc(C(C(F)(F)O))c12', 
            'O=c1c(F)c(-c2cnc(F)c(C)c2)oc2c(C(F)(F)F)ccc(C(C(F)(F)O))c12']

# Dictionary with all model SMILES lists
model_smiles = {
    "deepseek-v3.2": deepseek,
    "kimi-k2": kimi_k2,
}
for name, smiles_list in model_smiles.items():
  ave = 0.0
  count = 0
  print(f'Analysing {name} =======================================')
  for smile in smiles_list:
    mol = Chem.MolFromSmiles(smile)
    if mol != None:
      score, aux = docking(smile)
      ave += score
      count += 1
      print(f'{smile} : docking score = {score:.2f} kcal/mol,')
      qed, alogp, mol = lipinski(smile)
      print(f'aLogP = {alogp:.2f}, QED = {qed:.2f}')
      print('')
    else:
      print(f'invalid smiles: {smile}')
  print('')
  try:
    print(f'Average docking score for {name} is: {ave/count}')
    print('======================================================')
    print('')
  except:
    print(f'No valid SMILES')