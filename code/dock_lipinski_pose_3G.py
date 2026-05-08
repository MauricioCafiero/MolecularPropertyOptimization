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

def save_pose(pose_mol, pose_score, name):
  '''
    Save the bext pose (lowest score) from a docking run as an SDF file. 
    
    Args:
        pose_mol: the mol object for the best pose
        pose_score: the score for the best pose
        name: a name to use for the SDF file
    
    Returns:
        None; SDF file is saved.
  '''
  pose_mol.SetProp('_Name',str(pose_score))
  w = Chem.SDWriter(name)
  w.write(pose_mol)
  w.close()
  print(f"SDF file written for score {name}")

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

openai_smiles = [
  'CC1=C(C=C(C=C1)F)C(=O)NC2=CC(=CC(=C2)C(=O)O)COC(F)(F)F',
  'CC1=C(C=C(C=C1)F)C(=O)NC2=CC(=CC(=C2)C(=O)O)COC(=O)OC',
  'CC1=C(C=C(C=C1)F)C(=O)NC2=CC(=CC(=C2)C(=O)O)CO'
]

openai_orig_smiles = [
  'O=c1cc(-c2c(F)cccc2)oc2cccc(C(C(=O)[O-]))c12', #-8.7
  'O=c1cc(-c2ccc(C(=O)O)cc2)oc2cccc(C(C(=O)[O-]))c12', #-8.7
  'O=c1cc(-c2ccc(C#N)cc2)oc2cccc(C(C(=O)[O-]))c12' #-8.5
]

# Anthropic
anthropic_smiles = [
  'O=c1cc(-c2cc(c7ccc(C(=O)N)cc7)ccc2)oc2c(F)ccc(O)c12', #-9.6
]

# deepseek-v3.1:671b
deepseek_v3_smiles = [
  'O=c1cc(-c2cccc(C(C(C)C)C(=O)N)c2)oc2c(F)cccc12', #-9.2
  'O=c1cc(-c2cccc(C(C(C)C)C(=O)N)c2)oc2ccccc12', #-9.0
  'O=c1cc(-c2cccc(C(C(C)C)C(=O)N)c2)oc2ccc(F)cc12' #-9.1
]

# gemini-3-flash-preview
gemini_3_flash_preview_smiles = [
  'O=c1cc(-c2c(F)c(F)c(F)cc2)[nH]c2cc(F)cc(CC(=O)O)c12', #-9.1
  'Cn1c(-c2ccc3cc(F)ccc3c2)cc(=O)c2cc(F)cc(CC(=O)O)c12', #-9.6
  'Cn1c(-c2c(F)cc(F)cc2)cc(=O)c2cc(F)cc(CC(=O)O)c12' #-9.2
]

# kimi-k2:1t
kimi_k2_smiles = [
  'O=c1cc(-c2c(C)cccc2)oc2cc(F)cc(C(C(=O)[O-]))c12', #-8.9
  'O=c1cc(-c2c(C)cccc2)oc2cccc(C(C(=O)NS(=O)(=O)C))c12', #-8.0
  'O=c1cc(-c2c(C)cccc2)oc2cccc(C(C(=O)[O-]))c12' #-8.9
]


# Dictionary with all model SMILES lists
model_smiles = {
    'GPT5p2': openai_smiles,
    'GPT5p2_orig': openai_orig_smiles,
    'Claude': anthropic_smiles,
    'Gemini': gemini_3_flash_preview_smiles,
    'DeepSeek': deepseek_v3_smiles,
    'KimiK2': kimi_k2_smiles,
}


for name, smiles_list in model_smiles.items():
  ave = 0.0
  count = 0
  ave_qed = 0.0
  ave_alogp = 0.0
  model_idx = 0
  print(f'Analysing {name} =======================================')
  for smile in smiles_list:
    mol = Chem.MolFromSmiles(smile)
    if mol != None:
      score, aux = docking(smile)
      if model_idx == 0:
        filename = f'{name}_top_pose.sdf'
        save_pose(aux['ligand'], score, filename)
        model_idx += 1
      ave += score
      count += 1
      print(f'{smile} : docking score = {score:.2f} kcal/mol,')
      qed, alogp, mol = lipinski(smile)
      ave_qed += qed
      ave_alogp += alogp
      print(f'aLogP = {alogp:.2f}, QED = {qed:.2f}')
      print('')
    else:
      print(f'invalid smiles: {smile}')
      model_idx += 1
  print('')
  try:
    print(f'Average docking score for {name} is: {ave/count}')
    print(f'Average QED for {name} is: {ave_qed/count}')
    print(f'Average aLogP for {name} is: {ave_alogp/count}')
    print('======================================================')
    print('')
  except:
    print(f'No valid SMILES')
