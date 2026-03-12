from rdkit import Chem
from rdkit.Chem import QED, Draw
import os

scoring_args = ['alogp']

def scoring_function(smiles: str):
  '''
    calculates a property of the molecule based on the scoring_args. 
    If the calculation fails, returns -999.
  '''
  
  mol = Chem.MolFromSmiles(smiles)
  qed = Chem.QED.default(mol)

  p = Chem.QED.properties(mol)

  lipinski_hash = {'mw': 0, 'alogp': 1, 'hba': 2, 'hbd': 3, 'psa': 4, 'rb': 5, 'ar': 6, 'um': 7}

  try:
    score = p[lipinski_hash[scoring_args[0]]]
  except:
    score = -999

  return score

task_hash = {
    'alogp': 'The octanol-water partition coefficient (logP) is a measure of how \
hydrophobic a compound is. A lower logP value indicates that the compound is more \
hydrophilic, while a higher logP value indicates that the compound is more lipophilic. \
In drug design, a logP value between 1 and 3 is often considered optimal for oral \
bioavailability, as it suggests a good balance between solubility and permeability.',
    'mw': 'Molecular weight (MW) is the mass of a molecule. In drug design, a molecular weight \
below 500 Daltons is often considered favorable for oral bioavailability, as it suggests that \
the compound is small enough to be absorbed by the body. However, this is just a general guideline \
and there are many exceptions.',
    'hba': 'The number of hydrogen bond acceptors (HBA) is a measure of how many atoms in a \
molecule can accept hydrogen bonds. In drug design, a lower number of hydrogen bond acceptors \
(typically less than 10) is often considered favorable for oral bioavailability, as it suggests that \
the compound is more likely to be absorbed by the body.',
    'hbd': 'The number of hydrogen bond donors (HBD) is a measure of how many atoms in a \
molecule can donate hydrogen bonds. In drug design, a lower number of hydrogen bond donors \
(typically less than 5) is often considered favorable for oral bioavailability, as it suggests that \
the compound is more likely to be absorbed by the body.',
    'psa': 'Polar surface area (PSA) is a measure of the surface area of a molecule that is \
polar. In drug design, a polar surface area below 140 Å² is often considered favorable for oral \
bioavailability, as it suggests that the compound is more likely to be absorbed by the body.',
    'rb': 'The number of rotatable bonds (RB) is a measure of the flexibility of a molecule. \
In drug design, a lower number of rotatable bonds (typically less than 10) is often considered \
favorable for oral bioavailability, as it suggests that the compound is more likely to be absorbed \
by the body.',
    'ar': 'The number of aromatic rings (AR) is a measure of the presence of aromatic rings in a \
molecule. In drug design, a lower number of aromatic rings (typically less than 5) is often \
considered favorable for oral bioavailability, as it suggests that the compound is more likely \
to be absorbed by the body.',
    'um': 'The number of undesirable substructures (UM) is a measure of the presence of certain \
substructures in a molecule that are often associated with poor drug-like properties. In drug design, \
a lower number of undesirable substructures (typically less than 5) is often considered favorable for \
oral bioavailability.'
}

task_specific_prompt = f'''# You are a drug design assistant. In the first user message you will
see a list of molecular SMILES strings and a specific property calculated for each molecule. 
{task_hash[scoring_args[0]]} Your task is to use the information in the list to learn trends about 
what makes a molecule have a good value for that property, and then use those trends to suggest 
new molecules that should have better values for that property than the ones in the list.'''