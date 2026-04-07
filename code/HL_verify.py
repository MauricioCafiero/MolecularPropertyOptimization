from pyscf import scf, dft, gto
import pyscf
from pyscf import lib
from rdkit import Chem
from rdkit.Chem import AllChem
import time, datetime, os, sys

#get number of cores
num_cores = os.cpu_count()
print(f'Number of cores: {num_cores}')
lib.num_threads(num_cores)

scoring_args = [num_cores, 'cam-b3lyp']

def scoring_function(smiles: str):
  '''
  receives a smiles string and returns the HOMO-LUMO gap calculated
  with a user-specified DFT method.

    Args:
      smiles: SMILES string for molecule

    Returns:
      gap: HOMO-LUMO gap in eV
      None: None
  '''
  try:
    atoms_list = ""
    mol = Chem.MolFromSmiles(smiles)
    molH = Chem.AddHs(mol)
    AllChem.EmbedMolecule(molH)
    AllChem.MMFFOptimizeMolecule(molH)
    xyz_string = f""
    for atom in molH.GetAtoms():
      atoms_list += atom.GetSymbol()
      pos = molH.GetConformer().GetAtomPosition(atom.GetIdx())
      xyz_string += f"{atom.GetSymbol()} {pos[0]} {pos[1]} {pos[2]}; "

    charge = 0
    for i,char in enumerate(smiles):
      if char == '-' and smiles[i+1] != 'c':
        charge -= 1
      elif char == '+':
        charge += 1

    new_mol = gto.M(
      atom  = xyz_string,
      charge = charge,
      spin = 0,
      basis = 'sto-3g',
      symmetry= True)

    dft_test = dft.RKS(new_mol)
    dft_test.xc = scoring_args[1]

    start = time.time()
    energy = dft_test.kernel()
    end = time.time()

    for i, occ in enumerate(dft_test.mo_occ):
      if occ == 0:
        homo_n = i-1
        lumo_n = i
        gap = (dft_test.mo_energy[lumo_n] - dft_test.mo_energy[homo_n])*27.21
        break

    total_time = end-start
    print(f'The HOMO-LUMO gap for {smiles} is: {gap:.3f} and took {total_time:.3f} seconds')
  except:
    print('Could not calculate gap')
    return 100.0

  return gap.item()

gemini_smiles = [
        'c1ccc2cc3cc4c(S([NH3+]))c(S([NH3+]))c5c(S([NH3+]))c(S([NH3+]))c6c(S([NH3+]))c(S([NH3+]))c7c([N+](=O)[O-])cc8cc9cc%10ccccc%10cc9cc8cc7cc6cc5cc4cc3cc2c1',
        'c1ccc2cc3cc4cc5cc6c(S([NH3+]))c(S([NH3+]))c7c(S([NH3+]))c(S([NH3+]))c8cc9cc%10cc%11cc%12ccccc%12cc%11cc%10cc9cc8cc7cc6cc5cc4cc3cc2c1',
        'c1ccc2cc3c(S([NH3+]))c(S([NH3+]))c4c(S([NH3+]))c(S([NH3+]))c5c(S([NH3+]))c(S([NH3+]))c6cc7cc8ccccc8cc7cc6cc5cc4cc3cc2c1'
]



gpt_smiles = [
        'c1(C#CC#N)ccc2c(C#C(C#N))c3c(C#C(C#N))cc(C#CC#N)c(C#CC#N)c3c(C#Cc7ccc8cc9ccccc9cc8c7)c2c1',
        'c1(C#C(C#N))ccc2c(C#C(C#N))c3c(C#C(C#N))cc(C#CC#N)c(C#CC#N)c3c(C#Cc7ccc8cc9ccccc9cc8c7)c2c1',
        'c1([N+](=O)[O-])ccc2c(C#C(C#N))c3c(C#C(C#N))cc(C#CC#N)c(C#CC#N)c3c(C#Cc7ccc8cc9ccccc9cc8c7)c2c1'
]

ant_smiles = [
        'c1(OC)c(N(C)c1c(N(C(C)C)C)c(C#N)c(C(=O)C#N)cc1)cc2cc(C(=O)C(C#N)(C#N))ccc2c1',
        'c1(OC)c(N(C)c1cc(C#N)c(C(=O)C#N)cc1)cc2cc(C(=O)C(C#N)(C#N))cc(N(C(C)C)C)c2c1',
        'c1(OC)c(N(C)c1cc(C#N)c(C(=O)C#N)cc1)cc2cc(C(=O)C(C#N)(C#N))cc(OC)c2c1'
]

corrected_ant_smiles = [
        'c1(OC)c(N(C)c6c(N(C(C)C)C)c(C#N)c(C(=O)C#N)cc6)cc2cc(C(=O)C(C#N)(C#N))ccc2c1',
        'c1(OC)c(N(C)c6cc(C#N)c(C(=O)C#N)cc6)cc2cc(C(=O)C(C#N)(C#N))cc(N(C(C)C)C)c2c1',
        'c1(OC)c(N(C)c6cc(C#N)c(C(=O)C#N)cc6)cc2cc(C(=O)C(C#N)(C#N))cc(OC)c2c1'
]

model_smiles = {
    'gemini_smiles': gemini_smiles,
    'gpt_smiles': gpt_smiles,
    'ant_smiles': ant_smiles,
    'corrected_ant_smiles': corrected_ant_smiles
}

for name, smiles_list in model_smiles.items():
  ave = 0.0
  count = 0
  print(f'Analysing {name} =======================================')
  for smile in smiles_list:
    mol = Chem.MolFromSmiles(smile)
    if mol != None:
      score = scoring_function(smile)
      ave += score
      count += 1
 #     print(f'{smile} : {score}')
    else:
      print(f'invalid smiles: {smile}')
  print('')
  try:
    print(f'Average for {name} is: {ave/count}')
    print('======================================================')
    print('')
  except:
    print(f'No valid SMILES')
