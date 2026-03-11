"""
Script to extract SMILES strings from model_replies.md - MAOB section
Organizes them into lists by model name and creates a dictionary
"""

# MAOB SMILES by model

# gpt 5.2
gpt_5p2_maob = [
    "O=c1cc(-c2ccc(C#C(C(F)(F)(F)))c(C#C(C(F)(F)(F)))c2)oc2ccccc12",
    "O=c1cc(-c2ccc(C#C(C(F)(F)(F)))cc2C#N)oc2ccccc12",
    "O=c1cc(-c2ccc(C#C(C(F)(F)(F)))cc2C=C(NC(=O)C))oc2ccccc12",
    "O=c1cc(-c2ccc(C#C(C(F)(F)(F)))cc2CC=C(OC(=O)C))oc2ccccc12",
    "O=c1cc(-c2ccc(C#Cc3ccccc3)cc2C(F)(F)(F))oc2ccccc12"
]

# gpt-oss:120b
gpt_oss_120b_maob = [
    "O=c1c(C=C(NC(=O)C))c(-c2ccc(C(F)(F)F)cc2)oc2ccccc12",
    "O=c1c(C#C(C(F)(F)F))c(-c2ccc(N(C)C)cc2)oc2ccccc12",
    "O=c1c(C=C(C#N))c(-c2ccc(C(=O)NCC)cc2)oc2ccccc12",
    "O=c1c(C#C(N))c(-c2ccc(C(F)(F)F)cc2)oc2ccccc12",
    "O=c1c(C#C(C(F)(F)F))c(-c2c3ccccc3c(c2)C(F)(F)F)oc2ccccc12"
]

# gpt-oss:20b
gpt_oss_20b_maob = [
    "c1c2c3c4ccccc4c3c2c1C=C(NC(=O)C)",
    "c1c2c3c4ccccc4c3c2c1C#C(C(F)(F)(F))",
    "c1c2c3c4ccccc4c3c2c1C=C(NC(=O)C)C(=O)C",
    "c1c2c3c4ccccc4c3c2c1C=C(NC(=O)C)C#C(C(F)(F)(F))",
    "c1c2c3c4ccccc4c3c2c1NC(=O)C"
]

# devstral-2:123b
devstral_2_123b_maob = [
    "c1(C#C(C(F)(F)(F)))ccc2cc3ccccc3cc2c1(C=C(NC(=O)C))",
    "O=c1cc(-c2ccc(CC=C(OC(=O)C))cc2)oc2ccccc12(C=C(CCC(C(C)C)))",
    "c1(C#C(C(F)(F)(F)))ccc2ccccc2c1(C#C(C(F)(F)(F)))",
    "c1(C=C(NC(=O)C))ccc2cc3ccccc3cc2c1(C#C(C(F)(F)(F)))",
    "O=c1cc(-c2cccc(C=C(OC(=O)C))c2)oc2ccccc12"
]

# cogito-2.1:671b
cogito_2p1_671b_maob = [
    "c1ccc2c(C=C(NC(=O)C))c3c(c2c1)ccc4ccccc34",
    "c1ccc2c(C#C(C(F)(F)(F)))c3c(c2c1)ccc4ccccc34",
    "O=c1cc(-c2ccc(C=C(NC(=O)C))cc2)oc2cc(C#C(C(F)(F)(F)))ccc12",
    "c1ccc2c(C=C(NC(=O)CF3))c3c(c2c1)ccc4ccccc34",
    "O=c1cc(-c2ccc(C#C(C(F)(F)(F)))cc2)oc2ccc(C=C(NC(=O)C))cc12"
]

# minimax-m2
minimax_m2_maob = [
    "O=c1cc(-c2ccc(C=C(NC(=O)C))cc2)oc2ccccc12",
    "O=c1cc(-c2ccc(C#C(C(F)(F)(F)))cc2)oc2ccccc12",
    "O=c1cc(-c2ccc(C=C(C(F)(F)(F)))cc2)oc2ccccc12",
    "O=c1cc(-c2ccc(N(C(Cl)(Cl)(Cl)))cc2)oc2ccccc12",
    "O=c1cc(-c2ccc(C=C([N+](=O)[O-]))cc2)oc2ccccc12"
]

# nemotron-3-nano:30b
nemotron_3_nano_30b_maob = [
    "c1ccc2c(C=C(C#N)C(F)(F)(F))c3ccccc23",
    "c1c2ccccc2c(=O)N(C(F)(F)(F))c3ccccc3",
    "c1c2ccccc12C(=O)C#C(C(F)(F)(F))",
    "c1c2ccccc12C(=O)C#C(C(F)(F)(F))a",  # Note: 'a' at end seems like an error in original
    "c1c2ccccc12-C(=O)C#C(C(F)(F)(F))"
]

# gemini-3-flash-preview
gemini_3_flash_preview_maob = [
    "O=C1C=C(C2=CC=C(C#CC(F)(F)F)C=C2)OC3=CC4=CC=CC=C4C=C13",
    "O=C1C=C(C2=CC=C(C=CNC(=O)C)C=C2)OC3=CC4=CC=CC=C4C=C13",
    "O=C1C=C(C2=CC=C(C#CC(F)(F)F)C=C2)OC3=C1C=CC4=CC=CC=C43",
    "O=C1C=C(C2=CC=C(CCC(C)C)C=C2)OC3=CC4=CC=CC=C4C=C13",
    "O=C1C=C(C2=CC=C(C#CC(F)(F)F)C=C2)OC3=CC4=CN=CC=C4C=C13"
]

# Create dictionary with model names as keys and SMILES lists as values
model_smiles_maob_dict = {
    'gpt_5p2': gpt_5p2_maob,
    'gpt_oss_120b': gpt_oss_120b_maob,
    'gpt_oss_20b': gpt_oss_20b_maob,
    'devstral_2_123b': devstral_2_123b_maob,
    'cogito_2p1_671b': cogito_2p1_671b_maob,
    'minimax_m2': minimax_m2_maob,
    'nemotron_3_nano_30b': nemotron_3_nano_30b_maob,
    'gemini_3_flash_preview': gemini_3_flash_preview_maob
}

# Print summary
print("MAOB SMILES Extraction Summary")
print("=" * 60)
print(f"Total models: {len(model_smiles_maob_dict)}")
print(f"Total SMILES: {sum(len(smiles_list) for smiles_list in model_smiles_maob_dict.values())}")
print("\nSMILES count per model:")
for model, smiles_list in model_smiles_maob_dict.items():
    print(f"  {model}: {len(smiles_list)} SMILES")

# Optional: Print all SMILES organized by model
print("\n" + "=" * 60)
print("All SMILES by Model:")
print("=" * 60)
for model, smiles_list in model_smiles_maob_dict.items():
    print(f"\n{model}:")
    for i, smiles in enumerate(smiles_list, 1):
        print(f"  {i}. {smiles}")
