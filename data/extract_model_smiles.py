"""
Extract SMILES strings proposed by different models from model_replies.md
and organize them into a dictionary.
"""

# gpt5.2 suggestions
gpt5_2 = [
    "c1(C(F)(F)(F))ccc2cc3ccccc3cc2c1C(F)(F)(F)",
    "c1(C(F)(F)(F))ccc2cc3ccccc3cc2c1C(=O)N(OC(=O)C)",
    "c1(CC(C(Cl)(Cl)(Cl)))ccc2cc3ccccc3cc2c1C(=O)N(OC(=O)C)",
    "O=c1cc(-c2ccc(C(F)(F)(F))cc2)oc2cc(C(F)(F)(F))ccc12",
    "O=c1cc(-c2ccc(C(F)(F)(F))cc2)oc2cc(C(=O)N(OC(=O)C))ccc12"
]

# deepseek-v3.1:671b suggestions
deepseek_v3_1_671b = [
    "c1(C(F)(F))(F))ccc2ccccc2c1",
    "c1(C(Cl)(Cl))(Cl))ccc2ccccc2c1",
    "c1(C(=O)N(OC(=O)C))(C(=O)N(OC(=O)C)))ccc2ccccc2c1",
    "c1(C(F)(F))(C(Cl)(Cl))(Cl)))ccc2ccccc2c1",
    "c1(C(=O)O(N(C)C))(C(F)(F))(F)))ccc2ccccc2c1"
]

# gpt-oss:120b suggestions
gpt_oss_120b = [
    "c1(C(F)(F)F)ccc2c3ccccc3c4ccccc4c2c1",
    "c1(C(F)(F)F)ccc2c3ccccc3c4ccccc4c2c1C(F)(F)F",
    "c1(C(F)(F)F)ccc2c3ccccc3c4ccccc4c2c1C(Cl)(Cl)(Cl)",
    "c1ccc2c(c1)ccc3c2c4ccccc4c3C(F)(F)F",
    "c1ccc2c(c1)ccc3c2c4ccccc4c3C(F)(F)F"  # Note: text says "same as #4 C(F)(F)F" implying two CF3 groups
]

# gpt-oss:20b suggestions
gpt_oss_20b = [
    "c1(C(F)(F)(F))ccc2ccc3ccc4ccccc4c3c2c1",
    "c1(C(F)(F)(F))ccc2ccc3ccc4cc(C(F)(F)(F))ccc4c3c2c1",
    "c1(C(F)(F)(F))ccc2ccc3ccc4ccc5ccccc5c4c3c2c1",
    "c1(CCl3)ccc2cc3cc4ccccc4c3c2c1",
    "c1(C(F)(F)(F))ccc2ccc3ccc4ccccc4c3c(cc2c1)C(C)(C)C"
]

# devstral-2:123b suggestions
devstral_2_123b = [
    "c1(C(F)(F)(F))ccc2cc3cc4ccccc4cc3cc2c1",
    "c1(C(F)(F)(F))ccc2cc(C(F)(F)(F))ccc3ccccc23c1",
    "c1(C(=O)N(OC(=O)C))ccc2cc(C(F)(F)(F))ccc3ccccc23c1",
    "O=c1cc(-c2cc(C(F)(F)(F))ccc3ccccc23)oc2ccccc12",
    "c1(O(C(C)(C)C))ccc2cc(C(F)(F)(F))ccc3ccccc23c1"
]

# cogito-2.1:671b suggestions
cogito_2_1_671b = [
    "c1(C(F)(F)(F))ccc2cc3c(cc2c1)-c4ccccc4-c5ccccc35",
    "c1(CC(C(Cl)(Cl)(Cl)))ccc2cc3c(cc2c1)-c4ccccc4-c5ccccc35",
    "O=c1c(C(F)(F)(F))c(-c2ccc3ccccc3c2)oc2ccccc12",
    "c1(C(F)(F)(F))ccc2cc3cc4ccccc4cc3cc2c1",
    "c1(C(F)(F)(F))ccc2cc3cc4c(cc3cc2c1)-c5ccccc5-c6ccccc46"
]

# minimax-m2 suggestions
minimax_m2 = [
    "c1(C(F)(F)(F))ccc2(C(F)(F)(F))c3ccccc3cc2c1",
    "c1(C(F)(F)(F))ccc2c(C(=O)N(OC(=O)C))c3ccccc3cc2c1",
    "c1(C(F)(F)(F))ccc2c(C(=O)O(N(C)C))c3ccccc3cc2c1",
    "O=c1cc(-c2(C(F)(F)(F))ccccc2)oc2(C(F)(F)(F))ccccc12",
    "c1(C(F)(F)(F))ccc2c(C(N(C)C))c3ccccc3cc2c1"
]

# nemotron-3-nano:30b suggestions
nemotron_3_nano_30b = [
    "c1(C(F)(F)(F))ccc2cc3ccc3cc2c1",  # baseline reference
    "c1(C(F)(F)(F)C(F)(F)F)ccc2cc3ccc3cc2c1",
    "c1(c2ccc(C(F)(F)(F))c2ccc(cc3c2c2ccc(C(F)(F)(F))c3)cc1)O=C(N)C(=O)O",
    "c1(C(F)(F)(F)C(F)(F)F)ccc2cc3c(ccc2c3)C(=O)N(OC(=O)C)ccc4ccccc4",
    "c1(C(F)(F)(F)C(F)(F)F)ccc2cc3c(ccc2c3)C(N(=O)O)C(=O)O"
]

# gemini-3-flash-preview suggestions
gemini_3_flash_preview = [
    "FC(F)(F)c1ccc2cc3cc(C(F)(F)(F))ccc3cc2c1",
    "O=c1cc(-c2ccc(C(F)(F)(F))cc2)oc2cc3ccccc3cc12",
    "ClC(Cl)(Cl)Cc1ccc2cc3cc(C(F)(F)(F))ccc3cc2c1",
    "CC(=O)ON(C(=O)c1ccc2cc3cc(C(=O)N(OC(C)=O))ccc3cc2c1)C",
    "O=c1cc(-c2ccc(C(F)(F)(F))cc2)oc2cc(C(F)(F)(F))ccc12"
]

# Create dictionary with all model suggestions
model_smiles_dict = {
    "gpt5.2": gpt5_2,
    "deepseek-v3.1:671b": deepseek_v3_1_671b,
    "gpt-oss:120b": gpt_oss_120b,
    "gpt-oss:20b": gpt_oss_20b,
    "devstral-2:123b": devstral_2_123b,
    "cogito-2.1:671b": cogito_2_1_671b,
    "minimax-m2": minimax_m2,
    "nemotron-3-nano:30b": nemotron_3_nano_30b,
    "gemini-3-flash-preview": gemini_3_flash_preview
}

# Print summary
if __name__ == "__main__":
    print("=" * 80)
    print("Model SMILES Extraction Summary")
    print("=" * 80)
    
    for model_name, smiles_list in model_smiles_dict.items():
        print(f"\n{model_name}: {len(smiles_list)} molecules")
        for i, smiles in enumerate(smiles_list, 1):
            print(f"  {i}. {smiles}")
    
    print("\n" + "=" * 80)
    print(f"Total models: {len(model_smiles_dict)}")
    total_molecules = sum(len(smiles) for smiles in model_smiles_dict.values())
    print(f"Total unique proposals: {total_molecules}")
    print("=" * 80)
    
    # Show how to access the dictionary
    print("\n# Example usage:")
    print("from extract_model_smiles import model_smiles_dict")
    print("gpt5_molecules = model_smiles_dict['gpt5.2']")
    print("all_models = list(model_smiles_dict.keys())")
