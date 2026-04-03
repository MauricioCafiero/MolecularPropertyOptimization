"""Top suggested SMILES extracted from ollama_replies.md and gpt_ant_replies.md (ONE_SHOT/HL)."""

deepseek_v3_1_671b_smiles = [
    "O=c1c2ccccc2c(S([NH3+]))c3ccccc3c1=O",
    "O=c1c2ccc(S([NH3+]))cc2c(C#N)c3ccccc3c1=O",
    "O=c1c2ccccc2c(OC)c3ccc(C(=O)O(O))cc3c1=O",
    "n1c2ccccc2c(C(=O)O(O))c3ccccc3c1=O",
    "O=c1c2cccc(S([NH3+]))c2c(C#N)c3cccc(C#N)c3c1=O",
]

gpt_oss_120b_smiles = [
    "S([NH3+])c1ccc2c(c1)ccc3c2ccc3",
    "S([NH3+])c1ccc2c(c1)ccc3c2ccc3C#N",
    "COc1ccc2c(c1)ccc3c2ccc3S([NH3+])",
    "S([NH3+])c1c(S([NH3+]))c2ccc3ccccc3c2c1",
    "S([NH3+])c1ccc2c(c1)ccc3c2ccc3[N+](=O)[O-]",
]

gpt_oss_20b_smiles = [
    "c1ccc2ccccc2c3ccccc3c1",
    "c1c2ccccc2c3ccccc3c1",
    "c1c2ccccc2c3ccccc13",
    "n1c2ccccc2c3ccccc3c1",
    "c1c2c3ccccc3c4ccccc4c2c1",
]

devstral_2_123b_smiles = [
    "c1ccc2cc3ccccc3cc2c1(C(=O)N(Cl))",
    "n1ccc2cc3ccccc3cc2c1(C(=O)O(O))",
    "c1ccc2cc3ccccc3cc2c1(C#N)",
    "o1ccc2cc3ccccc3cc2c1(C(=O)N(Cl))",
    "c1ccc2cc3ccccc3cc2c1(C(=O)N(Cl))(C#N)",
]

cogito_2_1_671b_smiles = [
    "c1cc2c3c4cc(C(=O)O(O))ccc4ccc3ccc2c1",
    "O=C(O)c1ccc2c3c1c1c4c(c3ccc2)ccc(C(=O)N(Cl))c4c1",
    "s1ccc2sc3c4c(cc3c2c1)ccc(C(=O)O(O))c4",
    "c1cc2c3c4c5c6c1c1c7c(c6cc5cc4cc3cc2)ccc(C(=O)N(Cl))c7c1",
    "O=C(O)c1ccc2sc3c(c2c1)ccc(C(=O)N(Cl))c3",
]

nemotron_3_nano_30b_smiles = [
    "c1ccc(S(=O)(=O)[NH3+])c2ccccc2",
    "c1c(S([NH3+]))cccc1",
    "n1c(S([NH3+]))c2ccccc2",
    "[NH3+]S(=O)(=O)c1ccc2ccccc2",
    "c1c(S([NH3+]))c2cc(ccc2)[N+](=O)[O-]",
]

gemini_3_flash_preview_smiles = [
    "CC(=O)OC#Cc1ccc2cc3cc4ccccc4cc3cc2c1",
    "[NH3+]S(c1c2ccccc2c(S([NH3+]))c3ccccc13)",
    "O=c1cc(-c2ccc3ccccc3c2)oc2cc(S([NH3+]))ccc12",
    "c1ccc2cc3cc4cc5ccccc5cc4cc3cc2c1",
    "N#CC=Cc1ccc(-c2c3ccccc3cc4ccccc24)cc1",
]

kimi_k2_1t_smiles = [
    "c1(S([NH3+]))ccc2cc3ccccc3cc2c1",
    "c1cc(S([NH3+]))c2cc3ccccc3cc2c1",
    "c1ccc2c(S([NH3+]))c3ccccc3cc2c1",
    "O=c1c(S([NH3+]))c(-c2ccccc2)oc2ccccc12",
    "O=c1cc(-c2ccc(S([NH3+]))cc2)oc2ccccc12",
]

gpt5p2_smiles = [
    "CC(=O)OcC#Cc1ccc2cccc3ccc1c23",
    "CC(=O)OcC#Cc1cccc2cccc3cccc4cccc1c234",
    "CC(=O)OcC#Cc1ccc2cccc3cccc4ccc1c2c34",
    "N#CC=CCc1ccc2cccc3ccc1c23",
    "CC(=O)OcC#Cc1ccc2cccc3cccc4ccc(C#Cc5oc(=O)ccccc5)c1c2c34",
]

claude_smiles = [
    "c1cc2ccc3cccc4cccc(c1)c2c34",
    "c1cc2ccc3cccc4cccc(OC)c(c1)c2c34",
    "c1cc2ccc3cccc4cccc5cccc(c1)c2c3c45",
    "c1ccc2c(C=CC=CC#N)cccc2c1",
    "C1=Cc2ccc3ccccc3c2C1",
]

model_smiles = {
    "deepseek-v3.1:671b": deepseek_v3_1_671b_smiles,
    "gpt-oss:120b": gpt_oss_120b_smiles,
    "gpt-oss:20b": gpt_oss_20b_smiles,
    "devstral-2:123b": devstral_2_123b_smiles,
    "cogito-2.1:671b": cogito_2_1_671b_smiles,
    "nemotron-3-nano:30b": nemotron_3_nano_30b_smiles,
    "gemini-3-flash-preview": gemini_3_flash_preview_smiles,
    "kimi-k2:1t": kimi_k2_1t_smiles,
    "gpt-5p2": gpt5p2_smiles,
    "claude": claude_smiles,
}