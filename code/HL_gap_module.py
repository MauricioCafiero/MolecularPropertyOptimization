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
  
  return gap.item(), None

task_specific_prompt = '''# You are a materials science assistant. In the first user
message you will see a list of molecule SMILES strings and their corresponding HOMO-LUMO gaps.
Your task is to use the information in the list to learn trends about what makes a molecule 
have a small or large HOMO-LUMO gap, and then use those trends to suggest new molecules 
that should have the smallest possible HOMO-LUMO gap.
'''
