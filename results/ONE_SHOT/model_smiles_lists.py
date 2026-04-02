"""Top suggested SMILES extracted from ollama_replies.md (ONE_SHOT)."""

deepseek_v3_1_671b_smiles = [
    "O=c1cc(-c2cccc(C(C(=O)[O-]))c2)oc2cccc(C=C([N+](=O)[O-]))c12",
    "c1ccc2c(C(C(=O)[O-]))c3cccc(C=C([N+](=O)[O-]))c3cc2c1",
    "O=c1cc(-c2ccc(C(C(=O)[O-]))cc2)oc2ccc(C=C([N+](=O)[O-]))cc12",
    "c1cc(C(C(=O)[O-]))c2cc3cc(C=C([N+](=O)[O-]))cc3cc2c1",
    "O=c1c(C(C(=O)[O-]))c(-c2cc(C=C([N+](=O)[O-]))ccc2)oc2ccccc12",
]

gpt_oss_120b_smiles = [
    "O=c1c(C(=O)OCC)c(-c2ccc(I)cc2)oc2cccc(C(=O)OCC)c12",
    "O=c1c(C(=O)OCC)c(-c2ccc([N+](=O)[O-])cc2)oc2cccc([N+](=O)[O-])c12",
    "O=c1c(C(=O)OCC)c(-c2ccc([N+](=O)[O-])cc2)oc2cccc(C(=O)OCC)c12",
    "O=c1c(C(=O)OC(C)(C)C)c(-c2ccc(C(=O)OC(C)(C)C)cc2)oc2cccc(C(=O)OC(C)(C)C)c12",
    "O=c1c(C(=O)[O-])c(-c2ccc(C(=O)[O-])cc2)oc2cccc(C(=O)[O-])c12",
]

gpt_oss_20b_smiles = [
    "c1c(C(C(=O)[O-])c(C(C(=O)[O-]))ccc1",
    "O=c1c(C(C(=O)[O-])c(-c2cc(C(C(=O)[O-]))ccc2)oc2ccccc12",
    "c1c(C(C(=O)[O-])c(C(N)(C)C)cc1",
    "O=c1c(O(C#N))c(-c2cc(C(C(=O)[O-]))ccc2)oc2ccccc12",
]

devstral_2_123b_smiles = [
    "O=c1cc(-c2cccc(C(C(=O)[O-]))c2)oc2cc(C=C([N+](=O)[O-]))ccc12",
    "O=c1cc(-c2cccc(C(C(=O)[O-]))c2)oc2cc(C(=O)O(C(C)C))ccc12",
    "O=c1cc(-c2ccccc2)oc2cccc(C(C(=O)[O-]))c12",
    "O=c1cc(-c2cccc(C(C(=O)[O-]))c2)oc2ccn(C=C([N+](=O)[O-]))cc12",
    "O=c1cc(-c2cccc(C(C(=O)[O-]))c2)oc2cc(C(C(=O)[O-]))ccc12",
]

cogito_2_1_671b_smiles = [
    "O=c1cc(-c2cccc(C(C(=O)[O-]))c2)oc2cccc(C(C(=O)[O-]))c12",
    "O=c1cc(-c2cc(C(C(=O)[O-]))ccc2)oc2ccc(C=C([N+](=O)[O-]))cc12",
    "O=c1cc(-c2cc(C(=O)O(C(C)C))ccc2)oc2ccc(C(C(=O)[O-]))cc12",
    "O=c1cc(-c2ccccc2C(C(=O)[O-]))oc2cccc(C=C([N+](=O)[O-]))c12",
    "O=c1cc(-c2cc(C(C(=O)[O-]))ccc2C(C(=O)[O-]))oc2ccccc12",
]

nemotron_3_nano_30b_smiles = [
    "c1c2c(ccccc2)c(cccc1)C(=O)Oc3ccc(cc3)C(=O)O",
    "c1c2ccccc2c(ccccc1)C(=O)Nc3ccc(cc3)C(=O)O",
    "C1=CC=C(C=C1)C(=O)Oc2ccccc2C(=O)Oc3ccccc3",
    "c1c2c(ccccc2)c(ccccc1)C(=O)Oc3ccc(cc3)N=C=O",
    "c1c2c(ccccc2)c(ccccc1)C(=O)Oc3ccccc3C(=O)Oc4ccccc4",
]

gemini_3_flash_preview_smiles = [
    "[O-]C(=O)Cc1cccc2oc(cc(=O)c12)-c3ccc(CC(=O)[O-])cc3",
    "[O-]C(=O)CC(O)Cc1cccc2oc(cc(=O)c12)-c3ccccc3",
    "[O-]C(=O)Cc1cccc2oc(cc(=O)c12)-c3ccc(F)cc3",
    "[O-]C(=O)Cc1cccc2oc(cc(=O)c12)-c3ccc4ccccc4c3",
    "O=c1cc(-c2ccccc2)oc2c(O)cc(CC(=O)[O-])cc12",
]

kimi_k2_1t_smiles = [
    "O=C(O)Cc1cc2cc3ccccc3cc2o1",
    "O=C(O)CCc1cc2cc3ccccc3cc2o1",
    "O=C(O)Cc1cc2c(CC(=O)O)cc3ccccc3cc2o1",
    "O=C(O)Cc1cc2cc3cc4ccccc4cc3cc2o1",
    "O=C(O)C(C(=O)O)c1cc2cc3cc4ccccc4cc3cc2o1",
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
}
