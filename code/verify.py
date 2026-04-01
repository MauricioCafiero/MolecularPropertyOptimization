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

target_name = 'HMGCR'


one_shot_smiles = ['O=c1cc(-c2ccccc2)oc2cccc(N(S(=O)(=O)C))c12',
                   'O=c1cc(-c2ccc3ccccc3c2)oc2cccc(N(C(=O)))c12',
                   'O=c1cc(-c2ccc(F)cc2)oc2cccc(N(C(=O)))c12']

one_shot_scores = [-8.3,-9.2,-8.7]

one_shot_logp = [2.83, 4.18, 3.17]

openai_tools_smiles = ['O=c1cc(-c2ccc(NC(=O)C)cc2)oc2cccc(N(C(=O)))c12',
                'O=c1cc(-c2cc(F)c(NC(=O)C)cc2)oc2cccc(N(C(=O)))c12']

openai_tools_scores = [-9.1, -9.2]

openai_tools_logp = [2.99, 3.13]

ant_smiles = ['O=c1c(O)c(-c2c(C)cc(C(=O)N)cc2)oc2c(F)ccc(C(=O)N)c12',
              'O=c1c(O)c(-c2c(C)cc(C(=O)N(C)C)cc2)oc2c(F)ccc(C(=O)N)c12',
              'O=c1c(O)c(-c2c(C)cc(C(=O)N(C)C)cc2)oc2c(F)ccc(C(=O)N(C)C)c12',
              'O=c1c(O)c(-c2c(C(=O)[O-])c(NC(=O)C)ccc2)oc2c(C(F)(F)(F))ccc(C(=O)N)c12',
              'O=c1c(O)c(-c2c(C(=O)[O-])c(NC(=O)C)c(F)cc2)oc2cc(F)cc(C)c12'
             ]
ant_scores = [-9.2, -8.6, -8.3, -9.4, -9.9  ]

ant_logp = [1.881, 2.414, 3.017, 1.605, 2.07 ]

ant_qed = [0.657, 0.720,0.714, 0.545, 0.709  ]

openai_smiles = ['O=c1c(O)c(-c2ccc(CC(C)(C)C)cc2)oc2cccc(C(C(=O)O))c12',
                 'O=c1c(O)c(-c2ccc(OC(F)(F)(F))cc2)oc2cccc(C(C(=O)O))c12']

openai_scores = [-9.2, -9.1]

openai_logp = [4.38, 3.69]

openai_qed = [0.715, 0.717 ]

gem_smiles = ['O=c1cc(-c2cc(F)c(F)cc2)oc2cc(F)cc(CC(=O)[O-])c12',
              'O=c1cc(-c2cc(F)c(F)cc2)oc2cccc(CC(=O)[O-])c12',
              'O=c1cc(-c2ccc(F)cc2)oc2cc(F)cc(CC(=O)[O-])c12']


gem_scores = [-9.0, -8.9, -8.8]

gem_logp = [2.17, 2.03, 2.03]

gem_qed = [0.74, 0.74, 0.74]

hash_lists = {
    'one_shot': (one_shot_smiles, one_shot_scores, one_shot_logp),
    'openai_tools': (openai_tools_smiles, openai_tools_scores, openai_tools_logp),
    'ANTHROPIC': (ant_smiles, ant_scores, ant_logp, ant_qed),
        'OPENAI': (openai_smiles, openai_scores, openai_logp, openai_qed),
        'GEMINI': (gem_smiles, gem_scores, gem_logp, gem_qed)
}

for name, set_tuple in hash_lists.items():
  ave = 0.0
  count = 0
  print(f'Analysing {name} =======================================')
  for smile, truth in zip(set_tuple[0], set_tuple[1]):
    mol = Chem.MolFromSmiles(smile)
    if mol != None:
      score, aux = docking(smile)
      ave += score
      count += 1
      print(f'{smile} : {score}')
      if isclose(score, truth, abs_tol=0.5):
        print('score validated.')
    else:
      print(f'invalid smiles: {smile}')
  print('')
  try:
    print(f'Average for {name} is: {ave/count}')
    print('======================================================')
    print('')
  except:
    print(f'No valid SMILES')
