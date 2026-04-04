from rdkit import Chem
from rdkit.Chem import Draw, QED
from PIL import Image

def scoring_function(smiles: str):
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

one_shot = ['N#CC=CCc1ccc2cccc3ccc1c23',
            'c1cc2ccc3cccc4cccc5cccc(c1)c2c3c45',
            'c1ccc2cc3cc4cc5ccccc5cc4cc3cc2c1'
                   ]

#claude = []
             
gemini3flash = [
        'c1ccc2cc3cc4c(S([NH3+]))c(S([NH3+]))c5c(S([NH3+]))c(S([NH3+]))c6c(S([NH3+]))c(S([NH3+]))c7c([N+](=O)[O-])cc8cc9cc%10ccccc%10cc9cc8cc7cc6cc5cc4cc3cc2c1',
        'c1ccc2cc3cc4cc5cc6c(S([NH3+]))c(S([NH3+]))c7c(S([NH3+]))c(S([NH3+]))c8cc9cc%10cc%11cc%12ccccc%12cc%11cc%10cc9cc8cc7cc6cc5cc4cc3cc2c1'
]

gpt5p2 = [
        'c1(C#CC#N)ccc2c(C#C(C#N))c3c(C#C(C#N))cc(C#CC#N)c(C#CC#N)c3c(C#Cc7ccc8cc9ccccc9cc8c7)c2c1',
        'c1(C#C(C#N))ccc2c(C#C(C#N))c3c(C#C(C#N))cc(C#CC#N)c(C#CC#N)c3c(C#Cc7ccc8cc9ccccc9cc8c7)c2c1',
        'c1([N+](=O)[O-])ccc2c(C#C(C#N))c3c(C#C(C#N))cc(C#CC#N)c(C#CC#N)c3c(C#Cc7ccc8cc9ccccc9cc8c7)c2c1'
]

hash_lists = {
    'one_shot': one_shot,
    #'ANTHROPIC': claude,
    'OPENAI': gpt5p2,
    'GEMINI': gemini3flash
}

all_imgs = []
for name, smiles_list in hash_lists.items():
    alogp_list = []
    qed_list = []
    mols = []
    for smile in smiles_list:
        qed, alogp, mol = scoring_function(smile)
        alogp_list.append(alogp)
        qed_list.append(qed)
        mols.append(mol)
    legs = [f'{name} {i+1}: QED={q:.2f}, logP={a:.2f}' for i, (q, a) in enumerate(zip(qed_list, alogp_list))]
    img = Draw.MolsToGridImage(mols, legends=legs, molsPerRow=2, subImgSize=(400, 400))
    all_imgs.append(img)
    print(f'Finished processing {name}')

for name, img in zip(hash_lists.keys(), all_imgs):
    print(f'Saving image for {name}')
    filename = f"../results/HL/finalist_images/{name}_finalists.png"
    img.save(filename)