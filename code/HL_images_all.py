from rdkit import Chem
from rdkit.Chem import Draw, QED
from PIL import Image

print("Starting to process SMILES and generate images...")

zero_openai_smiles = [
    "CN(C)c1ccc(/C=C/C(=C(C#N)C#N))cc1",
    "CN(C)c1ccc(/C=C/C=C/C(=C(C#N)C#N))cc1",
    "CN(C)c1ccc(/C=C/C(=C(C#N)C#N)C#N)cc1",
    "CN(C)c1ccc(-c2nc3ccccc3s2)cc1",
    "N#CC(=C(C#N)C#N)C#N",
]

# Anthropic
zero_anthropic_smiles = [
    "C1=CC=C2C(=C1)C=CC3=CC=CC4=CC=CC(=C3C2=C4)C5=CC=CC6=CC=CC=C6C5",
    "C1=C(S1)C2=C(SC(=C2)S3CCCS3)S4CCCS4",
    "C1=CC(=CC=C1C2=CC=CC(=C2)C3=CC=CC(=C3)C4=CC=CC(=C4)C5=CC=CC=C5)C6=CC=CC=C6",
    "C1=CSC(=C1)C2=CC=CC(=C2)C3=CC=CS3",
    "C1=CC2=C(C=C1)C=CC3=CC=CC4=CC=CC5=CC=CC6=CC=CC7=CC=CC(=C7C(=C6C(=C5C(=C4C(=C3C=C2)C=C)C=C)C=C)C=C)C=C",
]

# deepseek-v3.1:671b
zero_deepseek_v3_smiles = [
    "c1ccc2cc3cc4cc5cc6cc7ccccc7cc6cc5cc4cc3cc2c1",
    "N#Cc1ccc(C(C#N)(C#N)C#N)cc1",
    "c1cnccc1-c1ccc(s1)/C=C/c1sc(c2ccncc2)cc1",
    "c1cc2nc3ccccc3nc2n1-c1nc2ccccc2n1",
    "c1cc2ccc3ccc4ccc5ccc1c2c3c4c5",
]

# gpt-oss:120b
zero_gpt_oss_120b_smiles = [
    "CN(C)C1=CC=C(C=C1)C2=CN3C(=O)C4=CC=CC=C4C5=CC=CC=C5C(=O)N3C2",
    "C1=CC2=C(C=C1)SC=S2C3=CN=C(N=C3)C4=CC=CC=C4",
    "C1=CC2=C(C=C1)C3=CC4=C(C=C3C5=CC=CC=C5)C(=O)N(C6=CC=CC=C6)C(=O)C4=C2",
    "C1=SC=CS1C2=SC=CS2",
    "O=C1C2=CC=CC3=CC=CC4=CC=CC5=CC=CC6=CC=CC=1N2N6C3C5",
]

# gpt-oss:20b
zero_gpt_oss_20b_smiles = [
    "C60",
    "C70",
    "CCCCCC=CC=CC=CC=CC=C",
    "C1=CC2=CC3=CC4=CC5=CC=CC6=CC=C1C2C3C4C5C6",
    "O=[N+]c1ccc(cc1)N(=O)=O-C1=CC2=CC3=CC=CC=C3CC4=CC=CC4C=C2C=C1",
]

# devstral-2:123b
zero_devstral_2_smiles = [
    "C1=C(C=S1)C2=C(C=S2)C3=C(C=S3)C4=C(C=S4)",
    "N#C-C(C#N)=C1C=C(C#N)C(C#N)=C1C#N",
    "C1=CC=C2C=C3C=CC=C4C=C5C=CC=CC5=C4C=C3C=C21",
    "C1=CC=C2C=C3C=CC=C4C=C5C=CC=CC5=C4C=C3C=C21",
    "C1=CC=C2C=C3C=CC=C4C=C5C=CC=CC5=C4C=C3C=C21",
]

# cogito-2.1:671b
zero_cogito_2_smiles = [
    "C1=CC=C2C(=C1)C=CC=C2",
    "C1=CC2=C3C(=C1)C=CC4=CC=CC(=C43)C=C2",
    "C1=CC=C2C(=C1)C3=CC=CC4=CC=CC(=C43)C=C2",
    "C1=CC2=CC3=CC=C(N)C=C3C=C2C=C1",
    "C1=CC2=C(C=CC3=CC4=C(C=CC=C4)C=C32)C=C1",
]

# nemotron-3-nano:30b
zero_nemotron_3_nano_smiles = [
]

# gemini-3-flash-preview
zero_gemini_3_flash_preview_smiles = [
    "c1ccc2cc3cc4cc5cc6cc7ccccc7cc6cc5cc4cc3cc2c1",
    "Fc1c(F)cc2c(c1)c3c(s2)c4c(nsn4)c5c(s3)c6cc(F)c(F)cc6n5",
    "c1cc(sc1)-c2c3nsnc3c(c4sccc4)c5nsnc25",
    "O=C1C(=C2C=CC(=[N+](C)C)C=C2)C(=O)C(=C3C=CC(=[N+](C)C)C=C3)C1=O",
    "N#CC(C#N)=C1C=CC(=C2C=CC(=C3C=CC(=C4C=CC(=C(C#N)C#N)S4)S3)S2)S1",
]

# kimi-k2:1t
zero_kimi_k2_smiles = [
    "C=C=C=C=C=C=C=C",
    "C=C=C=C=C=C=C=C=C=C",
    "S=C=C=C=C=S",
    "c1cc2cc3cc4cc5cc6cc7cc8cc9cc1c2c3c4c5c6c7c89",
    "C1=C2C(=C(C(=C(C1=S)S)S)S)C2=S",
]

# OpenAI
frag_openai_smiles = [
    "c1ccc2cc3cc(/C=C(C#N))ccc3cc2c1/C=C(C#N)",
    "c1ccc2cc3cc(/C=C(OC))ccc3cc2c1/C=C(OC)",
    "c1ccc2cc3cc(/C=C(OC))ccc3cc2c1/C=C(C#N)",
    "O=c1cc(-c2ccc(/C=C(C#N))cc2)oc2ccccc12",
    "O=c1cc(-c2cc(OC)cc(/C=C(C#N))c2)oc2ccccc12",
]

# Anthropic
frag_anthropic_smiles = [
    "OCc1ccc2ccccc2c1C=CC#N",
    "C#C(OC(=O)C)c1ccc2cc3ccccc3cc2c1OC",
    "C=CC(C#N)c1ccc2ccccc2c1N(C(Cl)(Cl)Cl)",
    "C=CC(OC)c1ccc2ccccc2c1C=CC#N",
    "OCc1ccc2cc3ccccc3cc2c1C=CC#N",
]

# deepseek-v3.1:671b
frag_deepseek_v3_smiles = [
    "O=C(C#C)c1ccc2ccccc2c1N(C(Cl)(Cl)Cl)",
    "c1ccc2cc3ccccc3cc2c1C=CC(OC)",
    "O=c1cc(-c2ccc(S([NH3+]))cc2)oc2ccccc12",
    "O=C(O)O[nH]1cccc1C#C(OC(=O)C)",
    "s1ccc(C#C)c1C#Cc1c[nH]cc1C=CC(C#N)",
]

# gpt-oss:120b
frag_gpt_oss_120b_smiles = [
    "CN(C)c1ccc2ccccc2c1C#N",
    "CN(C)c1ccc2c3ccccc3c(c2c1)C#N",
    "CN(C)c1ccc(cc1)c1c2ccccc2oc2ccccc12C#N",
    "CN(C)c1ccc2sccc2c1C#N",
    "CN(C)c1ccc2c(c1)nc[nH]2C#N",
]

# gpt-oss:20b
frag_gpt_oss_20b_smiles = [
    "c1ccc2cc3ccccc3cc2c1C#N",
    "c1ccc2ccccc2c1C#N",
    "O=c1cc(-c2ccccc2C#N)oc2ccccc12C#N",
    "c1ccccc1C#Cc2ccccc2C#N",
    "c1ccc2cc3ccccc3cc2c1C#C(OC(=O)C)",
]

# devstral-2:123b
frag_devstral_2_smiles = [
    "c1ccc2cc3ccccc3cc2c1C=C(C#N)C=C(OC)C=C(C#N)",
    "O=c1cc(-c2ccccc2)oc2ccccc12C(=O)O(O)",
    "s1cccc1C=C(C#N)s1cccc1C=C(OC)s1cccc1",
    "c1ccc2ccccc2c1C(=O)N(Cl)C=C(N(C(Cl)(Cl)Cl))",
    "[nH]1cccc1C=C(C#N)[nH]1cccc1C=C(OC)[nH]1cccc1",
]

# cogito-2.1:671b
frag_cogito_2_smiles = [
    "CN(C)c1ccc2cc(ccc2c1)[N+](=O)[O-]",
    "Nc1ccc2cc3cc(ccc3c2c1)[N+](=O)[O-]",
    "O=C1c2ccccc2OC2=C1C=CC(=C2)[N+](=O)[O-]",
    "s1ccc(-c2ccc[nH]2)c1[N+](=O)[O-]",
    "O=C1C=CC(=O)C2=C1N=C([N+](=O)[O-])N2",
]

# nemotron-3-nano:30b
frag_nemotron_3_nano_smiles = [
    "c1ccc2ccccc2c1c(ccc(cc2)N(=O)=O)C=CC(CC)O",
    "c1ccc2ccccc2c1c(ccc(cc2)C#N)C=CC(CC)O",
    "N#CC(=O)C=C(c1ccc2ccccc2c1)C=CC(C(=O)N(C(Cl)(Cl)(Cl))C(Cl)(Cl)Cl))C(=O)C=O",
    "O=C1c2cc(-c3ccccc3)ccc2c1c4ccccc4",
    "N1C[NH3+]=n2c3ccccc3c2cc4ccccc4c1",
]

# gemini-3-flash-preview
frag_gemini_3_flash_preview_smiles = [
    "N#Cc1c2ccccc2c(N(C)C)c3ccccc13",
    "N#Cc1sc(cc1)-c2sc(N(C)C)cc2",
    "CN(C)c1ccc(cc1)-c2cc(=O)c3ccccc3o2",
    "N#CC=Cc1c2ccccc2c(C=CC#N)c3ccccc13",
    "CN(C)c1sc(cc1)-c2c3ccccc3c(c4sc(N(C)C)cc4)c5ccccc25",
]

# kimi-k2.5
frag_kimi_k2_smiles = [
    "COc1c2ccccc2c(/C=C/C#N)c2ccccc12",
    "N#CC=Cc1c2ccccc2c(/C=C/C#N)c2ccccc12",
    "COc1ccc(/C=C/c2cc(-c3ccccc3)oc3ccccc23)cc1",
    "N#CC=Cc1ccc(/C=C/OC)s1",
    "N#CC=Cc1c(/C=C/c2ccccc2OC)[nH]cn1",
]

one_deepseek_v3_1_671b_smiles = [
    "O=c1c2ccccc2c(S([NH3+]))c3ccccc3c1=O",
    "O=c1c2ccc(S([NH3+]))cc2c(C#N)c3ccccc3c1=O",
    "O=c1c2ccccc2c(OC)c3ccc(C(=O)O(O))cc3c1=O",
    "n1c2ccccc2c(C(=O)O(O))c3ccccc3c1=O",
    "O=c1c2cccc(S([NH3+]))c2c(C#N)c3cccc(C#N)c3c1=O",
]

one_gpt_oss_120b_smiles = [
    "S([NH3+])c1ccc2c(c1)ccc3c2ccc3",
    "S([NH3+])c1ccc2c(c1)ccc3c2ccc3C#N",
    "COc1ccc2c(c1)ccc3c2ccc3S([NH3+])",
    "S([NH3+])c1c(S([NH3+]))c2ccc3ccccc3c2c1",
    "S([NH3+])c1ccc2c(c1)ccc3c2ccc3[N+](=O)[O-]",
]

one_gpt_oss_20b_smiles = [
    "c1ccc2ccccc2c3ccccc3c1",
    "c1c2ccccc2c3ccccc3c1",
    "c1c2ccccc2c3ccccc13",
    "n1c2ccccc2c3ccccc3c1",
    "c1c2c3ccccc3c4ccccc4c2c1",
]

one_devstral_2_123b_smiles = [
    "c1ccc2cc3ccccc3cc2c1(C(=O)N(Cl))",
    "n1ccc2cc3ccccc3cc2c1(C(=O)O(O))",
    "c1ccc2cc3ccccc3cc2c1(C#N)",
    "o1ccc2cc3ccccc3cc2c1(C(=O)N(Cl))",
    "c1ccc2cc3ccccc3cc2c1(C(=O)N(Cl))(C#N)",
]

one_cogito_2_1_671b_smiles = [
    "c1cc2c3c4cc(C(=O)O(O))ccc4ccc3ccc2c1",
    "O=C(O)c1ccc2c3c1c1c4c(c3ccc2)ccc(C(=O)N(Cl))c4c1",
    "s1ccc2sc3c4c(cc3c2c1)ccc(C(=O)O(O))c4",
    "c1cc2c3c4c5c6c1c1c7c(c6cc5cc4cc3cc2)ccc(C(=O)N(Cl))c7c1",
    "O=C(O)c1ccc2sc3c(c2c1)ccc(C(=O)N(Cl))c3",
]

one_nemotron_3_nano_30b_smiles = [
    "c1ccc(S(=O)(=O)[NH3+])c2ccccc2",
    "c1c(S([NH3+]))cccc1",
    "n1c(S([NH3+]))c2ccccc2",
    "[NH3+]S(=O)(=O)c1ccc2ccccc2",
    "c1c(S([NH3+]))c2cc(ccc2)[N+](=O)[O-]",
]

one_gemini_3_flash_preview_smiles = [
    "CC(=O)OC#Cc1ccc2cc3cc4ccccc4cc3cc2c1",
    "[NH3+]S(c1c2ccccc2c(S([NH3+]))c3ccccc13)",
    "O=c1cc(-c2ccc3ccccc3c2)oc2cc(S([NH3+]))ccc12",
    "c1ccc2cc3cc4cc5ccccc5cc4cc3cc2c1",
    "N#CC=Cc1ccc(-c2c3ccccc3cc4ccccc24)cc1",
]

one_kimi_k2_1t_smiles = [
    "c1(S([NH3+]))ccc2cc3ccccc3cc2c1",
    "c1cc(S([NH3+]))c2cc3ccccc3cc2c1",
    "c1ccc2c(S([NH3+]))c3ccccc3cc2c1",
    "O=c1c(S([NH3+]))c(-c2ccccc2)oc2ccccc12",
    "O=c1cc(-c2ccc(S([NH3+]))cc2)oc2ccccc12",
]

one_gpt5p2_smiles = [
    "CC(=O)OcC#Cc1ccc2cccc3ccc1c23",
    "CC(=O)OcC#Cc1cccc2cccc3cccc4cccc1c234",
    "CC(=O)OcC#Cc1ccc2cccc3cccc4ccc1c2c34",
    "N#CC=CCc1ccc2cccc3ccc1c23",
    "CC(=O)OcC#Cc1ccc2cccc3cccc4ccc(C#Cc5oc(=O)ccccc5)c1c2c34",
]

one_claude_smiles = [
    "c1cc2ccc3cccc4cccc(c1)c2c34",
    "c1cc2ccc3cccc4cccc(OC)c(c1)c2c34",
    "c1cc2ccc3cccc4cccc5cccc(c1)c2c3c45",
    "c1ccc2c(C=CC=CC#N)cccc2c1",
    "C1=Cc2ccc3ccccc3c2C1",
]

adv_gemini_smiles = [
        'c1ccc2cc3cc4c(S([NH3+]))c(S([NH3+]))c5c(S([NH3+]))c(S([NH3+]))c6c(S([NH3+]))c(S([NH3+]))c7c([N+](=O)[O-])cc8cc9cc%10ccccc%10cc9cc8cc7cc6cc5cc4cc3cc2c1',
        'c1ccc2cc3cc4cc5cc6c(S([NH3+]))c(S([NH3+]))c7c(S([NH3+]))c(S([NH3+]))c8cc9cc%10cc%11cc%12ccccc%12cc%11cc%10cc9cc8cc7cc6cc5cc4cc3cc2c1',
        'c1ccc2cc3c(S([NH3+]))c(S([NH3+]))c4c(S([NH3+]))c(S([NH3+]))c5c(S([NH3+]))c(S([NH3+]))c6cc7cc8ccccc8cc7cc6cc5cc4cc3cc2c1'
]



adv_gpt_smiles = [
        'c1(C#CC#N)ccc2c(C#C(C#N))c3c(C#C(C#N))cc(C#CC#N)c(C#CC#N)c3c(C#Cc7ccc8cc9ccccc9cc8c7)c2c1',
        'c1(C#C(C#N))ccc2c(C#C(C#N))c3c(C#C(C#N))cc(C#CC#N)c(C#CC#N)c3c(C#Cc7ccc8cc9ccccc9cc8c7)c2c1',
        'c1([N+](=O)[O-])ccc2c(C#C(C#N))c3c(C#C(C#N))cc(C#CC#N)c(C#CC#N)c3c(C#Cc7ccc8cc9ccccc9cc8c7)c2c1'
]

adv_ant_smiles = [
        'c1(OC)c(N(C)c1c(N(C(C)C)C)c(C#N)c(C(=O)C#N)cc1)cc2cc(C(=O)C(C#N)(C#N))ccc2c1',
        'c1(OC)c(N(C)c1cc(C#N)c(C(=O)C#N)cc1)cc2cc(C(=O)C(C#N)(C#N))cc(N(C(C)C)C)c2c1',
        'c1(OC)c(N(C)c1cc(C#N)c(C(=O)C#N)cc1)cc2cc(C(=O)C(C#N)(C#N))cc(OC)c2c1'
]

adv_corrected_ant_smiles = [
        'c1(OC)c(N(C)c6c(N(C(C)C)C)c(C#N)c(C(=O)C#N)cc6)cc2cc(C(=O)C(C#N)(C#N))ccc2c1',
        'c1(OC)c(N(C)c6cc(C#N)c(C(=O)C#N)cc6)cc2cc(C(=O)C(C#N)(C#N))cc(N(C(C)C)C)c2c1',
        'c1(OC)c(N(C)c6cc(C#N)c(C(=O)C#N)cc6)cc2cc(C(=O)C(C#N)(C#N))cc(OC)c2c1'
]


# add frags, ones, adversary

hash_lists = {
    "zero_GPT5p2": zero_openai_smiles,
    "zero_Claude": zero_anthropic_smiles,
    "zero_Deepseek": zero_deepseek_v3_smiles,
    "zero_GPT_OSS120": zero_gpt_oss_120b_smiles,
    "zero_GPT_OSS20": zero_gpt_oss_20b_smiles,
    "zero_Devstral": zero_devstral_2_smiles,
    "zero_Cogito": zero_cogito_2_smiles,
    "zero_Nemotron": zero_nemotron_3_nano_smiles,
    "zero_Gemini": zero_gemini_3_flash_preview_smiles,
    "zero_Kimi_k2": zero_kimi_k2_smiles,
    "frag_GPT5p2": frag_openai_smiles,
    "frag_Claude": frag_anthropic_smiles,
    "frag_Deepseek": frag_deepseek_v3_smiles,
    "frag_GPT_OSS120": frag_gpt_oss_120b_smiles,
    "frag_GPT_OSS20": frag_gpt_oss_20b_smiles,
    "frag_Devstral": frag_devstral_2_smiles,
    "frag_Cogito": frag_cogito_2_smiles,
    "frag_Nemotron": frag_nemotron_3_nano_smiles,
    "frag_Gemini": frag_gemini_3_flash_preview_smiles,
    "frag_Kimi_k2": frag_kimi_k2_smiles,
    "one_Deepseek": one_deepseek_v3_1_671b_smiles,
    "one_GPT_OSS120": one_gpt_oss_120b_smiles,
    "one_GPT_OSS20": one_gpt_oss_20b_smiles,
    "one_Devstral": one_devstral_2_123b_smiles,
    "one_Cogito": one_cogito_2_1_671b_smiles,
    "one_Nemotron": one_nemotron_3_nano_30b_smiles,
    "one_Gemini": one_gemini_3_flash_preview_smiles,
    "one_Kimi_k2": one_kimi_k2_1t_smiles,
    "one_GPT5p2": one_gpt5p2_smiles,
    "one_Claude": one_claude_smiles,
    "adversarial_Gemini": adv_gemini_smiles,
    "adversarial_GPT5p2": adv_gpt_smiles,
    "adversarial_Claude": adv_ant_smiles,
    "adversarial_Corrected_Claude": adv_corrected_ant_smiles
}

all_imgs = []
all_names = []
for name, smiles_list in hash_lists.items():
    mols = []
    for smile in smiles_list:
        try:
            mol = Chem.MolFromSmiles(smile)
            mols.append(mol)
        except:
            print(f'Could not parse SMILES: {smile}')
    legs = [f'{name} {i+1}' for i, smile in enumerate(smiles_list)]
    if len(mols) == 0:
        print(f'No valid SMILES for {name}, skipping image generation.')
    else:
        img = Draw.MolsToGridImage(mols, legends=legs, molsPerRow=2, subImgSize=(400, 400))
        all_imgs.append(img)
        all_names.append(name)
    print(f'Finished processing {name}')

for name, img in zip(all_names, all_imgs):
    print(f'Saving image for {name}')
    filename = f"../results/HL/HL_all_images/{name}_finalists.png"
    img.save(filename)