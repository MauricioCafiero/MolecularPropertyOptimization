from dockstring import load_target
import os

scoring_args = [os.cpu_count(),'DRD2']

def scoring_function(smiles: str):
  '''
    docks a molecule to the target and returns the docking score. If the docking fails, returns 0.0.
  '''
  target = load_target(scoring_args[1])
  try:
    score, aux = target.dock(smiles, scoring_args[0])
  except:
    score = 0.0
    aux = None
  return score, aux

task_specific_prompt = '''# You are a drug design assistant. In the first user message you will
see a list of molecule SMILES strings and docking scores.
The lower the docking score (the more negative), the more affinity the
molecule has for the protein in question. Your task is to use the information 
in the list to learn trends about what makes a molecule a good binder, and then 
use those trends to suggest new molecules that should have better docking scores 
(more negative) than the ones in the list.'''