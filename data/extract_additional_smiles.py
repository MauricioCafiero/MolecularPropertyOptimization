"""
Script to extract SMILES strings from additional sections:
1. deepseek-v3.1:671b from model_replies.md (MAOB section)
2. gpt_5p2_tools_first from tool_replies.md (first tool call)
3. gpt_5p2_tools_second from tool_replies.md (second tool call)
"""

# deepseek-v3.1:671b from model_replies.md MAOB section
deepseek_v3p1_671b_maob = [
    "O=c1cc(-c2ccc(C=C(NC(=O)C))cc2)oc2cccc(C#C(C(F)(F)(F)))c12",
    "c1(C=C(NC(=O)C))ccc2c(C#C(C(F)(F)(F)))c3ccccc3cc2c1",
    "O=c1cc(-c2ccc(C=C(NC(=O)C))cc2)oc2ccc(C=C(NC(=O)C))cc12",
    "c1ccc2c(C=C(NC(=O)C))c3c(C#C(C(F)(F)(F)))ccccc3cc2c1",
    "O=c1cc(-c2ccc(C=C(NC(=O)C))cc2)oc2cccc(C=C(NC(=O)C))c12"
]

# gpt_5p2_tools from tool_replies.md - first tool call
gpt_5p2_tools_first = [
    "O=c1cc(-c2cc(C(F)(F)(F))c(C#C(C(F)(F)(F)))cc2)oc2ccccc12",
    "O=c1cc(-c2cc(C#C)c(C#C(C(F)(F)(F)))cc2)oc2ccccc12",
    "O=c1cc(-c2cc(F)c(C#C(C(F)(F)(F)))cc2)oc2ccccc12",
    "O=c1cc(-c2cc(Cl)c(C#C(C(F)(F)(F)))cc2)oc2ccccc12",
    "O=c1cc(-c2c(F)cc(C#C(C(F)(F)(F)))cc2)oc2ccccc12"
]

# gpt_5p2_tools from tool_replies.md - second tool call
gpt_5p2_tools_second = [
    "O=c1cc(-c2cc(C(F)(F)(F))c(C#C(C(F)(F)(F)))c(F)c2)oc2ccccc12",
    "O=c1cc(-c2cc(C(F)(F)(F))c(C#C(C(F)(F)(F)))cc2)oc2cc(F)ccc12",
    "O=c1cc(-c2cc(C(F)(F)(F))c(C#C(C(F)(F)(F)))cc2)oc2ccc(F)cc12",
    "O=c1cc(-c2cc(C(F)(F)(F))c(C#C(C(F)(F)(F)))c(C(=O))c2)oc2ccccc12",
    "O=c1cc(-c2cc(C(F)(F)(F))c(C#C(C(F)(F)(F)))c(Cl)c2)oc2ccccc12"
]

# Create dictionary with model names as keys and SMILES lists as values
additional_smiles_dict = {
    'deepseek_v3p1_671b_maob': deepseek_v3p1_671b_maob,
    'gpt_5p2_tools_first': gpt_5p2_tools_first,
    'gpt_5p2_tools_second': gpt_5p2_tools_second
}

# Print summary
print("Additional SMILES Extraction Summary")
print("=" * 70)
print(f"Total sections: {len(additional_smiles_dict)}")
print(f"Total SMILES: {sum(len(smiles_list) for smiles_list in additional_smiles_dict.values())}")
print("\nSMILES count per section:")
for section, smiles_list in additional_smiles_dict.items():
    print(f"  {section}: {len(smiles_list)} SMILES")

# Optional: Print all SMILES organized by section
print("\n" + "=" * 70)
print("All SMILES by Section:")
print("=" * 70)
for section, smiles_list in additional_smiles_dict.items():
    print(f"\n{section}:")
    for i, smiles in enumerate(smiles_list, 1):
        print(f"  {i}. {smiles}")

print("\n" + "=" * 70)
print("\nDictionary variable name: additional_smiles_dict")
print("Access examples:")
print("  - additional_smiles_dict['deepseek_v3p1_671b_maob']")
print("  - additional_smiles_dict['gpt_5p2_tools_first']")
print("  - additional_smiles_dict['gpt_5p2_tools_second']")
