# Molecular Property Optimization (FAO-MOLPROP)

A **fragment-based, AI-assisted framework for molecular property optimization** that combines tool-augmented LLMs with computational chemistry to design optimized molecules without model fine-tuning.

![License](https://img.shields.io/badge/License-MIT-blue.svg)
![Python](https://img.shields.io/badge/Python-3.8+-green.svg)

---

## 🎯 Overview

This project demonstrates a modular workflow for molecular design using **10 different LLMs** (3 closed-weight, 7 open-weight) across multiple design paradigms:

1. **Fragment-based design** — User-specified scaffolds and substituents create a flexible design space
2. **Tool-augmented reasoning** — LLMs access computational chemistry tools (docking, HOMO-LUMO gap, Lipinski properties, SAS/NP scores)
3. **Multiple design modes** — Zero-shot, one-shot, and adversarial design with iterative refinement
4. **Multi-objective optimization** — Balance binding affinity, drug-likeness, synthetic accessibility, and binding site localization
5. **Generality** — Successfully demonstrated for docking score minimization (HMGCR inhibitors) and HOMO-LUMO gap minimization

The framework supports **adversarial design** where two LLMs debate and validate proposals, achieving superior results compared to zero/one-shot approaches and fine-tuned models.

---

## 🏗️ Project Structure

```
MolecularPropertyOptimization/
├── README.md                          # This file
├── LICENSE                            # MIT License
├── requirements.txt                   # Python dependencies
├── code/                              # Core functionality & design scripts
│   ├── MolPropOp.py                  # Fragment manipulation (grow, replace, substitute)
│   ├── docking_module.py              # AutoDock Vina scoring via DockString
│   ├── HL_gap_module.py               # HOMO-LUMO gap calculations (PySCF)
│   ├── lipinski_module.py             # Drug-likeness (QED, aLogP, MW, etc.)
│   ├── all_mol_lists.py               # Generated molecule SMILES collections
│   ├── set_up_database.py             # SQLite database management
|   ├── query_database.py              # Script to extract data from SQLite database
│   ├── insert_qed_alogp.py            # Database population utilities
│   ├── GPT_ANT_*.py                   # Adversarial design scripts (GPT/Claude)
│   ├── Ollama_*.py                    # Open-weight model design scripts
│   ├── dock_*.py                      # Docking verification & analysis
│   ├── HL_*.py                        # HOMO-LUMO verification & analysis
│   ├── *_finalist_images.py           # Molecule visualization generators
│   └── *.ipynb                        # Jupyter notebooks for exploration
│
├── data/                              # Input datasets & database
│   ├── gen_molecules.db               # SQLite: SMILES, scores, properties
│   ├── HMGCR_input_set.md             # HMGCR docking initial dataset
│   ├── HL_initial_data.txt            # HOMO-LUMO gap initial dataset
│   └── model_replies.md               # LLM conversation logs
│
├── results/                           # Design session outputs
│   ├── ZERO_SHOT/                     # Zero-shot design results
│   ├── ONE_SHOT/                      # One-shot design results
│   ├── FRAGMENTS/                     # Zero-shot with fragment suggestions
│   ├── HL/                            # HOMO-LUMO gap results
│   ├── SAS_NP_all.txt                 # Synthetic accessibility scores
│   ├── lipinski_results_all.txt       # QED/aLogP for all molecules
│   └── dock_finalist_images/          # Final candidate visualizations
│
├── paper/                             # Manuscript & documentation
│   └── supporting_data.md             # Supporting information
│
├── poses/                             # Docking pose images & PDB files
│   └── *.jpg, *.pdb                   # PyMOL-rendered binding poses
│
└── tables/                            # Summary data & figures
    └── summary_tables_images.md       # Figure collection
```

---

## 🔧 Core Components

### 1. **Fragment Manipulation Engine** (`MolPropOp.py`)

Provides three main operations for molecular exploration:

- **`substitute(smiles, substituents, positions)`** — Add substituents to specified positions on scaffolds
- **`grow_cycle(smiles, substituents, positions)`** — Grow molecules by adding functional groups
- **`replace_groups(smiles, old_group, new_groups)`** — Swap chemical groups systematically

All operations maintain validity using RDKit sanitization and SMILES verification.

### 2. **Scoring  and Auxilliary Functions**

#### Docking Module (`docking_module.py`)
- Computes **binding affinity** via AutoDock Vina (through DockString)
- Returns docking score (kcal/mol, lower = better binding)
- Supports HMGCR target from DUD-E database
- Automated ligand preparation (protonation, conformer generation, MMFF94 optimization)

#### HOMO-LUMO Gap Module (`HL_gap_module.py`)
- Calculates **frontier orbital energy gaps** using PySCF
- CAM-B3LYP/sto-3g level of theory
- 3D structure generation with RDKit ETKDG
- Returns gap in eV (lower = better for optoelectronic applications)

#### Lipinski Module (`lipinski_module.py`)
- Calculates **drug-likeness properties**:
  - aLogP (lipophilicity)
  - QED (quantitative estimate of drug-likeness)
  - Molecular weight (MW)
  - Hydrogen bond donors/acceptors (HBD/HBA)
  - Topological polar surface area (PSA)
- Flags Lipinski violations for ADME risk assessment

#### Synthetic Accessibility (`test_SAS_NP.py`)
- **SAS scores** — Synthetic Accessibility Score (1-10, lower = easier)
- **NP scores** — Natural Product-likeness

### 3. **LLM Integration**

Built with **LangChain** and **LangGraph** for multi-step agentic reasoning:

- **10 LLMs tested**:
  - Closed-weight: GPT 5.2, Claude 4.5 Haiku, Gemini 3 Flash
  - Open-weight: DeepSeek V3.1, GPT-OSS-120B/20B, Devstral-2, Cogito-2.1, Nemotron-3-Nano, Kimi-K2.5
- **Tool Binding** — Dynamic access to all scoring and manipulation functions
- **State Management** — Conversation history tracked through message lists
- **Ollama Integration** — Local hosting of open-weight models

### 4. **Adversarial Framework**

Enables **debate-driven design** between two LLMs:

- **Primary Model** — Analyzes data, proposes molecules, uses tools
- **Adversary Model** — Critiques proposals, suggests improvements, validates reasoning
- **Iterative Refinement** — Multi-turn conversations until convergence
- **Three Generations**:
  - Gen 1: Basic adversarial with docking/Lipinski tools
  - Gen 2: (Reserved for future development)
  - Gen 3: Added binding site analysis and SAS/NP scoring

---

## 🧪 How It Works

### Fragment-Based Design Cycle

```
1. Define Fragments
   9 scaffolds (benzene, pyridine, furan, naphthalene, anthracene, etc.)
   567 substituents (11 EWG + 16 EDG + 14 linkers)
   → 14,742+ unique singly-substituted molecules possible

2. Initial Dataset Generation
   Random selection of 10 substituents added to all attachment points
   → 260 molecules scored with target function

3. LLM Analysis & Design
   ├─ Zero-shot: Generate molecules without examples
   ├─ Zero-shot + Fragments: With suggested scaffolds/substituents
   ├─ One-shot: Given initial 260 scored molecules
   └─ Adversarial: Iterative debate between two LLMs

4. Tool-Augmented Refinement
   LLM uses tools to:
   ├─ Calculate scores (docking, HOMO-LUMO gap)
   ├─ Check drug-likeness (Lipinski, QED, aLogP)
   ├─ Verify binding site location
   ├─ Assess synthetic accessibility (SAS)
   └─ Query PubChem for related structures

5. Validation & Selection
   ├─ Primary model proposes 5 lead molecules
   ├─ Adversary critiques and suggests improvements
   ├─ Iterate until convergence
   └─ Verify all final molecules computationally

6. Results Analysis
   All SMILES verified with same scoring functions
   Comparison to known benchmarks (e.g., statins for HMGCR)
   Visualization of structures and docking poses
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- RDKit
- PySCF (for HOMO-LUMO gap calculations)
- OpenAI API key (for GPT models)
- Anthropic API key (for Claude models)
- Google API key (for Gemini models)
- Ollama (for open-weight models - optional)
- DockString (for docking scoring)

### Installation

```bash
# Clone repository
git clone https://github.com/MauricioCafiero/MolecularPropertyOptimization.git
cd MolecularPropertyOptimization

# Create virtual environment
python -m venv .venv
.venv\Scripts\activate  # On Windows
# source .venv/bin/activate  # On Linux/Mac

# Install dependencies
pip install -r requirements.txt

# Set up API keys (Windows PowerShell)
$env:OPENAI_API_KEY="your-openai-key-here"
$env:ANTHROPIC_API_KEY="your-anthropic-key-here"
$env:GOOGLE_API_KEY="your-google-key-here"

# For Ollama (open-weight models)
# Download and install from https://ollama.com/
# Pull desired models: ollama pull deepseek-v3.1
```

### Running a Design Session

```python
# See example notebooks in code/ folder:
# - gen_design.ipynb: Main adversarial design workflow
# - Ollama_MolOpt.ipynb: Open-weight model design
# - Agent_demo.ipynb: Single-agent tool calling examples

# Or run scripts directly:
python code/GPT_ANT_ONE_SHOT.py  # GPT vs Claude adversarial (one-shot)
python code/Ollama_OneShot.py    # Open-weight model one-shot design
```

## 📈 Key Features

✅ **Fragment-Based Design** — User-controlled scaffolds and substituents  
✅ **10 LLM Comparison** — 3 closed-weight + 7 open-weight models tested  
✅ **Multiple Design Modes** — Zero-shot, one-shot, adversarial with tool access  
✅ **Dual Optimization Tasks** — HMGCR docking (-9.90 kcal/mol best) and HOMO-LUMO gaps (1.39 eV best)  
✅ **Multi-Objective Balancing** — Score, QED, aLogP, SAS, binding site localization  
✅ **No Fine-Tuning Required** — Frontier LLMs perform chemistry tasks with general weights  
✅ **Tool Integration** — Docking, DFT, Lipinski, SAS/NP, binding site analysis, PubChem queries  
✅ **Comprehensive Documentation** — Full manuscript, supporting data, and conclusions provided  
✅ **Database Management** — SQLite storage of all molecules and properties  
✅ **Visualization** — Automated 2D structure and 3D docking pose generation

---

## 📚 References

### Software & Tools
- **RDKit** — Landrum, G. (2024). RDKit: Open-source cheminformatics. http://www.rdkit.org
- **DockString** — García-Ortegón et al. (2022). J. Chem. Inf. Model. 62, 3486–3502
- **AutoDock Vina** — Trott & Olson (2010). J. Comput. Chem. 31, 455–461
- **PySCF** — Sun et al. (2020). J. Chem. Phys. 153, 024109
- **LangChain/LangGraph** — LangChain Inc. (2024). Multi-step agentic reasoning framework
- **Ollama** — Ollama (2024). Local LLM hosting platform

### LLMs Tested
- **Closed-weight**: GPT 5.2 (OpenAI), Claude 4.5 Haiku (Anthropic), Gemini 3 Flash (Google)
- **Open-weight**: DeepSeek V3.1, GPT-OSS-120B/20B, Devstral-2, Cogito-2.1, Nemotron-3-Nano, Kimi-K2.5

### Related Work
- **ChemCrow** — Bran et al. (2023). LLM agents for chemistry
- **SmileyLlama** — Cavanagh et al. (2024). Fine-tuned LLMs for molecular design
- **PharmAgents** — Gao et al. (2025). Multi-LLM drug discovery workflow

---
## 📝 License

MIT License © 2026 Mauricio Cafiero

See [LICENSE](LICENSE) for details.

---

## 📧 Contact & Support

- **Issues & Discussions:** [GitHub Issues](https://github.com/MauricioCafiero/MolecularPropertyOptimization/issues)
- **Author:** Mauricio Cafiero

---

**Status:** Published research | Latest session: June 2026 | Best HMGCR docking: -9.90 kcal/mol (Claude) | Best HOMO-LUMO gap: 1.39 eV (Gemini) ✅
