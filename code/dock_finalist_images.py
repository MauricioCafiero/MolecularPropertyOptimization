from rdkit import Chem
from rdkit.Chem import Draw, QED
from PIL import Image

def scoring_function(smiles: str):
  '''
    calculates a property of the molecule based on the scoring_args. 
    If the calculation fails, returns -999.
  '''
  try:
    mol = Chem.MolFromSmiles(smiles)
    qed = QED.default(mol)

    p = QED.properties(mol)

    lipinski_hash = {'mw': 0, 'alogp': 1, 'hba': 2, 'hbd': 3, 'psa': 4, 'rb': 5, 'ar': 6, 'um': 7}

    alogp = p[lipinski_hash['alogp']]

    return qed, alogp, mol
  except Exception as e:
    print(f"Error processing {smiles}: {e}")
    return -999, -999, None

# zero_openai_smiles = [
#     "CC(C)C[C@H](O)C[C@H](O)CCCn1nnnc1-c2ccc(cc2)C(c3ccccc3)(c4ccccc4)O",
#     "CC(C)C[C@H](O)C[C@H](O)CCCP(=O)(O)O-c1ccc(cc1)C(c2ccccc2)(c3ccccc3)O",
#     "CC(C)C[C@H](O)C[C@H](O)CCC(=O)OCCc1nc2ccccc2n1-c3ccc(cc3)C(c4ccccc4)(c5ccccc5)O",
#     "CC(C)C[C@H](O)C[C@H](O)CCC(=O)OCCNS(=O)(=O)c1ccc(cc1)C(c2ccccc2)(c3ccccc3)O",
#     "CC(C)C[C@H](O)C[C@H](O)CCC(=O)O-c1ccc(cc1)C2(c3ccccc3)Cc4ccccc42",
# ]

# # Anthropic
# zero_anthropic_smiles = [
#     "CC(C)c1c(C(=O)Nc2ccccc2C(=O)O)c(c(c1)C)C(O)CC(O)C(O)=O",
#     "CC(C)C1=C(C(=O)O)C2CCC(O)C(O)C2(C)C1C(O)CC(O)C(=O)O",
#     "CC(C)c1c(C(=O)Nc2ccc(F)cc2)c(cc1C(O)CC(O)C(O)=O)CCc1ccccc1",
#     "c1c(C(O)CC(O)C(=O)O)c(cc(n1)C(C)C)C(=O)Nc1ccccc1C(C)C",
#     "CC(C)C1=C(C(=O)O)C(C)C(C)(O)C1C(O)CC(O)C(O)=O",
# ]

# # deepseek-v3.1:671b
# zero_deepseek_v3_smiles = [
#     "O=C(O)CC[C@H](O)C[C@H](O)CCc1c2ccccc2n(CC3CCCCC3)c1C",
#     "O=C(O)C[C@H](O)CC[C@H](O)CCc1cnc2c(c1)ccc(c2)F",
#     "O=C(O)C[C@H](O)CC[C@H](O)CCc1c(CN2CCOCC2)nc2ccc(C(F)(F)F)cc12",
#     "O=C(O)C[C@H](O)CC[C@H](O)CCS(=O)(=O)c1ccc(CN2CCCCC2)cc1",
#     "O=C(O)CC[C@H](O)C[C@H](O)CCc1cnc(-c2ccc(S(N)(=O)=O)cc2)nc1",
# ]

# # gpt-oss:120b
# zero_gpt_oss_120b_smiles = [
#     "CC(C)CCCC(C)C1CCC2C(C1)C(=O)O[C@@H]2C(=O)OCC(C)C",
#     "CC(C)CCCC(C)C1CCC2C(C1)C(=O)O[C@@H]2C(=O)OC(C)(C)C",
#     "CC(C)CCCC(C)C1CCC2C(C1)C(=O)O[C@@H]2C(=O)OC(C)C1=CC=CC=C1F",
#     "CC(C)CCCC(C)C1CCC2C(C1)C(=O)O[C@@H]2C(=O)OCC1=CN=CN1",
#     "CC(C)CCCC(C)C1CCC2C(C1)C(=O)O[C@@H]2C(=O)OC1=CC(=C(C=C1)Cl)C(F)(F)F",
# ]

# # gpt-oss:20b
# zero_gpt_oss_20b_smiles = [
#     "CC12CCC(=O)C3CC(C(=O)OCCc4occc4)C3(O)C1C2",
#     "CCCCCCCCCC(=O)C(O)C1(C)C(C(=O)OCCc2ncccc2)C(C)C1C",
#     "CC12CC(O)C3(C)C(=O)C(=O)OC(C)C1C3OC2",
#     "CC(C)(C)COC(=O)C1CC(C(=O)OCCc2c(C)cccc2)C(C)C1C",
#     "CC12CCCC(=O)C(O)C1NC(=O)S(=O)(=O)c3ccccc3",
# ]

# # devstral-2:123b
# zero_devstral_2_smiles = [
#     "CC(C)C(=O)O[C@@H](Cc1ccccc1)C(=O)N[C@@H](CC2=CC=C(C=C2)O)C(=O)O",
#     "CC(C)C(=O)O[C@@H](Cc1ccc(F)cc1)C(=O)N[C@@H](CCC(O)=O)C(=O)O",
#     "CC(C)C(=O)O[C@@H](C1CCC2=CC=CC=C21)C(=O)N[C@@H](CC(O)=O)C(=O)O",
#     "CC(C)C(=O)O[C@@H](C1CCN(C)CC1)C(=O)N[C@@H](CCc2ccco2)C(=O)O",
#     "CC(C)C(=O)O[C@@H](Cc1ccc(CC(C)C)cc1)C(=O)N[C@@H](CC(O)=O)C(=O)O",
# ]

# # cogito-2.1:671b
# zero_cogito_2_smiles = [
#     "CC(C)C1=CC(=C(C=C1)C2=CC(=O)NC(=O)N2C3CCCCC3)O",
#     "CC(C)C1=CC(=C(C=C1)C2=C(NC(=O)NC2=O)C3=CC=CC=C3)O",
#     "CC(C)C1=CC(=C(C=C1)C2=CC(=O)NC(=O)NC2C3=CC=CC=C3)OC",
#     "CC(C)C1=CC(=C(C=C1)C2=NC(=O)NC(=O)N2C3CCCC3)O",
#     "CC(C)C1=CC(=C(C=C1)C2=CC(=O)NC(=O)NC2C3CCC(CC3)O)O",
# ]

# # nemotron-3-nano:30b
# zero_nemotron_3_nano_smiles = [
#     "CC1=CC(C(=C(C=C1)C(=O)O)O)C(=O)NCC(=O)N",
#     "CC(C)(C)C(=O)O)C(=O)NCC(=O)N",
#     "O=C(N[C@H](C)C(=O)O)C(N[C@H]1CCC[CH]1)C1=CC=C(C=C1)C(=O)O",
#     "O=C(C)C1=CC=CC(=C1)C(O)=OC(=O)NCC(=O)N",
#     "CCOC(=O)NCC(=O)NCC1=CC=C(C=C1)C(=O)O",
# ]

# # gemini-3-flash-preview
# zero_gemini_3_flash_preview_smiles = [
#     "CC(C)c1c(\\C=C\\[C@H](O)C[C@H](O)CC(=O)O)c2cc(F)ccc2nc1N(C)S(=O)(=O)C",
#     "CC(C)n1c(C2=CC=C(F)C=C2)c(C2=CC3=CC=CC=C3C=C2)c(\\C=C\\[C@H](O)C[C@H](O)CC(=O)O)c1",
#     "CC(C)c1c(\\C=C\\[C@H](O)C[C@H](O)CC(=O)O)c(c(nc(n1)NS(=O)(=O)C(F)(F)F)C2=CC=C(F)C=C2)",
#     "CC(C)c1c(\\C=C\\[C@H](O)C[C@H](O)CC(=O)O)c(c2cc(C(=O)NC)ccc12)C3=CC=C(F)C=C3",
#     "CC(C)c1c(\\C=C\\[C@H](O)C[C@H](O)CC(=O)O)c(c2noc(c12)C3=CC=C(F)C=C3)",
# ]

# # kimi-k2:1t
# zero_kimi_k2_smiles = [
#     "O=C(O)CC(O)CC(O)CC1CC(c2ccc(F)cc2)CC1c1ccc(F)cc1",
#     "O=C(O)CC(O)CC(O)Cc1cccc2c1oc1cc(C(F)(F)F)ccc12",
#     "O=C(O)CC(O)CC(O)CC1CCc2c1cc(C(F)(F)F)cc2-c1ccccc1",
#     "O=C(O)CC(O)CC(O)Cc1cccc2nc(C3CC3)ccc12",
#     "O=C(O)CC(O)CC(O)CC1CCc2c1cc(Oc1cc(F)cc(F)c1)cc2",
# ]

# frags_openai_smiles = [
#     "O=C(O)CCCCCCc1ccc2ccccc2c1",
#     "O=c1cc(-c2ccccc2)oc2ccccc12CCC(=O)O",
#     "O=C(O)Cc1cccc(n1)c2ccc3ccccc3c2",
#     "O=C(O)CCCCc1ccc2cc3ccccc3cc2c1",
#     "O=C(O)Cc1ccc2cc(C#N)ccc2c1",
# ]

# # Anthropic
# frags_anthropic_smiles = [
#     "CC(C)C[C@H](O)[C@H](C)[C@@H](C=C[C@@H](C)C(=O)O)C[C@@H]1CCC2=C(C1)C=CC(=C2)C(C)C",
#     "CC(C)C[C@H](O)[C@H](C)C(=O)Oc1ccc2ccccc2c1-c1ccccc1C(=O)O",
#     "CC(C)C[C@H](O)[C@H](C)[C@@H](C=Cc1ccncc1)C[C@H](C(=O)O)C(C)C",
#     "O=c1cc(-c2ccccc2)oc2ccc(cc12)CC[C@H](O)[C@H](C)C(=O)O",
#     "c1ccc2cc3ccccc3cc2c1CC[C@H](O)[C@H](C(=O)O)C(C)C",
# ]

# # deepseek-v3.1:671b
# frags_deepseek_v3_smiles = [
#     "O=C(O)C(C)CC([O-])C(=O)c1cc(-c2ccccc2)oc2ccccc12",
#     "O=C([O-])CC(C)Cc1cnc(n1)c1ccc2ccccc2c1",
#     "C#Nc1ccc(CN(C(C)C)CC([O-])C(=O)O)cn1",
#     "O=C([O-])c1ccco1",
#     "C(C(=O)[O-])c1ccc2cc3ccccc3cc2c1",
# ]

# # gpt-oss:120b
# frags_gpt_oss_120b_smiles = [
#     "Ic1ncccc1CC(C(O)CO)C(=O)O",
#     "c1ccc2ccccc2c1CC(C(O)CO)C(=O)O",
#     "O=c1cc(-c2ccccc2)oc2ccccc12C(C(O)CO)C(=O)O",
#     "s1cccc1CC(C(O)CO)C(=O)O",
#     "n1c[nH]cc1CC(C(O)CO)C(=O)O",
# ]

# # gpt-oss:20b
# frags_gpt_oss_20b_smiles = [
#     "O=c1cc(-c2ccccc2)oc2ccccc12C#N",
#     "O=c1cc(-c2ccccc2)oc2ccccc12C(C(=O)O(C(C)C))",
#     "c1ccc2cc3ccccc3cc2c1C(=O)[O-]",
#     "n1c[nH]cc1C(=O)[O-]C(C)C",
#     "c1ccc2ccccc2c1C(C)C#N",
# ]

# # devstral-2:123b
# frags_devstral_2_smiles = [
#     "CC(C)(C)c1ccccc1C(=O)O[C@H](C)C(=O)N1CCN(C)CC1",
#     "CC(C)c1ncccc1C(=O)N[C@H](C(=O)O)C(C)C",
#     "CC(C)C(=O)Oc1ccc2ccccc2c1C(=O)N[C@H](C)C(=O)O",
#     "CC(C)c1c[nH]cc1C(=O)N[C@H](C(=O)O)C(C)C",
#     "CC(C)(C)c1ccc2cc3ccccc3cc2c1C(=O)O[C@H](C)C(=O)N1CCN(C)CC1",
# ]

# # cogito-2.1:671b
# frags_cogito_2_smiles = [
#     "CC(C)C(CC1=CC=C(C=C1)C2=CC=CC=C2)C(=O)[O-]",
#     "CC(C)C(CC1=CC=CC2=CC=CC=C12)C(=O)[O-]",
#     "CC(N(C)C)C(CC1=CC=CC2=CC3=CC=CC=C3CC2=C1)C(=O)[O-]",
#     "CC(C)C(CC1=CC=C(O1)C2=CC=CC=C2)C(=O)[O-]",
#     "CC(C)C(CC1=CC=CC2=CC=C(O2)C(=O)OCC(C)C)C(=O)[O-]",
# ]

# # nemotron-3-nano:30b
# frags_nemotron_3_nano_smiles = [
#     "c1c2ccnc3c2ncd2n1c(cc3)CC(=O)OCC(=O)[O-]",
#     "c1c2ccnc3c2ncd2n1c(cc3)CC(=O)OCC(=O)N(C)C",
#     "c1c2ccnc3c2ncd2n1c(cc3)CC(=O)OCC(C(S(=O)(=O)[O-]))(=-O)",
#     "c1c2ccnc3c2ncd2n1c(cc3)CC(=O)OCC(=O)C#N",
#     "c1c2ccnc3c2ncd2n1c(cc3)CC(=O)OCC(=O)CC(=O)[O-]",
# ]

# # gemini-3-flash-preview
# frags_gemini_3_flash_preview_smiles = [
#     "CC(C)c1c(C(=O)Nc2ccccc2)c(-c3ccc(F)cc3)n(CC[C@H](O)C[C@H](O)CC(=O)O)c1-c4ccccc4",
#     "OC(=O)C[C@H](O)C[C@H](O)/C=C/c1c(-c2ccc(F)cc2)c2ccccc2nc1C(C)C",
#     "CC(C)c1nc(C(C)C)c(C=C[C@H](O)C[C@H](O)CC(=O)O)c(c1OC)-c2ccc(F)cc2",
#     "O=C(O)C[C@H](O)C[C@H](O)CCc1cc(=O)c2cc(F)ccc2o1-c3ccccc3",
#     "N#Cc1c(C(C)C)n(CC[C@H](O)C[C@H](O)CC(=O)O)c(-c2ccc(F)cc2)c1-c3ccccc3",
# ]

# # kimi-k2.5
# frags_kimi_k2_smiles = [
#     "CN(C)CCc1cc2ccccc2cc1CC(=O)[O-]",
#     "O=c1c(CC(=O)[O-])c(-c2ccccc2)oc2ccccc12",
#     "NCc1cc2cc3ccccc3cc2cc1CC(=O)[O-]",
#     "CC(C)OC(=O)c1cc(-c2ccccc2)sc1C#N",
#     "O=C([O-])Cc1cc(C#CSC)ccn1",
# ]

# one_deepseek_v3_1_671b_smiles = [
#     "O=c1cc(-c2cccc(C(C(=O)[O-]))c2)oc2cccc(C=C([N+](=O)[O-]))c12",
#     "c1ccc2c(C(C(=O)[O-]))c3cccc(C=C([N+](=O)[O-]))c3cc2c1",
#     "O=c1cc(-c2ccc(C(C(=O)[O-]))cc2)oc2ccc(C=C([N+](=O)[O-]))cc12",
#     "c1cc(C(C(=O)[O-]))c2cc3cc(C=C([N+](=O)[O-]))cc3cc2c1",
#     "O=c1c(C(C(=O)[O-]))c(-c2cc(C=C([N+](=O)[O-]))ccc2)oc2ccccc12",
# ]

# one_gpt_oss_120b_smiles = [
#     "O=c1c(C(=O)OCC)c(-c2ccc(I)cc2)oc2cccc(C(=O)OCC)c12",
#     "O=c1c(C(=O)OCC)c(-c2ccc([N+](=O)[O-])cc2)oc2cccc([N+](=O)[O-])c12",
#     "O=c1c(C(=O)OCC)c(-c2ccc([N+](=O)[O-])cc2)oc2cccc(C(=O)OCC)c12",
#     "O=c1c(C(=O)OC(C)(C)C)c(-c2ccc(C(=O)OC(C)(C)C)cc2)oc2cccc(C(=O)OC(C)(C)C)c12",
#     "O=c1c(C(=O)[O-])c(-c2ccc(C(=O)[O-])cc2)oc2cccc(C(=O)[O-])c12",
# ]

# one_gpt_oss_20b_smiles = [
#     "c1c(C(C(=O)[O-])c(C(C(=O)[O-]))ccc1",
#     "O=c1c(C(C(=O)[O-])c(-c2cc(C(C(=O)[O-]))ccc2)oc2ccccc12",
#     "c1c(C(C(=O)[O-])c(C(N)(C)C)cc1",
#     "O=c1c(O(C#N))c(-c2cc(C(C(=O)[O-]))ccc2)oc2ccccc12",
# ]

# one_devstral_2_123b_smiles = [
#     "O=c1cc(-c2cccc(C(C(=O)[O-]))c2)oc2cc(C=C([N+](=O)[O-]))ccc12",
#     "O=c1cc(-c2cccc(C(C(=O)[O-]))c2)oc2cc(C(=O)O(C(C)C))ccc12",
#     "O=c1cc(-c2ccccc2)oc2cccc(C(C(=O)[O-]))c12",
#     "O=c1cc(-c2cccc(C(C(=O)[O-]))c2)oc2ccn(C=C([N+](=O)[O-]))cc12",
#     "O=c1cc(-c2cccc(C(C(=O)[O-]))c2)oc2cc(C(C(=O)[O-]))ccc12",
# ]

# one_cogito_2_1_671b_smiles = [
#     "O=c1cc(-c2cccc(C(C(=O)[O-]))c2)oc2cccc(C(C(=O)[O-]))c12",
#     "O=c1cc(-c2cc(C(C(=O)[O-]))ccc2)oc2ccc(C=C([N+](=O)[O-]))cc12",
#     "O=c1cc(-c2cc(C(=O)O(C(C)C))ccc2)oc2ccc(C(C(=O)[O-]))cc12",
#     "O=c1cc(-c2ccccc2C(C(=O)[O-]))oc2cccc(C=C([N+](=O)[O-]))c12",
#     "O=c1cc(-c2cc(C(C(=O)[O-]))ccc2C(C(=O)[O-]))oc2ccccc12",
# ]

# one_nemotron_3_nano_30b_smiles = [
#     "c1c2c(ccccc2)c(cccc1)C(=O)Oc3ccc(cc3)C(=O)O",
#     "c1c2ccccc2c(ccccc1)C(=O)Nc3ccc(cc3)C(=O)O",
#     "C1=CC=C(C=C1)C(=O)Oc2ccccc2C(=O)Oc3ccccc3",
#     "c1c2c(ccccc2)c(ccccc1)C(=O)Oc3ccc(cc3)N=C=O",
#     "c1c2c(ccccc2)c(ccccc1)C(=O)Oc3ccccc3C(=O)Oc4ccccc4",
# ]

# one_gemini_3_flash_preview_smiles = [
#     "[O-]C(=O)Cc1cccc2oc(cc(=O)c12)-c3ccc(CC(=O)[O-])cc3",
#     "[O-]C(=O)CC(O)Cc1cccc2oc(cc(=O)c12)-c3ccccc3",
#     "[O-]C(=O)Cc1cccc2oc(cc(=O)c12)-c3ccc(F)cc3",
#     "[O-]C(=O)Cc1cccc2oc(cc(=O)c12)-c3ccc4ccccc4c3",
#     "O=c1cc(-c2ccccc2)oc2c(O)cc(CC(=O)[O-])cc12",
# ]

# one_kimi_k2_1t_smiles = [
#     "O=C(O)Cc1cc2cc3ccccc3cc2o1",
#     "O=C(O)CCc1cc2cc3ccccc3cc2o1",
#     "O=C(O)Cc1cc2c(CC(=O)O)cc3ccccc3cc2o1",
#     "O=C(O)Cc1cc2cc3cc4ccccc4cc3cc2o1",
#     "O=C(O)C(C(=O)O)c1cc2cc3cc4ccccc4cc3cc2o1",
# ]

# one_gpt_5_2_smiles = [
#     "O=c1cc(-c2ccc(C(C(=O)[O-]))cc2)oc2cccc(C(C(=O)[O-]))c12",
#     "O=c1cc(-c2ccc(C=C([N+](=O)[O-]))cc2)oc2cccc(C(C(=O)[O-]))c12",
#     "O=c1cc(-c2ccccc2)oc2cccc(C(C(=O)[O-])C(=O)[O-])c12",
#     "O=c1cc(-c2ccccc2C(C(=O)[O-]))oc2cccc(C(C))c12",
#     "O=c1cc(-c2ccc(OC#N)cc2)oc2cccc(C(C(=O)[O-]))c12",
# ]

# one_claude_smiles = [
#     "O=c1cc(-c2cccc(c2)C(=O)[O-])oc2cccc(C(=O)[O-])c12",
#     "O=c1cc(-c2cc3ccccc3cc2C(=O)[O-])oc2cccc(C(=O)[O-])c12",
#     "O=c1cc(-c2ccccc2C(=O)[O-])oc2c(C=C([N+](=O)[O-]))ccc(C(C(=O)[O-]))c12",
#     "O=c1cc(-c2ccc(C(=O)[O-])cc2)oc2ccc(C(=O)[O-])cc12",
#     "O=c1cc(-c2cc3ccccc3cc2C(=O)[O-])oc2c(C(C(=O)[O-]))ccc(C(=O)[O-])c12",
# ]

# claude = ['O=c1c(O)c(-c2c(C)cc(C(=O)N)cc2)oc2c(F)ccc(C(=O)N)c12',
#               'O=c1c(O)c(-c2c(C)cc(C(=O)N(C)C)cc2)oc2c(F)ccc(C(=O)N)c12',
#               'O=c1c(O)c(-c2c(C)cc(C(=O)N(C)C)cc2)oc2c(F)ccc(C(=O)N(C)C)c12',
#               'O=c1c(O)c(-c2c(C(=O)[O-])c(NC(=O)C)ccc2)oc2c(C(F)(F)(F))ccc(C(=O)N)c12',
#               'O=c1c(O)c(-c2c(C(=O)[O-])c(NC(=O)C)c(F)cc2)oc2cc(F)cc(C)c12']
             
# gpt5p2 = ['O=c1c(O)c(-c2ccc(CC(C)(C)C)cc2)oc2cccc(C(C(=O)O))c12',
#                  'O=c1c(O)c(-c2ccc(OC(F)(F)(F))cc2)oc2cccc(C(C(=O)O))c12']

# gemini3flash = ['O=c1cc(-c2cc(F)c(F)cc2)oc2cc(F)cc(CC(=O)[O-])c12',
#               'O=c1cc(-c2c(OC)c(F)c(F)cc2)oc2cc(F)cc(CC(=O)[O-])c12',
#               'O=c1cc(-c2ccc(F)cc2)oc2cc(F)cc(CC(=O)[O-])c12',
#               'O=c1cc(-c2c(F)cc(F)cc2)oc2cc(F)cc(CC(=O)[O-])c12',
#               'O=c1cc(-c2cc(F)c(F)cc2)oc2cccc(CC(=O)[O-])c12']

kimi_k2 = ['Cc1c(C)c2c(c3c(F)c(O)c(C(=O)N)c(C)c13)C(C)=C(C(=O)[O-])O2',
           'Cc1c(C)c2c(c3c(O)c(C(=O)N)c(C)c(C)c13)C(C)=C(C(=O)[O-])O2',
           'Cc1c(C)c2c(c3c(O)c(C(=O)N)c(C)c(F)c13)C(C)=C(C(=O)[O-])O2' ]


deepseek = ['O=c1c(F)c(-c2cnc(F)c(C)c2)oc2cccc(C(C(F)(F)O))c12', 
            'O=c1c(F)c(-c2cnc(F)c(C)c2)oc2c(OC)ccc(C(C(F)(F)O))c12', 
            'O=c1c(F)c(-c2cnc(F)c(C)c2)oc2c(C(=O)N)ccc(C(C(F)(F)O))c12', 
            'O=c1c(F)c(-c2cnc(F)c(C)c2)oc2c(C(F)(F)F)ccc(C(C(F)(F)O))c12']

hash_lists = {
    # 'OPENAI Zero-shot': zero_openai_smiles,
    # 'ANTHROPIC Zero-shot': zero_anthropic_smiles,
    # 'Deepseek-v3.1 Zero-shot': zero_deepseek_v3_smiles,
    # 'GPT-OSS-120B Zero-shot': zero_gpt_oss_120b_smiles,
    # 'GPT-OSS-20B Zero-shot': zero_gpt_oss_20b_smiles,
    # 'DEVSTRAL-2 Zero-shot': zero_devstral_2_smiles,
    # 'COGITO-2.1 Zero-shot': zero_cogito_2_smiles,
    # 'NEMOTRON-3-NANO Zero-shot': zero_nemotron_3_nano_smiles,
    # 'GEMINI Zero-shot': zero_gemini_3_flash_preview_smiles,
    # 'KIMI-K2 Zero-shot': zero_kimi_k2_smiles,
    # 'OPENAI Fragments': frags_openai_smiles,
    # 'ANTHROPIC Fragments': frags_anthropic_smiles,
    # 'Deepseek-v3.1 Fragments': frags_deepseek_v3_smiles,
    # 'GPT-OSS-120B Fragments': frags_gpt_oss_120b_smiles,
    # 'GPT-OSS-20B Fragments': frags_gpt_oss_20b_smiles,
    # 'DEVSTRAL-2 Fragments': frags_devstral_2_smiles,
    # 'COGITO-2.1 Fragments': frags_cogito_2_smiles,
    # 'NEMOTRON-3-NANO Fragments': frags_nemotron_3_nano_smiles,
    # 'GEMINI Fragments': frags_gemini_3_flash_preview_smiles,
    # 'KIMI-K2 Fragments': frags_kimi_k2_smiles,
    # 'OPENAI One-shot': one_gpt_5_2_smiles,
    # 'ANTHROPIC One-shot': one_claude_smiles,
    # 'Deepseek-v3.1 One-shot': one_deepseek_v3_1_671b_smiles,
    # 'GPT-OSS-120B One-shot': one_gpt_oss_120b_smiles,
    # 'GPT-OSS-20B One-shot': one_gpt_oss_20b_smiles,
    # 'DEVSTRAL-2 One-shot': one_devstral_2_123b_smiles,
    # 'COGITO-2.1 One-shot': one_cogito_2_1_671b_smiles,
    # 'NEMOTRON-3-NANO One-shot': one_nemotron_3_nano_30b_smiles,
    # 'GEMINI One-shot': one_gemini_3_flash_preview_smiles,
    # 'KIMI-K2 One-shot': one_kimi_k2_1t_smiles,
    # 'ANTHROPIC': claude,
    # 'OPENAI': gpt5p2,
    # 'GEMINI': gemini3flash
    'KIMI-K2': kimi_k2,
    'Deepseek': deepseek
}

all_imgs = []
good_names = []
for name, smiles_list in hash_lists.items():
    alogp_list = []
    qed_list = []
    mols = []
    for smile in smiles_list:
        qed, alogp, mol = scoring_function(smile)
        if mol is None:
            continue
        alogp_list.append(alogp)
        qed_list.append(qed)
        mols.append(mol)
    legs = [f'{name} {i+1}: QED={q:.2f}, logP={a:.2f}' for i, (q, a) in enumerate(zip(qed_list, alogp_list))]
    try:
        img = Draw.MolsToGridImage(mols, legends=legs, molsPerRow=3)
        all_imgs.append(img)
        good_names.append(name)
        print(f'Finished processing {name}')
    except Exception as e:
        print(f"Error processing {name}: {e}")
    

for name, img in zip(good_names, all_imgs):
    print(f'Saving image for {name}')
    filename = f"../results/dock_finalist_images/{name}_finalists.png"
    img.save(filename)


## order openai, anthropic, gemini for zero and one shots
# zero_shot = ['CC(C)C[C@H](O)C[C@H](O)CCC(=O)O-c1ccc(cc1)C2(c3ccccc3)Cc4ccccc42',
#              'c1c(C(O)CC(O)C(=O)O)c(cc(n1)C(C)C)C(=O)Nc1ccccc1C(C)C',
#              'CC(C)n1c(C2=CC=C(F)C=C2)c(C2=CC3=CC=CC=C3C=C2)c(\C=C\[C@H](O)C[C@H](O)CC(=O)O)c1']

# zero_shot_frags = ['O=C(O)Cc1cccc(n1)c2ccc3ccccc3c2',
#                    'CC(C)C[C@H](O)[C@H](C)C(=O)Oc1ccc2ccccc2c1-c1ccccc1C(=O)O',
#                    'OC(=O)C[C@H](O)C[C@H](O)/C=C/c1c(-c2ccc(F)cc2)c2ccccc2nc1C(C)C']

# one_shot = [
#                    'O=c1cc(-c2ccc(C=C([N+](=O)[O-]))cc2)oc2cccc(C(C(=O)[O-]))c12',
#                    'O=c1cc(-c2cc3ccccc3cc2C(=O)[O-])oc2c(C(C(=O)[O-]))ccc(C(=O)[O-])c12',
#                    '[O-]C(=O)Cc1cccc2oc(cc(=O)c12)-c3ccc4ccccc4c3']