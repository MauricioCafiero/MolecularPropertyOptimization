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
  'CC(C)C[C@H](O)C[C@H](O)CCC(=O)O-c1ccc(cc1)C2(c3ccccc3)Cc4ccccc42',   #zero gpt
  'c1c(C(O)CC(O)C(=O)O)c(cc(n1)C(C)C)C(=O)Nc1ccccc1C(C)C',      # zero claude
  'CC(C)n1c(C2=CC=C(F)C=C2)c(C2=CC3=CC=CC=C3C=C2)c(\C=C\[C@H](O)C[C@H](O)CC(=O)O)c1',  # zero gemini
  'O=C(O)CC[C@H](O)C[C@H](O)CCc1cnc(-c2ccc(S(N)(=O)=O)cc2)nc1',  # zero deepseek
  'O=C(O)CC(O)CC(O)CC1CCc2c1cc(C(F)(F)F)cc2-c1ccccc1', # zero kimik2
  'CC(C)CCCC(C)C1CCC2C(C1)C(=O)O[C@@H]2C(=O)OC1=CC(=C(C=C1)Cl)C(F)(F)F',     # zero gpt oss120
  'CC12CCC(=O)C3CC(C(=O)OCCc4occc4)C3(O)C1C2',   # zero gpt oss20
  'CC(C)C(=O)O[C@@H](C1CCC2=CC=CC=C21)C(=O)N[C@@H](CC(O)=O)C(=O)O',  # zero devstral
  'CC(C)C1=CC(=C(C=C1)C2=C(NC(=O)NC2=O)C3=CC=CC=C3)O',   # zero cogito
  'CCOC(=O)NCC(=O)NCC1=CC=C(C=C1)C(=O)O',    # zero nemotron
  'O=C(O)Cc1cccc(n1)c2ccc3ccccc3c2',    # zero frag gpt
  'CC(C)C[C@H](O)[C@H](C)C(=O)Oc1ccc2ccccc2c1-c1ccccc1C(=O)O',  # zero frag claude
  'OC(=O)C[C@H](O)C[C@H](O)/C=C/c1c(-c2ccc(F)cc2)c2ccccc2nc1C(C)C',  # zero frag gemini
  'C(C(=O)[O-])c1ccc2cc3ccccc3cc2c1',  # zero frag deepseek
  'NCc1cc2cc3ccccc3cc2cc1CC(=O)[O-]', # zero frag kimik2
  'c1ccc2ccccc2c1CC(C(O)CO)C(=O)O',  # zero frag gpt oss120
  'c1ccc2cc3ccccc3cc2c1C(=O)[O-]', # zero frag gpt oss20 
  'CC(C)(C)c1ccc2cc3ccccc3cc2c1C(=O)O[C@H](C)C(=O)N1CCN(C)CC1', # zero frag devstral
  'CC(N(C)C)C(CC1=CC=CC2=CC3=CC=CC=C3CC2=C1)C(=O)[O-]', # zero frag cogito
  'O=c1cc(-c2ccc(C=C([N+](=O)[O-]))cc2)oc2cccc(C(C(=O)[O-]))c12', # one shot gpt
  'O=c1cc(-c2cc3ccccc3cc2C(=O)[O-])oc2c(C(C(=O)[O-]))ccc(C(=O)[O-])c12', # one shot claude
  '[O-]C(=O)Cc1cccc2oc(cc(=O)c12)-c3ccc4ccccc4c3', # one shot gemini
  'O=c1cc(-c2cccc(C(C(=O)[O-]))c2)oc2cccc(C=C([N+](=O)[O-]))c12', # one shot deepseek
  'O=C(O)C(C(=O)O)c1cc2cc3cc4ccccc4cc3cc2o1', # one shot kimik2
  'O=c1c(C(=O)[O-])c(-c2ccc(C(=O)[O-])cc2)oc2cccc(C(=O)[O-])c12', # one shot gpt oss120
  'O=c1c(O(C#N))c(-c2cc(C(C(=O)[O-]))ccc2)oc2ccccc12', # one shot gpt oss20
  'O=c1cc(-c2ccccc2)oc2cccc(C(C(=O)[O-]))c12', # one shot devstral
  'O=c1cc(-c2cccc(C(C(=O)[O-]))c2)oc2cccc(C(C(=O)[O-]))c12', # one shot cogito
  'c1c2c(ccccc2)c(ccccc1)C(=O)Oc3ccccc3C(=O)Oc4ccccc4' # one shot nemotron
]

top_names = ['GPT5p2', 'Claude', 'Gemini', 'DeepSeek', 'KimiK2', 'GPT_OSS120', 'GPT_OSS20', 'DevStral', 'Cogito', 'NemoTron',
             'GPT_Frag', 'Claude_Frag', 'Gemini_Frag', 'DeepSeek_Frag', 'KimiK2_Frag', 'GPT_OSS120_Frag', 'GPT_OSS20_Frag', 'DevStral_Frag', 'Cogito_Frag',
             'GPT_One_Shot', 'Claude_One_Shot', 'Gemini_One_Shot', 'DeepSeek_One_Shot', 'KimiK2_One_Shot', 'GPT_OSS120_One_Shot', 'GPT_OSS20_One_Shot', 'DevStral_One_Shot', 'Cogito_One_Shot', 'NemoTron_One_Shot']

top_scores = [
  -7.70,
  -8.30,
  -8.10,
  -7.40,
  -8.30,
  -7.40,
  -6.90,
  -7.20,
  -8.00,
  -7.50,
  -8.30,
  -8.10,
  -8.50,
  -7.70,
  -7.40,
  -6.70,
  -7.60,
  -8.30,
  -7.00,
  -8.90, 
  -9.00,
  -9.20,
  -8.20,
  -7.50,
  -7.90,
  -7.50,
  -8.60,
  -8.50,
  -9.10
]

assert len(top_names) == len(top_smiles) == len(top_scores), "Length of names, smiles, and scores lists must be the same."
print(f'Found {len(top_names)} unique names, {len(top_smiles)} unique smiles, and {len(top_scores)} unique scores.')

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
