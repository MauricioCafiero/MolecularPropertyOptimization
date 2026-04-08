# SMILES lists extracted from gpt_ant_replies_frag.md and ollama_replies_frags.md
# Generated for ZERO_SHOT fragment experiment results

# OpenAI
openai_smiles = [
    "O=C(O)CCCCCCc1ccc2ccccc2c1",
    "O=c1cc(-c2ccccc2)oc2ccccc12CCC(=O)O",
    "O=C(O)Cc1cccc(n1)c2ccc3ccccc3c2",
    "O=C(O)CCCCc1ccc2cc3ccccc3cc2c1",
    "O=C(O)Cc1ccc2cc(C#N)ccc2c1",
]

# Anthropic
anthropic_smiles = [
    "CC(C)C[C@H](O)[C@H](C)[C@@H](C=C[C@@H](C)C(=O)O)C[C@@H]1CCC2=C(C1)C=CC(=C2)C(C)C",
    "CC(C)C[C@H](O)[C@H](C)C(=O)Oc1ccc2ccccc2c1-c1ccccc1C(=O)O",
    "CC(C)C[C@H](O)[C@H](C)[C@@H](C=Cc1ccncc1)C[C@H](C(=O)O)C(C)C",
    "O=c1cc(-c2ccccc2)oc2ccc(cc12)CC[C@H](O)[C@H](C)C(=O)O",
    "c1ccc2cc3ccccc3cc2c1CC[C@H](O)[C@H](C(=O)O)C(C)C",
]

# deepseek-v3.1:671b
deepseek_v3_smiles = [
    "O=C(O)C(C)CC([O-])C(=O)c1cc(-c2ccccc2)oc2ccccc12",
    "O=C([O-])CC(C)Cc1cnc(n1)c1ccc2ccccc2c1",
    "C#Nc1ccc(CN(C(C)C)CC([O-])C(=O)O)cn1",
    "O=C([O-])c1ccco1",
    "C(C(=O)[O-])c1ccc2cc3ccccc3cc2c1",
]

# gpt-oss:120b
gpt_oss_120b_smiles = [
    "Ic1ncccc1CC(C(O)CO)C(=O)O",
    "c1ccc2ccccc2c1CC(C(O)CO)C(=O)O",
    "O=c1cc(-c2ccccc2)oc2ccccc12C(C(O)CO)C(=O)O",
    "s1cccc1CC(C(O)CO)C(=O)O",
    "n1c[nH]cc1CC(C(O)CO)C(=O)O",
]

# gpt-oss:20b
gpt_oss_20b_smiles = [
    "O=c1cc(-c2ccccc2)oc2ccccc12C#N",
    "O=c1cc(-c2ccccc2)oc2ccccc12C(C(=O)O(C(C)C))",
    "c1ccc2cc3ccccc3cc2c1C(=O)[O-]",
    "n1c[nH]cc1C(=O)[O-]C(C)C",
    "c1ccc2ccccc2c1C(C)C#N",
]

# devstral-2:123b
devstral_2_smiles = [
    "CC(C)(C)c1ccccc1C(=O)O[C@H](C)C(=O)N1CCN(C)CC1",
    "CC(C)c1ncccc1C(=O)N[C@H](C(=O)O)C(C)C",
    "CC(C)C(=O)Oc1ccc2ccccc2c1C(=O)N[C@H](C)C(=O)O",
    "CC(C)c1c[nH]cc1C(=O)N[C@H](C(=O)O)C(C)C",
    "CC(C)(C)c1ccc2cc3ccccc3cc2c1C(=O)O[C@H](C)C(=O)N1CCN(C)CC1",
]

# cogito-2.1:671b
cogito_2_smiles = [
    "CC(C)C(CC1=CC=C(C=C1)C2=CC=CC=C2)C(=O)[O-]",
    "CC(C)C(CC1=CC=CC2=CC=CC=C12)C(=O)[O-]",
    "CC(N(C)C)C(CC1=CC=CC2=CC3=CC=CC=C3CC2=C1)C(=O)[O-]",
    "CC(C)C(CC1=CC=C(O1)C2=CC=CC=C2)C(=O)[O-]",
    "CC(C)C(CC1=CC=CC2=CC=C(O2)C(=O)OCC(C)C)C(=O)[O-]",
]

# nemotron-3-nano:30b
nemotron_3_nano_smiles = [
    "c1c2ccnc3c2ncd2n1c(cc3)CC(=O)OCC(=O)[O-]",
    "c1c2ccnc3c2ncd2n1c(cc3)CC(=O)OCC(=O)N(C)C",
    "c1c2ccnc3c2ncd2n1c(cc3)CC(=O)OCC(C(S(=O)(=O)[O-]))(=-O)",
    "c1c2ccnc3c2ncd2n1c(cc3)CC(=O)OCC(=O)C#N",
    "c1c2ccnc3c2ncd2n1c(cc3)CC(=O)OCC(=O)CC(=O)[O-]",
]

# gemini-3-flash-preview
gemini_3_flash_preview_smiles = [
    "CC(C)c1c(C(=O)Nc2ccccc2)c(-c3ccc(F)cc3)n(CC[C@H](O)C[C@H](O)CC(=O)O)c1-c4ccccc4",
    "OC(=O)C[C@H](O)C[C@H](O)/C=C/c1c(-c2ccc(F)cc2)c2ccccc2nc1C(C)C",
    "CC(C)c1nc(C(C)C)c(C=C[C@H](O)C[C@H](O)CC(=O)O)c(c1OC)-c2ccc(F)cc2",
    "O=C(O)C[C@H](O)C[C@H](O)CCc1cc(=O)c2cc(F)ccc2o1-c3ccccc3",
    "N#Cc1c(C(C)C)n(CC[C@H](O)C[C@H](O)CC(=O)O)c(-c2ccc(F)cc2)c1-c3ccccc3",
]

# kimi-k2.5
kimi_k2_smiles = [
    "CN(C)CCc1cc2ccccc2cc1CC(=O)[O-]",
    "O=c1c(CC(=O)[O-])c(-c2ccccc2)oc2ccccc12",
    "NCc1cc2cc3ccccc3cc2cc1CC(=O)[O-]",
    "CC(C)OC(=O)c1cc(-c2ccccc2)sc1C#N",
    "O=C([O-])Cc1cc(C#CSC)ccn1",
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
