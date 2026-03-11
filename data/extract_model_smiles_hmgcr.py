"""
Script to extract SMILES strings from model_replies.md - HMGCR section
Organizes them into lists by model name and creates a dictionary
"""

# HMGCR SMILES by model

# gpt 5.2
gpt_5p2_hmgcr = [
    "O=c1cc(-c2ccccc2)oc2cccc(N(C(=O))C(=O)C)c12",
    "O=c1cc(-c2ccccc2)oc2cccc(N(S(=O)(=O)C))c12",
    "O=c1cc(-c2ccccc2)oc2cccc(N(S(=O)(=O)c3ccccc3))c12",
    "O=c1cc(-c2ccccc2)oc2cccc(C#C(C(=O)[O-]))c12",
    "O=c1cc(-c2ccccc2)oc2cccc(N(C(=O))C#N)c12"
]

# gpt 5.2 tool call 1
gpt_5p2_tools_first_hmgcr = [
    "O=c1cc(-c2ccc(NC(=O)C)cc2)oc2cccc(N(C(=O)))c12",
    "O=c1cc(-c2ccc(C(=O)O)cc2)oc2cccc(N(C(=O)))c12",
    "O=c1cc(-c2ccc(C(=O)[O-])cc2)oc2cccc(N(C(=O)))c12",
    "O=c1cc(-c2ccc(C(F)(F)(F))cc2)oc2cccc(N(C(=O)))c12",
    "O=c1cc(-c2ccc(F)cc2)oc2cccc(N(C(=O)))c12"
]

# gpt 5.2 tool call 2
gpt_5p2_tools_second_hmgcr = [
    "O=c1cc(-c2cc(Cl)c(NC(=O)C)cc2)oc2cccc(N(C(=O)))c12",
    "O=c1cc(-c2ccc(NC(=O)C)c(Cl)c2)oc2cccc(N(C(=O)))c12",
    "O=c1cc(-c2c(F)cc(NC(=O)C)cc2)oc2cccc(N(C(=O)))c12",
    "O=c1cc(-c2cc(F)c(NC(=O)C)cc2)oc2cccc(N(C(=O)))c12",
    "O=c1cc(-c2ccc(NC(=O)C)cc2)oc2ccc(F)c(N(C(=O)))c12"
]

# deepseek-v3.1:671b
deepseek_v3p1_671b_hmgcr = [
    "O=c1cc(-c2cccc(N(C(=O)))c2)oc2ccccc12",
    "O=c1cc(-c2cc(N(N))cc(N(N))c2)oc2ccccc12",
    "O=c1cc(-c2ccc(C#CC(N(C(=O))))cc2)oc2ccccc12",
    "O=c1cc(-c2cc(N(N))c(C=C(F))cc2)oc2ccccc12",
    "O=c1cc(-c2cccc(C#C([O-]))c2)oc2cccc(N(C(=O)))c12"
]

# gpt-oss:120b
gpt_oss_120b_hmgcr = [
    "O=c1c(C#C(C))c(-c2ccc(C(F)(F)F)cc2)oc2cccc(NC(=O)c3ccccc3)c12",
    "O=c1c(C#C(C))c(-c2ccc(S(=O)(=O)NH2)cc2)oc2cccc(NC(=O)c3ccccc3)c12",
    "O=c1c(C#C(C))c(-c2ccc(C(F)(F)F)cc2)oc2cccc(NC(=O)c3ccc(C(=O)N)cc3)c12",
    "O=c1c(C#C(C))c(-c2c3ccccc3c4ccccc4c2)oc2cccc(NC(=O)c5ccccc5)c12",
    "O=c1c(C#C(C))c(-c2ccc(C(F)(F)F)cc2)oc2cccc(S(=O)(=O)NH2)c12"
]

# gpt-oss:20b
gpt_oss_20b_hmgcr = [
    "O=C(Nc1ccccc1)c1ccccc1C#C(C)",
    "O=C(Nc1ccc(C#N)cc1)c1ccccc1",
    "O=c1c(-c2ccccc2)oc2c(c1)ncc3ccccc3c2",
    "c1c(C#C(C))ccc2c1c(=O)ncc3ccccc3c2",
    "O=c1c(-c2ccc(C#N)cc2)oc2c(C(C)C)ncc3ccccc3c2"
]

# devstral-2:123b
devstral_2_123b_hmgcr = [
    "O=c1cc(-c2cccc(N(N))c2)oc2cc(N(C=O))ccc12",
    "O=c1cc(-c2cccc(C#C([O-]))c2)oc2cc(C=C(F))ccc12",
    "O=c1cc(-c2cccc(CC=C(C#N))c2)oc2cc(N(C=O))ccc12",
    "O=c1cc(-c2cc3ccccc3cc2c2cccc(N(N))c2)oc2ccccc12",
    "O=c1cc(-c2cccc(C#C(NC))c2)oc2cc(N(C=O))ccc12"
]

# cogito-2.1:671b
cogito_2p1_671b_hmgcr = [
    "O=c1cc(-c2cccc(N(N))c2)oc2cccc(N(C(=O)))c12",
    "O=c1cc(-c2cccc(CC=C(C#N))c2)oc2cccc(N(C(=O)))c12",
    "O=c1cc(-c2ccc(N(N))cc2)oc2cccc(C#C(NC))c12",
    "O=c1cc(-c2cccc(C#C([O-]))c2)oc2cccc(N(C(=O)))c12",
    "O=c1cc(-c2cccc(C=C(F))c2)oc2cccc(N(N))c12"
]

# minimax-m2
minimax_m2_hmgcr = [
    "O=c1cc(-c2cc(N(N))ccc2)oc2ccccc12",
    "O=c1cc(-c2ccc(N(C(=O)))cc2)oc2ccccc12",
    "O=c1cc(-c2cc(C#C([O-]))ccc2)oc2ccccc12",
    "O=c1cc(-c2ccc(N(C(=O)))cc2)oc2ccccc12",
    "n1c[nH]c(C#C([O-]))c2cc3ccccc3cc2c1"
]

# nemotron-3-nano:30b
nemotron_3_nano_30b_hmgcr = [
    "c1ccc2c(c1)C#CC#N",
    "c1ccc2c(c1)C#C(C#N)",
    "c1c2cc3ccccc3c2c(C#C(NC(=O)))c1",
    "c1cc2c3ccccc3c2c1C#C(NC(=O))C#N",
    "o1c2c3ccccc3c2c1C#C(C#N)"
]

# gemini-3-flash-preview
gemini_3_flash_preview_hmgcr = [
    "O=c1cc(-c2ccc(F)cc2)oc2cccc(N(C(=O)))c12",
    "O=c1cc(-c2ccc(N(N))cc2)oc2cccc(N(C(=O)))c12",
    "O=c1cc(-c2cccc(CC=C(C#N))c2)oc2cccc(N(C(=O)))c12",
    "O=c1cc(-c2ccc(N(C(=O)))cc2)oc2cccc(N(C(=O)))c12",
    "O=c1cc(-c2ccc(N(N))cc2)oc2cccc(C=C(F))c12"
]

# Create dictionary with model names as keys and SMILES lists as values
model_smiles_hmgcr_dict = {
    'gpt_5p2': gpt_5p2_hmgcr,
    'gpt_5p2_tools_first': gpt_5p2_tools_first_hmgcr,
    'gpt_5p2_tools_second': gpt_5p2_tools_second_hmgcr,
    'deepseek_v3p1_671b': deepseek_v3p1_671b_hmgcr,
    'gpt_oss_120b': gpt_oss_120b_hmgcr,
    'gpt_oss_20b': gpt_oss_20b_hmgcr,
    'devstral_2_123b': devstral_2_123b_hmgcr,
    'cogito_2p1_671b': cogito_2p1_671b_hmgcr,
    'minimax_m2': minimax_m2_hmgcr,
    'nemotron_3_nano_30b': nemotron_3_nano_30b_hmgcr,
    'gemini_3_flash_preview': gemini_3_flash_preview_hmgcr
}

# Print summary
print("HMGCR SMILES Extraction Summary")
print("=" * 70)
print(f"Total models: {len(model_smiles_hmgcr_dict)}")
print(f"Total SMILES: {sum(len(smiles_list) for smiles_list in model_smiles_hmgcr_dict.values())}")
print("\nSMILES count per model:")
for model, smiles_list in model_smiles_hmgcr_dict.items():
    print(f"  {model}: {len(smiles_list)} SMILES")

# Optional: Print all SMILES organized by model
print("\n" + "=" * 70)
print("All SMILES by Model:")
print("=" * 70)
for model, smiles_list in model_smiles_hmgcr_dict.items():
    print(f"\n{model}:")
    for i, smiles in enumerate(smiles_list, 1):
        print(f"  {i}. {smiles}")
