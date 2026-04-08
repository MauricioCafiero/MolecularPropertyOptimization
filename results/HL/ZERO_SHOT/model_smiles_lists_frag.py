# SMILES lists extracted from HL_gpt_ant_replies_frag.md and ollama_replies_frags.md
# Generated for HL ZERO_SHOT fragment experiment results

# OpenAI
openai_smiles = [
    "c1ccc2cc3cc(/C=C(C#N))ccc3cc2c1/C=C(C#N)",
    "c1ccc2cc3cc(/C=C(OC))ccc3cc2c1/C=C(OC)",
    "c1ccc2cc3cc(/C=C(OC))ccc3cc2c1/C=C(C#N)",
    "O=c1cc(-c2ccc(/C=C(C#N))cc2)oc2ccccc12",
    "O=c1cc(-c2cc(OC)cc(/C=C(C#N))c2)oc2ccccc12",
]

# Anthropic
anthropic_smiles = [
    "OCc1ccc2ccccc2c1C=CC#N",
    "C#C(OC(=O)C)c1ccc2cc3ccccc3cc2c1OC",
    "C=CC(C#N)c1ccc2ccccc2c1N(C(Cl)(Cl)Cl)",
    "C=CC(OC)c1ccc2ccccc2c1C=CC#N",
    "OCc1ccc2cc3ccccc3cc2c1C=CC#N",
]

# deepseek-v3.1:671b
deepseek_v3_smiles = [
    "O=C(C#C)c1ccc2ccccc2c1N(C(Cl)(Cl)Cl)",
    "c1ccc2cc3ccccc3cc2c1C=CC(OC)",
    "O=c1cc(-c2ccc(S([NH3+]))cc2)oc2ccccc12",
    "O=C(O)O[nH]1cccc1C#C(OC(=O)C)",
    "s1ccc(C#C)c1C#Cc1c[nH]cc1C=CC(C#N)",
]

# gpt-oss:120b
gpt_oss_120b_smiles = [
    "CN(C)c1ccc2ccccc2c1C#N",
    "CN(C)c1ccc2c3ccccc3c(c2c1)C#N",
    "CN(C)c1ccc(cc1)c1c2ccccc2oc2ccccc12C#N",
    "CN(C)c1ccc2sccc2c1C#N",
    "CN(C)c1ccc2c(c1)nc[nH]2C#N",
]

# gpt-oss:20b
gpt_oss_20b_smiles = [
    "c1ccc2cc3ccccc3cc2c1C#N",
    "c1ccc2ccccc2c1C#N",
    "O=c1cc(-c2ccccc2C#N)oc2ccccc12C#N",
    "c1ccccc1C#Cc2ccccc2C#N",
    "c1ccc2cc3ccccc3cc2c1C#C(OC(=O)C)",
]

# devstral-2:123b
devstral_2_smiles = [
    "c1ccc2cc3ccccc3cc2c1C=C(C#N)C=C(OC)C=C(C#N)",
    "O=c1cc(-c2ccccc2)oc2ccccc12C(=O)O(O)",
    "s1cccc1C=C(C#N)s1cccc1C=C(OC)s1cccc1",
    "c1ccc2ccccc2c1C(=O)N(Cl)C=C(N(C(Cl)(Cl)Cl))",
    "[nH]1cccc1C=C(C#N)[nH]1cccc1C=C(OC)[nH]1cccc1",
]

# cogito-2.1:671b
cogito_2_smiles = [
    "CN(C)c1ccc2cc(ccc2c1)[N+](=O)[O-]",
    "Nc1ccc2cc3cc(ccc3c2c1)[N+](=O)[O-]",
    "O=C1c2ccccc2OC2=C1C=CC(=C2)[N+](=O)[O-]",
    "s1ccc(-c2ccc[nH]2)c1[N+](=O)[O-]",
    "O=C1C=CC(=O)C2=C1N=C([N+](=O)[O-])N2",
]

# nemotron-3-nano:30b
nemotron_3_nano_smiles = [
    "c1ccc2ccccc2c1c(ccc(cc2)N(=O)=O)C=CC(CC)O",
    "c1ccc2ccccc2c1c(ccc(cc2)C#N)C=CC(CC)O",
    "N#CC(=O)C=C(c1ccc2ccccc2c1)C=CC(C(=O)N(C(Cl)(Cl)(Cl))C(Cl)(Cl)Cl))C(=O)C=O",
    "O=C1c2cc(-c3ccccc3)ccc2c1c4ccccc4",
    "N1C[NH3+]=n2c3ccccc3c2cc4ccccc4c1",
]

# gemini-3-flash-preview
gemini_3_flash_preview_smiles = [
    "N#Cc1c2ccccc2c(N(C)C)c3ccccc13",
    "N#Cc1sc(cc1)-c2sc(N(C)C)cc2",
    "CN(C)c1ccc(cc1)-c2cc(=O)c3ccccc3o2",
    "N#CC=Cc1c2ccccc2c(C=CC#N)c3ccccc13",
    "CN(C)c1sc(cc1)-c2c3ccccc3c(c4sc(N(C)C)cc4)c5ccccc25",
]

# kimi-k2.5
kimi_k2_smiles = [
    "COc1c2ccccc2c(/C=C/C#N)c2ccccc12",
    "N#CC=Cc1c2ccccc2c(/C=C/C#N)c2ccccc12",
    "COc1ccc(/C=C/c2cc(-c3ccccc3)oc3ccccc23)cc1",
    "N#CC=Cc1ccc(/C=C/OC)s1",
    "N#CC=Cc1c(/C=C/c2ccccc2OC)[nH]cn1",
]

# Dictionary with all model SMILES lists
model_smiles = {
    "openai": openai_smiles,
    "anthropic": anthropic_smiles,
    "deepseek-v3.1": deepseek_v3_smiles,
    "gpt-oss:120b": gpt_oss_120b_smiles,
    "gpt-oss:20b": gpt_oss_20b_smiles,
    "devstral-2": devstral_2_smiles,
    "cogito-2.1": cogito_2_smiles,
    "nemotron-3-nano": nemotron_3_nano_smiles,
    "gemini-3-flash-preview": gemini_3_flash_preview_smiles,
    "kimi-k2.5": kimi_k2_smiles,
}
