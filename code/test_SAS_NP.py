from rdkit import Chem
from rdkit.Chem import RDConfig
import sys, os
sys.path.append(os.path.join(RDConfig.RDContribDir, 'SA_Score'))
sys.path.append(os.path.join(RDConfig.RDContribDir, 'NP_Score'))
import sascorer, npscorer

# code works on local conda environment, on Colab, and on Github codespace

def calculate_SAS_and_NP(smiles_list: list[str]):
    '''Calculate SAS and NP scores for a list of SMILES strings. SAS score is a measure 
    of synthetic accessibility, and a value of 1 indicates that the molecule is easy to synthesize, 
    while a value of 10 indicates that it is difficult to synthesize. 
    NP score is a measure of natural product-likeness, and a higher score indicates that the 
    molecule is more similar to natural products; the score runs from -5 to 5, with higher scores 
    indicating greater similarity to natural products.

    Args:
        smiles_list (list[str]): A list of SMILES strings representing the molecules to be scored.

    Returns:
        list[tuple[float, float]]: A list of tuples containing the SAS and NP scores for each molecule.
    '''
    fscore = npscorer.readNPModel()

    out_string = '| SMILES | SAS Score | NP Score |\n'
    out_string += '|---------|-----------|----------|\n'
    for smiles in smiles_list:
        mol = Chem.MolFromSmiles(smiles)
        if mol is not None:
            sas_score = sascorer.calculateScore(mol)
            np_score = npscorer.scoreMol(mol, fscore)
            out_string += f'| {smiles} | {sas_score:.2f} | {np_score:.2f} |\n'
        else:
            out_string += f'| {smiles} | {"Invalid SMILES"} | {"Invalid SMILES"} |\n'
    return out_string


smiles_list = ['O=c1cc(-c2c(F)c(C)c(F)cc2)oc2cccc(CC(=O)O)c12', 'O=c1cc(-c2c(F)cc(Cl)cc2)oc2cccc(CC(=O)O)c12']

results = calculate_SAS_and_NP(smiles_list)
print(results)