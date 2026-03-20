# Molecular Property Optimization

An **AI-driven framework for iterative drug molecule design** that combines LLM-powered multi-agent reasoning with computational chemistry tools to discover optimized bioactive compounds.

![License](https://img.shields.io/badge/License-MIT-blue.svg)
![Python](https://img.shields.io/badge/Python-3.8+-green.svg)

---

## 🎯 Overview

This project leverages **large language models (LLMs)** to intelligently design better drug molecules by:

1. **Analyzing molecular trends** — Understanding what chemical features drive binding affinity and drug-likeness
2. **Proposing new molecules** — Using LLM reasoning to suggest targeted chemical modifications
3. **Scoring & validation** — Computing docking scores (protein-ligand binding affinity) and ADME properties
4. **Iterative refinement** — Cycling through rounds of design, evaluation, and improvement

The system supports **adversarial design** where multiple LLMs debate and validate proposals, enabling robust molecule discovery with reduced false positives.

---

## 🏗️ Project Structure

```
MolecularPropertyOptimization/
├── README.md                          # This file
├── LICENSE                            # MIT License
├── code/                              # Core functionality
│   ├── MolPropOp.py                  # Main optimization engine & cycle functions
│   ├── app.py                         # Gradio web interface & LangChain agent
│   ├── docking_module.py              # Protein-ligand binding affinity scoring
│   ├── lipinski_module.py             # Drug-likeness properties (QED, LogP, etc.)
│   ├── adversarial_design.py          # Multi-agent debate framework
│   ├── required.txt                   # Python dependencies
│   └── *.ipynb                        # Jupyter notebooks for exploration
│
├── data/                              # Molecular datasets & benchmarks
│   ├── input_set.md                   # Initial molecule screening data
│   ├── HMGCR_input_set.md             # HMGCR target benchmark
│   ├── maob_input_set.md              # MAOB target benchmark
│   ├── model_replies.md               # LLM responses from design sessions
│   └── *.py                           # Data extraction & processing scripts
│
├── results/                           # Design session outputs
│   ├── ANT_FIRST/                     # Anthropic Claude design session
│   ├── GPT_FIRST/                     # OpenAI GPT design session
│   ├── molecule_images/               # 2D structure visualizations
│   ├── molecular_structures/          # 3D structure files
│   └── DESIGN_SESSION_ANALYSIS.md     # Summary of design outcomes
│
├── agent_analysis_code/               # Post-analysis & visualization
│   ├── generate_molecule_images.py    # RDKit structure rendering
│   └── *.py                           # Analysis utilities
│
└── .venv/                             # Python virtual environment
```

---

## 🔧 Core Components

### 1. **Optimization Engine** (`MolPropOp.py`)

Provides three main operations for molecular exploration:

- **`grow_cycle(smiles, substituents, num_items)`** — Add functional groups to strategic positions
- **`replace_groups(smiles, mapping)`** — Swap chemical groups (e.g., tBu → OCF₃)
- **`make_random_list(count, base_smiles)`** — Generate random structural variants

All operations maintain validity using RDKit and sanitization checks.

### 2. **Scoring Functions**

#### Docking Module (`docking_module.py`)
- Computes **binding affinity** via molecular docking (using `dockstring`)
- Returns docking score (kcal/mol, lower = better binding)
- Supports multiple protein targets (DRD2, HMGCR, MAOB, etc.)

#### Lipinski Module (`lipinski_module.py`)
- Calculates **drug-likeness properties**:
  - LogP (lipophilicity)
  - Molecular weight (MW)
  - Hydrogen bond donors/acceptors (HBD/HBA)
  - Topological polar surface area (PSA)
  - QED (quantitative estimate of drug-likeness)
- Flags Lipinski violations for ADME risk assessment

### 3. **LLM Integration** (`app.py`)

Built with **LangChain** and **LangGraph** for multi-step agentic reasoning:

- **LLM Agent** — GPT-4 or Claude (configurable)
- **Tool Binding** — Calls grow_cycle, replace_groups dynamically
- **State Management** — Tracks conversation history & molecular evolution
- **Web Interface** — Gradio-based UI for interactive design sessions

### 4. **Adversarial Framework** (`adversarial_design.py`)

Enables **debate-driven design**:

- **Model Node** — Proposes new molecules based on trend analysis
- **Adversary Node** — Critiques proposals, flags risks
- **Multiple LLMs** — Different providers debate strengths/weaknesses
- **Convergence** — Refinement until high-confidence leads emerge

---

## 🧪 How It Works

### Typical Design Cycle

```
1. Input Screening Data
   (↓ Initial molecules + docking scores)

2. Trend Analysis
   LLM reads scores → identifies SAR (structure-activity relationships)
   "Lower docking scores correlate with aromatic rings + tBu groups"

3. Propose Modifications
   (↓ grow_cycle / replace_groups suggestions)

4. Score New Molecules
   Docking + Lipinski properties calculated for each proposal

5. Adversarial Review
   ├─ Model: "These 5 candidates look promising"
   ├─ Adversary: "Risk #1 has poor LogP; #3 may be metabolically unstable"
   └─ Refined Set: Champion molecules selected

6. Iterate
   (↓ Repeat with best molecules as seed set)
```

---

## 📊 Results & Key Findings

### Recent Design Sessions

#### **GPT-First Session (2026-03-20)**
- **Target:** Chromone-based HMGCR inhibitors
- **Best Affinity:** -9.2 kcal/mol (tBu variant)
- **Optimized Lead:** -9.1 kcal/mol @ LogP 3.69 (OCF₃ bioisostere)
- **Key Insight:** Ether linker + halogenated groups preserve binding while improving drug-likeness
- **Deliverables:** [Detailed analysis with embedded structures](results/GPT_FIRST/TURN_BY_TURN_ANALYSIS_WITH_STRUCTURES.md)

#### **ANT-First Session**
- **Target:** Multiple protein targets (DRD2, MAOB)
- **Outcomes:** [Comprehensive SAR summary](results/ANT_FIRST/)
- **Highlights:** Adversarial feedback improved lead selection accuracy

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- RDKit
- OpenAI API key (for GPT models) or Anthropic API key
- dockstring (for docking scoring)

### Installation

```bash
# Clone repository
git clone https://github.com/MauricioCafiero/MolecularPropertyOptimization.git
cd MolecularPropertyOptimization

# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r code/requirements.txt

# Set up API keys
export OPENAI_API_KEY="your-key-here"
export ANTHROPIC_API_KEY="your-key-here"  # If using Claude
```

### Running a Design Session

#### Interactive Web UI (Gradio)
```bash
cd code
python app.py
# Opens at http://localhost:7860
```

#### Command-Line Design
```python
from MolPropOp import grow_cycle, replace_groups
from docking_module import scoring_function

# Suggest new molecules
new_molecules = grow_cycle(
    smiles="c1ccc2cc(C(=O)O)ccc2c1",
    substituents=["F", "Cl", "Br"],
    num_items=5
)

# Score them
for smi in new_molecules:
    affinity, _ = scoring_function(smi)
    print(f"{smi} → {affinity:.2f} kcal/mol")
```

---

## 🔬 Detailed Guides

### Using the Optimization Engine

- **[Grow Cycle Guide](code/MolPropOp.py)** — Add substituents at strategic positions
- **[Replace Groups Guide](code/MolPropOp.py)** — Bioisostere exploration
- **[Scoring Functions](code/docking_module.py)** — Binding affinity & ADME properties

### Design Session Analysis

- **[Executive Summary](results/GPT_FIRST/EXECUTIVE_SUMMARY_2026-03-20.md)** — Quick decision summary
- **[Full SAR Analysis](results/GPT_FIRST/SAR_SUMMARY_2026-03-20.md)** — Chemistry & synthesis routes
- **[Turn-by-Turn Breakdown](results/GPT_FIRST/TURN_BY_TURN_ANALYSIS_WITH_STRUCTURES.md)** — With embedded molecule structures
- **[Complete Design Session](results/GPT_FIRST/DESIGN_SESSION_ANALYSIS_2026-03-20.md)** — Full methodology & data tables

### Data & Benchmarks

- **[Input Datasets](data/HMGCR_input_set.md)** — Screening data for various targets
- **[Molecular Sets](data/sets.md)** — Curated molecule databases

---

## 🛠️ Configuration

### Switching Scoring Functions

Edit `code/app.py` or `code/MolPropOp.py` to select scoring:

```python
# Use docking (protein-specific)
from docking_module import scoring_function

# Or use Lipinski properties (target-agnostic)
from lipinski_module import scoring_function

# Or create custom scoring function
def my_scoring_function(smiles: str):
    # Your logic here
    return score, auxiliary_data
```

### Selecting LLM Providers

```python
from langchain_openai.chat_models import ChatOpenAI
from langchain_anthropic import ChatAnthropic

# OpenAI GPT
model = ChatOpenAI(model_name="gpt-4", api_key=openai_key)

# Anthropic Claude
model = ChatAnthropic(model_name="claude-3-opus", api_key=anthropic_key)

# Local LLM via Ollama
from OllamaMolPropOp import model  # Uses local Ollama instance
```

---

## 📈 Key Features

✅ **Automated Molecular Design** — LLM-driven structure optimization  
✅ **Multi-Target Support** — DRD2, HMGCR, MAOB, custom proteins  
✅ **Adversarial Validation** — LLM debate reduces false positives  
✅ **Drug-Likeness Filtering** — Lipinski rules, QED, LogP assessment  
✅ **Molecule Visualization** — Embedded 2D/3D structure rendering  
✅ **Reproducible Workflows** — Complete session logs & analysis  
✅ **Scalable Design** — Parallel molecule testing, batch operations  

---

## 🔍 Example Use Cases

### 1. Lead Generation
Start with a known active scaffold; use `grow_cycle` to explore nearby chemical space.

### 2. SAR Exploration
Systematic `replace_groups` to map structure-activity relationships.

### 3. ADME Optimization
Use Lipinski module to balance binding affinity with drug-likeness.

### 4. Multi-Target Design
Run parallel design sessions against different proteins; use adversarial framework to identify common pharmacophores.

---

## 📚 Publications & References

- **RDKit:** Landrum, G. (2016). RDKit: Open-source cheminformatics. http://www.rdkit.org
- **Docking:** Via dockstring library; supports VINA, Smina backends
- **LLM Tools:** LangChain, LangGraph for agent orchestration
- **Molecular Scoring:** QED (Bickerton et al., 2012); Lipinski (Lipinski et al., 2001)

---

## 🤝 Contributing

Contributions welcome! Areas for expansion:

- **Additional scoring functions** (QSAR models, ML-based fitness)
- **More molecular operations** (linker optimization, scaffold hopping)
- **Multi-objective optimization** (Pareto frontier analysis)
- **Experimental validation** (integration with lab robotics)
- **Case studies** (publication of designed & synthesized compounds)

---

## ⚠️ Disclaimer

This tool is designed for **research and educational purposes**. While molecules are computationally optimized for binding, they must be:

1. **Synthesized** to confirm experimental validity
2. **Experimentally validated** (cell assays, enzyme kinetics, PK/PD)
3. **Toxicity-tested** before any therapeutic development
4. **Reviewed by medicinal chemists** for synthetic feasibility & off-target risks

Docking scores are estimates; real-world binding may differ significantly.

---

## 📝 License

MIT License © 2026 Mauricio Cafiero

See [LICENSE](LICENSE) for details.

---

## 📧 Contact & Support

- **Issues & Discussions:** [GitHub Issues](https://github.com/MauricioCafiero/MolecularPropertyOptimization/issues)
- **Author:** Mauricio Cafiero

---

## 🎓 Quick Start Checklist

- [ ] Install dependencies (`pip install -r code/requirements.txt`)
- [ ] Set API keys (OpenAI/Anthropic)
- [ ] Review example molecules in `/data/`
- [ ] Run `python code/app.py` for interactive design
- [ ] Check `/results/GPT_FIRST/` for design session examples
- [ ] Read [design session analysis](results/GPT_FIRST/TURN_BY_TURN_ANALYSIS_WITH_STRUCTURES.md) for methodology

---

**Status:** Active development | Latest design session: 2026-03-20 | Local optimization at -9.2 kcal/mol ✅
