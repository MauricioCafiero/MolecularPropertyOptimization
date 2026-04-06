# SMILES lists extracted from HL_gpt_ant_replies.md and ollama_replies.md
# Generated for HL ZERO_SHOT experiment results

# OpenAI
openai_smiles = [
    "CN(C)c1ccc(/C=C/C(=C(C#N)C#N))cc1",
    "CN(C)c1ccc(/C=C/C=C/C(=C(C#N)C#N))cc1",
    "CN(C)c1ccc(/C=C/C(=C(C#N)C#N)C#N)cc1",
    "CN(C)c1ccc(-c2nc3ccccc3s2)cc1",
    "N#CC(=C(C#N)C#N)C#N",
]

# Anthropic
anthropic_smiles = [
    "C1=CC=C2C(=C1)C=CC3=CC=CC4=CC=CC(=C3C2=C4)C5=CC=CC6=CC=CC=C6C5",
    "C1=C(S1)C2=C(SC(=C2)S3CCCS3)S4CCCS4",
    "C1=CC(=CC=C1C2=CC=CC(=C2)C3=CC=CC(=C3)C4=CC=CC(=C4)C5=CC=CC=C5)C6=CC=CC=C6",
    "C1=CSC(=C1)C2=CC=CC(=C2)C3=CC=CS3",
    "C1=CC2=C(C=C1)C=CC3=CC=CC4=CC=CC5=CC=CC6=CC=CC7=CC=CC(=C7C(=C6C(=C5C(=C4C(=C3C=C2)C=C)C=C)C=C)C=C)C=C",
]

# deepseek-v3.1:671b
deepseek_v3_smiles = [
    "c1ccc2cc3cc4cc5cc6cc7ccccc7cc6cc5cc4cc3cc2c1",
    "N#Cc1ccc(C(C#N)(C#N)C#N)cc1",
    "c1cnccc1-c1ccc(s1)/C=C/c1sc(c2ccncc2)cc1",
    "c1cc2nc3ccccc3nc2n1-c1nc2ccccc2n1",
    "c1cc2ccc3ccc4ccc5ccc1c2c3c4c5",
]

# gpt-oss:120b
gpt_oss_120b_smiles = [
    "CN(C)C1=CC=C(C=C1)C2=CN3C(=O)C4=CC=CC=C4C5=CC=CC=C5C(=O)N3C2",
    "C1=CC2=C(C=C1)SC=S2C3=CN=C(N=C3)C4=CC=CC=C4",
    "C1=CC2=C(C=C1)C3=CC4=C(C=C3C5=CC=CC=C5)C(=O)N(C6=CC=CC=C6)C(=O)C4=C2",
    "C1=SC=CS1C2=SC=CS2",
    "O=C1C2=CC=CC3=CC=CC4=CC=CC5=CC=CC6=CC=CC=1N2N6C3C5",
]

# gpt-oss:20b
gpt_oss_20b_smiles = [
    "C60",
    "C70",
    "CCCCCC=CC=CC=CC=CC=C",
    "C1=CC2=CC3=CC4=CC5=CC=CC6=CC=C1C2C3C4C5C6",
    "O=[N+]c1ccc(cc1)N(=O)=O-C1=CC2=CC3=CC=CC=C3CC4=CC=CC4C=C2C=C1",
]

# devstral-2:123b
devstral_2_smiles = [
    "C1=C(C=S1)C2=C(C=S2)C3=C(C=S3)C4=C(C=S4)",
    "N#C-C(C#N)=C1C=C(C#N)C(C#N)=C1C#N",
    "C1=CC=C2C=C3C=CC=C4C=C5C=CC=CC5=C4C=C3C=C21",
    "C1=CC=C2C=C3C=CC=C4C=C5C=CC=CC5=C4C=C3C=C21",
    "C1=CC=C2C=C3C=CC=C4C=C5C=CC=CC5=C4C=C3C=C21",
]

# cogito-2.1:671b
cogito_2_smiles = [
    "C1=CC=C2C(=C1)C=CC=C2",
    "C1=CC2=C3C(=C1)C=CC4=CC=CC(=C43)C=C2",
    "C1=CC=C2C(=C1)C3=CC=CC4=CC=CC(=C43)C=C2",
    "C1=CC2=CC3=CC=C(N)C=C3C=C2C=C1",
    "C1=CC2=C(C=CC3=CC4=C(C=CC=C4)C=C32)C=C1",
]

# nemotron-3-nano:30b
nemotron_3_nano_smiles = [
    "graphene",
]

# gemini-3-flash-preview
gemini_3_flash_preview_smiles = [
    "c1ccc2cc3cc4cc5cc6cc7ccccc7cc6cc5cc4cc3cc2c1",
    "Fc1c(F)cc2c(c1)c3c(s2)c4c(nsn4)c5c(s3)c6cc(F)c(F)cc6n5",
    "c1cc(sc1)-c2c3nsnc3c(c4sccc4)c5nsnc25",
    "O=C1C(=C2C=CC(=[N+](C)C)C=C2)C(=O)C(=C3C=CC(=[N+](C)C)C=C3)C1=O",
    "N#CC(C#N)=C1C=CC(=C2C=CC(=C3C=CC(=C4C=CC(=C(C#N)C#N)S4)S3)S2)S1",
]

# kimi-k2:1t
kimi_k2_smiles = [
    "C=C=C=C=C=C=C=C",
    "C=C=C=C=C=C=C=C=C=C",
    "S=C=C=C=C=S",
    "c1cc2cc3cc4cc5cc6cc7cc8cc9cc1c2c3c4c5c6c7c89",
    "C1=C2C(=C(C(=C(C1=S)S)S)S)C2=S",
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
    "kimi-k2": kimi_k2_smiles,
}
