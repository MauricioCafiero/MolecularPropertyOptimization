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

openai_smiles = [
    "CC(C)C[C@H](O)C[C@H](O)CCCn1nnnc1-c2ccc(cc2)C(c3ccccc3)(c4ccccc4)O",
    "CC(C)C[C@H](O)C[C@H](O)CCCP(=O)(O)O-c1ccc(cc1)C(c2ccccc2)(c3ccccc3)O",
    "CC(C)C[C@H](O)C[C@H](O)CCC(=O)OCCc1nc2ccccc2n1-c3ccc(cc3)C(c4ccccc4)(c5ccccc5)O",
    "CC(C)C[C@H](O)C[C@H](O)CCC(=O)OCCNS(=O)(=O)c1ccc(cc1)C(c2ccccc2)(c3ccccc3)O",
    "CC(C)C[C@H](O)C[C@H](O)CCC(=O)O-c1ccc(cc1)C2(c3ccccc3)Cc4ccccc42",
]

# Anthropic
anthropic_smiles = [
    "CC(C)c1c(C(=O)Nc2ccccc2C(=O)O)c(c(c1)C)C(O)CC(O)C(O)=O",
    "CC(C)C1=C(C(=O)O)C2CCC(O)C(O)C2(C)C1C(O)CC(O)C(=O)O",
    "CC(C)c1c(C(=O)Nc2ccc(F)cc2)c(cc1C(O)CC(O)C(O)=O)CCc1ccccc1",
    "c1c(C(O)CC(O)C(=O)O)c(cc(n1)C(C)C)C(=O)Nc1ccccc1C(C)C",
    "CC(C)C1=C(C(=O)O)C(C)C(C)(O)C1C(O)CC(O)C(O)=O",
]

# deepseek-v3.1:671b
deepseek_v3_smiles = [
    "O=C(O)CC[C@H](O)C[C@H](O)CCc1c2ccccc2n(CC3CCCCC3)c1C",
    "O=C(O)C[C@H](O)CC[C@H](O)CCc1cnc2c(c1)ccc(c2)F",
    "O=C(O)C[C@H](O)CC[C@H](O)CCc1c(CN2CCOCC2)nc2ccc(C(F)(F)F)cc12",
    "O=C(O)C[C@H](O)CC[C@H](O)CCS(=O)(=O)c1ccc(CN2CCCCC2)cc1",
    "O=C(O)CC[C@H](O)C[C@H](O)CCc1cnc(-c2ccc(S(N)(=O)=O)cc2)nc1",
]

# gpt-oss:120b
gpt_oss_120b_smiles = [
    "CC(C)CCCC(C)C1CCC2C(C1)C(=O)O[C@@H]2C(=O)OCC(C)C",
    "CC(C)CCCC(C)C1CCC2C(C1)C(=O)O[C@@H]2C(=O)OC(C)(C)C",
    "CC(C)CCCC(C)C1CCC2C(C1)C(=O)O[C@@H]2C(=O)OC(C)C1=CC=CC=C1F",
    "CC(C)CCCC(C)C1CCC2C(C1)C(=O)O[C@@H]2C(=O)OCC1=CN=CN1",
    "CC(C)CCCC(C)C1CCC2C(C1)C(=O)O[C@@H]2C(=O)OC1=CC(=C(C=C1)Cl)C(F)(F)F",
]

# gpt-oss:20b
gpt_oss_20b_smiles = [
    "CC12CCC(=O)C3CC(C(=O)OCCc4occc4)C3(O)C1C2",
    "CCCCCCCCCC(=O)C(O)C1(C)C(C(=O)OCCc2ncccc2)C(C)C1C",
    "CC12CC(O)C3(C)C(=O)C(=O)OC(C)C1C3OC2",
    "CC(C)(C)COC(=O)C1CC(C(=O)OCCc2c(C)cccc2)C(C)C1C",
    "CC12CCCC(=O)C(O)C1NC(=O)S(=O)(=O)c3ccccc3",
]

# devstral-2:123b
devstral_2_smiles = [
    "CC(C)C(=O)O[C@@H](Cc1ccccc1)C(=O)N[C@@H](CC2=CC=C(C=C2)O)C(=O)O",
    "CC(C)C(=O)O[C@@H](Cc1ccc(F)cc1)C(=O)N[C@@H](CCC(O)=O)C(=O)O",
    "CC(C)C(=O)O[C@@H](C1CCC2=CC=CC=C21)C(=O)N[C@@H](CC(O)=O)C(=O)O",
    "CC(C)C(=O)O[C@@H](C1CCN(C)CC1)C(=O)N[C@@H](CCc2ccco2)C(=O)O",
    "CC(C)C(=O)O[C@@H](Cc1ccc(CC(C)C)cc1)C(=O)N[C@@H](CC(O)=O)C(=O)O",
]

# cogito-2.1:671b
cogito_2_smiles = [
    "CC(C)C1=CC(=C(C=C1)C2=CC(=O)NC(=O)N2C3CCCCC3)O",
    "CC(C)C1=CC(=C(C=C1)C2=C(NC(=O)NC2=O)C3=CC=CC=C3)O",
    "CC(C)C1=CC(=C(C=C1)C2=CC(=O)NC(=O)NC2C3=CC=CC=C3)OC",
    "CC(C)C1=CC(=C(C=C1)C2=NC(=O)NC(=O)N2C3CCCC3)O",
    "CC(C)C1=CC(=C(C=C1)C2=CC(=O)NC(=O)NC2C3CCC(CC3)O)O",
]

# nemotron-3-nano:30b
nemotron_3_nano_smiles = [
    "CC1=CC(C(=C(C=C1)C(=O)O)O)C(=O)NCC(=O)N",
    "CC(C)(C)C(=O)O)C(=O)NCC(=O)N",
    "O=C(N[C@H](C)C(=O)O)C(N[C@H]1CCC[CH]1)C1=CC=C(C=C1)C(=O)O",
    "O=C(C)C1=CC=CC(=C1)C(O)=OC(=O)NCC(=O)N",
    "CCOC(=O)NCC(=O)NCC1=CC=C(C=C1)C(=O)O",
]

# gemini-3-flash-preview
gemini_3_flash_preview_smiles = [
    "CC(C)c1c(\\C=C\\[C@H](O)C[C@H](O)CC(=O)O)c2cc(F)ccc2nc1N(C)S(=O)(=O)C",
    "CC(C)n1c(C2=CC=C(F)C=C2)c(C2=CC3=CC=CC=C3C=C2)c(\\C=C\\[C@H](O)C[C@H](O)CC(=O)O)c1",
    "CC(C)c1c(\\C=C\\[C@H](O)C[C@H](O)CC(=O)O)c(c(nc(n1)NS(=O)(=O)C(F)(F)F)C2=CC=C(F)C=C2)",
    "CC(C)c1c(\\C=C\\[C@H](O)C[C@H](O)CC(=O)O)c(c2cc(C(=O)NC)ccc12)C3=CC=C(F)C=C3",
    "CC(C)c1c(\\C=C\\[C@H](O)C[C@H](O)CC(=O)O)c(c2noc(c12)C3=CC=C(F)C=C3)",
]

# kimi-k2:1t
kimi_k2_smiles = [
    "O=C(O)CC(O)CC(O)CC1CC(c2ccc(F)cc2)CC1c1ccc(F)cc1",
    "O=C(O)CC(O)CC(O)Cc1cccc2c1oc1cc(C(F)(F)F)ccc12",
    "O=C(O)CC(O)CC(O)CC1CCc2c1cc(C(F)(F)F)cc2-c1ccccc1",
    "O=C(O)CC(O)CC(O)Cc1cccc2nc(C3CC3)ccc12",
    "O=C(O)CC(O)CC(O)CC1CCc2c1cc(Oc1cc(F)cc(F)c1)cc2",
]

# Dictionary with all model SMILES lists
model_smiles = {
    "openai": openai_smiles,
    "anthropic": anthropic_smiles,
    "deepseek-v3.1": deepseek_v3_smiles,
    "gpt-oss:120b": gpt_oss_120b_smiles,
    "gpt-oss:20b": gpt_oss_20b_smiles,
    "devstral-2": devstral_2_smiles,
    "cogito-2.1": cogito_2_smiles,
    "nemotron-3-nano": nemotron_3_nano_smiles,
    "gemini-3-flash-preview": gemini_3_flash_preview_smiles,
    "kimi-k2": kimi_k2_smiles,
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
