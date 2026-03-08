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