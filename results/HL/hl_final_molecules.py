#!/usr/bin/env python3
"""
Final HOMO-LUMO Gap Optimized Molecules from Adversarial Design Sessions
=========================================================================

Contains the top ~5 recommended molecules from each session:
- Gemini-led session (with Claude as adversary)
- GPT 5.2-led session (with Claude as adversary)
"""

# ============================================================================
# GEMINI-LED SESSION - Top 5 Molecules
# Source: results/HL/GEMINI_FIRST/adversary_design_2026-03-30_08-02-50.md
# Best validated result: 0.8579 eV
# ============================================================================

gemini_smiles = [
    # 1. Octacene-5-S([NH3+])-1-NO2 (0.8579 eV) - Best validated
    'c1c(S([NH3+]))c2c(S([NH3+]))c3c(S([NH3+]))c4c([N+](=O)[O-])c5c(S([NH3+]))c6c(S([NH3+]))c7ccccc7cc6cc5cc4cc3cc2cc1',
    # 2. Tetracyano-octacene (0.95-1.10 eV)
    'c1ccc2cc3cc4c(C#N)c5c(C#N)c6c(C#N)c7c(C#N)c8ccccc8cc7cc6cc5cc4cc3cc2c1',
    # 3. Tetracyano-decacene (0.65-0.80 eV estimated)
    'c1ccc2cc3cc4cc5c(C#N)c6c(C#N)c7c(C#N)c8c(C#N)cc9cc%10ccccc%10cc9cc8cc7cc6cc5cc4cc3cc2c1',
    # 4. Tetraaza-decacene-tetracyano (0.50-0.65 eV estimated)
    'c1ccc2cc3nc4cc5c(C#N)c6c(C#N)c7c(C#N)c8c(C#N)cc9cc%10ccccc%10cc9cc8nc7cc6cc5nc4cc3cc2c1',
    # 5. Octacene-6-S([NH3+]) central (0.80-0.90 eV)
    'c1c(S([NH3+]))c2c(S([NH3+]))c3c(S([NH3+]))c4c(S([NH3+]))c5c(S([NH3+]))c6c(S([NH3+]))c7ccccc7cc6cc5cc4cc3cc2cc1',
]

# ============================================================================
# GPT 5.2-LED SESSION - Top 5 Molecules
# Source: results/HL/GPT_FIRST/adversary_design_2026-03-25_09-16-49.md
# Best result: 3.95 eV
# ============================================================================

gpt_smiles = [
    # 1. No-ester, 5 nitrile-alkynes (3.95 eV) - Best practical
    'c1(C#CC#N)ccc2c(C#C(C#N))c3c(C#C(C#N))cc(C#CC#N)c(C#CC#N)c3c(C#Cc7ccc8cc9ccccc9cc8c7)c2c1',
    # 2. Constrained growth with 4 nitrile-alkynes (4.04 eV)
    'c1(C#CC(=O)OC)ccc2c(C#C(C#N))c3c(C#C(C#N))cc(C#CC#N)c(C#CC#N)c3c(C#Cc7ccc8cc9ccccc9cc8c7)c2c1',
    # 3. Dual nitrile-alkyne optimized (4.55 eV)
    'c1(C#CC(=O)OC)ccc2c(C#C(OC(=O)C))c3ccc(C#CC#N)c(C#CC#N)c3c(C#Cc7ccc8cc9ccccc9cc8c7)c2c1',
    # 4. Single nitrile baseline (4.73 eV)
    'c1(C#CC(=O)OC)ccc2c(C#C(OC(=O)C))c3ccc(C#CC#N)cc3c(C#Cc7ccc8cc9ccccc9cc8c7)c2c1',
    # 5. Phenanthrene-linked baseline (4.94 eV)
    'c1(C#CC(=O)OC)ccc2c(C#C(OC(=O)C))c3ccccc3c(C#Cc7ccc8cc9ccccc9cc8c7)c2c1',
]

# ============================================================================
# COMBINED DICTIONARY
# ============================================================================

hl_molecules = {
    'gemini_smiles': gemini_smiles,
    'gpt_smiles': gpt_smiles,
}

# ============================================================================
# MAIN - Print summary when run directly
# ============================================================================

if __name__ == "__main__":
    print("HOMO-LUMO Gap Optimized Molecules")
    print("=" * 50)
    
    print("\nGemini Session (best: 0.8579 eV):")
    for i, smi in enumerate(gemini_smiles, 1):
        print(f"  {i}. {smi[:60]}...")
    
    print("\nGPT 5.2 Session (best: 3.95 eV):")
    for i, smi in enumerate(gpt_smiles, 1):
        print(f"  {i}. {smi[:60]}...")
