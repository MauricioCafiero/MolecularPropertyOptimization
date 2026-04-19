from dockstring import load_target
import os
from math import isclose
from rdkit import Chem

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
  w.close
  print(f"SDF file written for score {name}")

target_name = 'HMGCR'

top_smiles = [
    'O=c1c(O)c(-c2ccc(CC(C)(C)C)cc2)oc2cccc(C(C(=O)O))c12',
    'O=c1c(O)c(-c2c(C(=O)[O-])c(NC(=O)C)ccc2)oc2c(C(F)(F)(F))ccc(C(=O)N)c12', #mol 2
    'O=c1cc(-c2cc(F)c(F)cc2)oc2cccc(CC(=O)[O-])c12',
    'O=c1c(F)c(-c2cnc(F)c(C)c2)oc2c(C(F)(F)F)ccc(C(C(F)(F)O))c12', #mol 3
    'Cc1c(C)c2c(c3c(O)c(C(=O)N)c(C)c(C)c13)C(C)=C(C(=O)[O-])O2' #mol 1
]

top_names = ['GPT5p2', 'Claude', 'Gemini', 'DeepSeek', 'KimiK2']

top_scores = [-8.9, -9.4, -8.9, -8.3, -8.7]

for name, smile, score in zip(top_names, top_smiles, top_scores):
  print(f'Analysing {name} =======================================')
  mol = Chem.MolFromSmiles(smile)
  if mol != None:
    filename = f'{name}_top_pose.sdf'
    score, aux = docking(smile)
    save_pose(aux['ligand'], score, filename)
  else:
    print(f'invalid smiles: {smile}')
  print('')
