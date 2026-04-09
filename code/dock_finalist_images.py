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

## order openai, anthropic, gemini for zero and one shots

zero_shot = ['CC(C)C[C@H](O)C[C@H](O)CCC(=O)O-c1ccc(cc1)C2(c3ccccc3)Cc4ccccc42',
             'c1c(C(O)CC(O)C(=O)O)c(cc(n1)C(C)C)C(=O)Nc1ccccc1C(C)C',
             'CC(C)n1c(C2=CC=C(F)C=C2)c(C2=CC3=CC=CC=C3C=C2)c(\C=C\[C@H](O)C[C@H](O)CC(=O)O)c1']

zero_shot_frags = ['O=C(O)Cc1cccc(n1)c2ccc3ccccc3c2',
                   'CC(C)C[C@H](O)[C@H](C)C(=O)Oc1ccc2ccccc2c1-c1ccccc1C(=O)O',
                   'OC(=O)C[C@H](O)C[C@H](O)/C=C/c1c(-c2ccc(F)cc2)c2ccccc2nc1C(C)C']

one_shot = [
                   'O=c1cc(-c2ccc(C=C([N+](=O)[O-]))cc2)oc2cccc(C(C(=O)[O-]))c12',
                   'O=c1cc(-c2cc3ccccc3cc2C(=O)[O-])oc2c(C(C(=O)[O-]))ccc(C(=O)[O-])c12',
                   '[O-]C(=O)Cc1cccc2oc(cc(=O)c12)-c3ccc4ccccc4c3']

claude = ['O=c1c(O)c(-c2c(C)cc(C(=O)N)cc2)oc2c(F)ccc(C(=O)N)c12',
              'O=c1c(O)c(-c2c(C)cc(C(=O)N(C)C)cc2)oc2c(F)ccc(C(=O)N)c12',
              'O=c1c(O)c(-c2c(C)cc(C(=O)N(C)C)cc2)oc2c(F)ccc(C(=O)N(C)C)c12',
              'O=c1c(O)c(-c2c(C(=O)[O-])c(NC(=O)C)ccc2)oc2c(C(F)(F)(F))ccc(C(=O)N)c12',
              'O=c1c(O)c(-c2c(C(=O)[O-])c(NC(=O)C)c(F)cc2)oc2cc(F)cc(C)c12']
             
gpt5p2 = ['O=c1c(O)c(-c2ccc(CC(C)(C)C)cc2)oc2cccc(C(C(=O)O))c12',
                 'O=c1c(O)c(-c2ccc(OC(F)(F)(F))cc2)oc2cccc(C(C(=O)O))c12']

gemini3flash = ['O=c1cc(-c2cc(F)c(F)cc2)oc2cc(F)cc(CC(=O)[O-])c12',
              'O=c1cc(-c2c(OC)c(F)c(F)cc2)oc2cc(F)cc(CC(=O)[O-])c12',
              'O=c1cc(-c2ccc(F)cc2)oc2cc(F)cc(CC(=O)[O-])c12',
              'O=c1cc(-c2c(F)cc(F)cc2)oc2cc(F)cc(CC(=O)[O-])c12',
              'O=c1cc(-c2cc(F)c(F)cc2)oc2cccc(CC(=O)[O-])c12']

hash_lists = {
    'ZERO_SHOT': zero_shot,
    'ZERO_SHOT_FRAGMENTS': zero_shot_frags,
    'ONE_SHOT': one_shot,
    'ANTHROPIC': claude,
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
    img = Draw.MolsToGridImage(mols, legends=legs, molsPerRow=3)
    all_imgs.append(img)
    print(f'Finished processing {name}')

for name, img in zip(hash_lists.keys(), all_imgs):
    print(f'Saving image for {name}')
    filename = f"../results/dock_finalist_images/{name}_finalists.png"
    img.save(filename)