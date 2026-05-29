import os
from rdkit import Chem  

print('hello world')
mol = Chem.MolFromSmiles('CCO')
print(mol)