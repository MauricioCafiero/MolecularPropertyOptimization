# Fragment-based, AI-assisted Optimization of molecular properties (FAO-MOL)

## Minimization of docking scores for HMGCR calculated by AutoDock Vina

#### Table 1. Docking Scores (kcal/mol) for zero shot molecules for each model tested. 

| Model | No. Mols | Low | High | Ave |
|-------|:-:|:-:|:-:|---|
| GPT 5.2  | 5 | -7.70 | -6.70 | -7.18 |
| Claude   | 3 | -8.30 | -6.40 | -7.20 |
| Gemini   | 2 | -8.10 | -7.90 | -8.00 |
||||||
| Deepseek V3.1  | 4 | -7.40 | -7.00 | -7.13 |
| GPT OSS 120B   | 5 | -7.40 | -6.10 | -6.74 | 
| GPT OSS 20B    | 4 | -6.90 | -6.00 | -6.43 |
| Devstral 2     | 5 | -7.20 | -6.70 | -6.92 |
| Cogito 2.1     | 5 | -8.00 | -6.90 | -7.4 |
| Nemotron 3 Nano| 2 | -7.50 | -6.90 | -7.20 |
| Kimi K2        | 5 | -8.30 | -7.00 | -7.78 |

#### Table 2. Docking Scores (kcal/mol) for zero shot molecules with suggested fragments for each model tested. 

| Model | No. Mols | Low | High | Ave |
|-------|:-:|:-:|:-:|---|
| GPT 5.2  | 4 | -8.30 | -6.40 | -7.15 |
| Claude   | 5 | -8.10 | -6.40 | -7.46 |
| Gemini   | 4 | -8.50 | -7.80 | -8.13 |
||||||
| Deepseek V3.1  | 2 | -7.70 | -5.30 | -6.50 |
| GPT OSS 120B   | 4 | -6.70 | -5.80 | -6.15 | 
| GPT OSS 20B    | 2 | -7.60 | -6.30 | -6.94 |
| Devstral 2     | 5 | -8.30 | -6.50 | -7.12 |
| Cogito 2.1     | 4 | -7.00 | -6.70 | -6.88 |
| Nemotron 3 Nano| 0 | - | - | - |
| Kimi K2        | 5 | -7.40 | -6.10 | -6.76 |


#### Table 3. Docking Scores (kcal/mol) for one shot molecules for each model tested. The highest docking score given in the one-shot dataset was -8.6 kcal/mol.

| Model | No. Mols | Low | High | Ave |
|-------|:-:|:-:|:-:|---|
| GPT 5.2  | 5 | -8.90 | -7.20 | -7.82 |
| Claude   | 5 | -9.00 | -7.40 | -8.42 |
| Gemini   | 5 | -9.20 | -7.30 | -8.14 |
||||||
| Deepseek V3.1  | 4 | -8.20 | -7.50 | -7.80 |
| GPT OSS 120B   | 5 | -7.90 | -6.80 | -7.26 | 
| GPT OSS 20B    | 1 | -7.50 | -7.50 | -7.5 |
| Devstral 2     | 4 | -8.60 | -7.90 | -8.20 |
| Cogito 2.1     | 5 | -8.50 | -7.50 | -8.1 |
| Nemotron 3 Nano| 3 | -9.10 | -7.60 | -8.26 |
| Kimi K2        | 4 | -7.50 | -6.90 | -7.15 |


#### Table 4. Docking Scores (kcal/mol) for adversarially designed molecules for each model tested. The highest docking score given in the one-shot dataset was -8.6 kcal/mol.

| Model | Adversary |  No. Mols | Low | High | Ave |
|-------|:-:|:-:|:-:|:-:|---|
| GPT 5.2  | Claude  | 2 | -8.90 | -8.90 | -8.90 |
| Claude   | GPT 5.2 | 5 | -9.90 | -8.10 | -8.96 |
| Gemini   | Claude  | 5 | -9.10 | -8.90 | -8.98 |


#### Table 5. Docking Scores (kcal/mol) progression for zero-shot, one-shot, and adversarially designed molecules for each model tested. The highest docking score given in the one-shot dataset was -8.6 kcal/mol.

| Model | design mode | No. Mols | Low | High | Ave |
|-------|:-:|:-:|:-:|:-:|---|
| GPT 5.2  | zero-shot | 5 | -7.70 | -6.70 | -7.18 |
| GPT 5.2  | zero/frags| 4 | -8.30 | -6.40 | -7.15 |
| GPT 5.2  | one-shot  | 5 | -8.90 | -7.20 | -7.82 |
| GPT 5.2  | w/ Claude | 2 | -8.90 | -8.90 | -8.90 |
||||||
| Claude   | zero-shot | 3 | -8.30 | -6.40 | -7.20 |
| Claude   | zero/frags| 5 | -8.10 | -6.40 | -7.46 |
| Claude   | one-shot  | 5 | -9.00 | -7.40 | -8.42 |
| Claude   | w/ GPT 5.2| 5 | -9.90 | -8.10 | -8.96 |
||||||
| Gemini   | zero-shot | 2 | -8.10 | -7.90 | -8.00 |
| Gemini   | zero/frags| 4 | -8.50 | -7.80 | -8.13 |
| Gemini   | one-shot  | 5 | -9.20 | -7.30 | -8.14 |
| Gemini   | w/ Claude | 5 | -9.10 | -8.90 | -8.98 |

### Lipinski properties for AI-designed molecules

## Minimization of the HOMO-LUMO gap as calculated with CAM-B3LYP/sto-3g in PySCF. Molecule structures optimized with MMFF.

#### Table 6. HOMO-LUMO gaps (eV) for zero shot molecules for each model tested. 

| Model | No. Mols | High | Low | Ave |
|-------|:-:|:-:|:-:|---|
| GPT 5.2  | 5 | 7.57 | 5.04 | 6.17 |
| Claude   | 5 | 8.62 | 2.75 | 5.75 |
| Gemini   | 3 | 4.23 | 3.42 | 3.75 |
||||||
| Deepseek V3.1  | 3 | 9.31 | 3.42 | 6.32 |
| GPT OSS 120B   | 3 | 6.91 | 2.21 | 4.12 | 
| GPT OSS 20B    | 2 | 6.51 | 5.75 | 6.12 |
| Devstral 2     | 2 | 5.58 | 4.62 | 5.10 |
| Cogito 2.1     | 5 | 7.77 | 5.84 | 6.54 |
| Nemotron 3 Nano| 0 | - | - | - |
| Kimi K2        | 4 | 5.00 | 3.79 | 4.50 |


#### Table 7. HOMO-LUMO gaps (eV) for zero shot molecules with suggested fragments for each model tested.

| Model | No. Mols | High | Low | Ave |
|-------|:-:|:-:|:-:|---|
| GPT 5.2  | 5 | 7.03 | 5.76 | 6.19 |
| Claude   | 4 | 7.62 | 5.94 | 7.11 |
| Gemini   | 5 | 7.26 | 5.37 | 6.10 |
||||||
| Deepseek V3.1  | 4 | 7.53 | 5.69 | 6.47 |
| GPT OSS 120B   | 2 | 7.25 | 6.68 | 6.97 | 
| GPT OSS 20B    | 4 | 7.67 | 5.78 | 6.66 |
| Devstral 2     | 2 | 7.03 | 5.89 | 6.46 |
| Cogito 2.1     | 4 | 7.14 | 6.66 | 6.87 |
| Nemotron 3 Nano| 0 | - | - | - |
| Kimi K2        | 4 | 7.32 | 5.78 | 6.35 |


#### Table 8. HOMO-LUMO gaps (eV) for one shot molecules for each model tested. The lowest HOMO-LUMO gap given in the one-shot dataset was 5.579 eV.

| Model | No. Mols | High | Low | Ave |
|-------|:-:|:-:|:-:|---|
| GPT 5.2  | 1 | 7.08 | 7.08 | 7.08 |
| Claude   | 4 | 7.34 | 2.46 | 5.95 |
| Gemini   | 5 | 5.95 | 4.26 | 5.26 |
||||||
| Deepseek V3.1  | 1 | 3.46 | 3.46 | 3.46 |
| GPT OSS 120B   | 0 | - | - | - | 
| GPT OSS 20B    | 4 | 7.55 | 4.76 | 6.27 |
| Devstral 2     | 3 | 5.92 | 5.82 | 5.87 |
| Cogito 2.1     | 2 | 7.57 | 3.48 | 5.53 |
| Nemotron 3 Nano| 1 | 9.50 | 9.50 | 9.50 |
| Kimi K2        | 5 | 7.52 | 5.69 | 6.10 |


#### Table 9. HOMO-LUMO gaps (eV) for adversarially designed molecules for each model tested. TThe lowest HOMO-LUMO gap given in the one-shot dataset was 5.579 eV.
/*correction for the SMILES error in the Claude session.

| Model | Adversary |  No. Mols | High | Low | Ave |
|-------|:-:|:-:|:-:|:-:|---|
| GPT 5.2  | Claude  | 3 | 3.95 | 3.91 | 3.93 |
| Claude   | GPT 5.2 | 3 | 3.10 | 2.98 | 3.06 |
| Claude*   | GPT 5.2 | 3 | 6.49 | 6.03 | 6.28 |
| Gemini   | Claude  | 2 | 1.49 | 1.39 | 1.44 |


#### Table 10. HOMO-LUMO gap (eV) progression for zero-shot, 
one-shot, and adversarially designed molecules for each model tested. The lowest HOMO-LUMO gap given in the one-shot dataset was 5.579 eV.

| Model | design mode | No. Mols | High | Low | Ave |
|-------|:-:|:-:|:-:|:-:|---|
| GPT 5.2  | zero-shot | 5 | 7.57 | 5.04 | 6.17 |
| GPT 5.2  | zero/frags| 5 | 7.03 | 5.76 | 6.19 |
| GPT 5.2  | one-shot  | 1 | 7.08 | 7.08 | 7.08 |
| GPT 5.2  | w/ Claude | 3 | 3.95 | 3.91 | 3.93 |
||||||
| Claude   | zero-shot | 5 | 8.62 | 2.75 | 5.75 |
| Claude   | zero/frags| 4 | 7.62 | 5.94 | 7.11 |
| Claude   | one-shot  | 4 | 7.34 | 2.46 | 5.95 |
| Claude   | w/ GPT 5.2| 3 | 3.10 | 2.98 | 3.06 |
||||||
| Gemini   | zero-shot | 3 | 4.23 | 3.42 | 3.75 |
| Gemini   | zero/frags| 5 | 7.26 | 5.37 | 6.10 |
| Gemini   | one-shot  | 5 | 5.95 | 4.26 | 5.26 |
| Gemini   | w/ Claude | 2 | 1.49 | 1.39 | 1.44 |

