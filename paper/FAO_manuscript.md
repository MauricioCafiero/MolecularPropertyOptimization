# Fragment-based, AI-assisted Optimization of molecular properties (FAO-MOLPROP)

## Introduction

The work described here uses ten different open and closed-weight LLMs, augmented with tools, to optimize the properties of molecules for tasks which can be scored using a computational tool. In particular, we give two examples of property optimization: ligand docking scores and HOMO-LUMO gaps. 

As early as 2023, Bioko *et al* were using OpenAI's GPT 4 in their *Coscientist* to perform 'autonomous design, planning and performance of complex scientific experiments.<sup>1</sup> They used a harness and three LLM-based sub-agents to perform planning, document searching and web-searching tasks, and provided a Python coding environment to execute LLL-designed code. They found that GPT 4 could reason about chemical information well enough to perform many tasks, including synthesis planning. More relevant to this work, Zhang *et al* used GPT4 (and GPT 3.5) in molecule identification and optimization. In one trial, they used a zero-shot approach to ask the LLM to refine a molecule to have a particular QED (quantitative estimate of drug-likeness) value, and found that the model, while at times producing invalid SMILES strings, could reason well about attaining a particular QED and suggested four molecules, though none had the desried value.<sup>2</sup>  Rather than rely on an LLM directly, Wang *et al* used GPT 4 for help with three distinct tasks within  a drug-deisgn workflow: idea generation, concept clarification, and coding help. <sup>3</sup> At that time, GPT 4 provided inaccurate information both about molecules and in the concept clarification regime. Bran *et al* designed the ChemCrow agent (again based on GPT 4), which had access to some simple chemical tools (SMILES to Weight, Func Groups). <sup>4</sup>. They evaluated ChemCrow for several types of chemical tasks; for the molecule design tasks relevant to the current work, they use zero-shot design for two different design tasks. Since the authors did not provide validation or verification of the LLM generated molecules, it is difficult to tell how well the LLM performed on these tasks. 

In a very different use of LLMs for molecule design, Cavanagh *et al* fine-tuned the Llama 3.1 8B Instruct model on chemical information (SmileyLlama). <sup>5</sup> The fine-tuning prompts consisted of SMILES strings of 2M drug-like molecules from ChEMBL along with ADME data for each molecule calculated by RDKit. This fine tuning increased the model's ability to generate valid SMILES as well as molecules with desired properties, with the resulting SMILES similar in property distribution to the original training set. The authors further used a reinforcement learning-type approach to further train the model to generate molecules that would be good inhibitors of a particular enzyme. This aligned model could then generate novel SMILES that could be good inhibitors and adhere to other property requests. This approach uses AutoDock to provide data for the reinforcement learning, while the approach described in the current work uses AutoDock as a tool directly accessible to the foundation model LLM. 






This work makes use of fragment-based design of molecules. 

## Methods

### Fragment-based Molecular Optimization

The automated property optimization requires one or more scaffolds--in SMILES format, defined substitution points for 'clean' molecules (no substituents added), defined substitution points for substituted molecules, a set of substituents to add, a substitution function, a grow function, a replacement function, one or more scoring functions, any desired auxilliary functions (optional).
The workflow for the process begins by adding a random selection of the substituents to the 'clean' substitution points on all selected scaffolds using the substitution function. This set of molecules is then 'scored' by the scoring function. From this point, several paths can follow. A molecule with a promising score can be used with the grow function to add more/different substituents to try to improve the score, or the replacement function may be used on a promising molecule to see how different substituents would change the score. Additional scoring and auxilliary functions may be used to gain additional information on the molecules. These processes are then repeated until a best possible score is achieved. 

In this work, we used the following scaffolds: ```c1ccccc1``` (benzene), ```n1ccccc1``` (pyridine),```o1cccc1``` (furan), ```s1cccc1``` (thiophene), ```[nH]1cccc1``` (pyrrole), ```n1c[nH]cc1``` (imidazole), ```c1ccc2ccccc2c1``` (naphthalene), ```c1ccc2cc3ccccc3cc2c1``` (anthracene), and ```O=c1cc(-c2ccccc2)oc2ccccc12``` (flavone). In practice any set of molecule SMILES may be used as a scaffold. For substituents we used sets of 11 electron withdrawing groups, 16 electron donating groups and 14 linkers. The linkers can be combined with the other two groups, combined with each other, or used alone as substituents themselves. This results in 567 potential substituents. (see supporting information) In practice, we chose a random set of 10 substituents from the 567 available for the initial dataset created with the substitution function.

The clean subtitution points on the scaffolds are all attachment points that are symmetrically unique, i.e., benzene only has one unique attachment point, napthalene has two, anthracene has three, etc. Each of the 567 substituents can be placed on any clean attachment point; since the rings used in this work have a total of 26 attachment points, this results in a total of 14,742 unique molecules that may be generated in an automated fashion. Note that these are only the singly substituted molecules that can be generated by the substitution function--multiply substituted molecules may also be created when using the grow function on a promising molecules generated with the substitution function. In this work, the 10 randomly chosen substituents were added to all attachment points, for a a total of 260 molecules in the intial dataset.

The grow function adds any user-specified set of substituents to any molecules--ususally a promising molecule from the substitution function. The substituents are added in any user-defined locations. For this work, the location were: ```c[0-9]c```, ```1c\[n```, ```cc```, ```c\[nH\]``` (these a regular expression for SMILES notation). Note that these include any open position on an aromatic ring. The replacement function looks for a user-defined substituent offset in the SMILES string with () and replaces it with an of a user-defined set of substituents. All novel molecules generatd by the grow and replacement functions are scored used the scoring function. 

### Scoring and auxilliary functions

In this work, two scoring functions were tested: docking (using AutoDock Vina via DockString) and HOMO-LUMO gap (HLG) (using PySCF). The scoring functions take two inputs: a globally defined ```scoring_args``` variable and the SMILES string of the molecule in question. In this work, the ```scoring_args``` were the protein to dock in ('HMGCR') and the DFT functional to use for gap calculations ('cam-b3lyp'). Along with the scoring fuunction, a 'task specific prompt' is needed to describe the task to be accomlished--this serves as part of the system message for the LLM (see below). In this work, the task specific prompts requested minimzation of docking score and the HOMO-LUMO gap. Since the docking scoring function used the convenient DockString package, all protein preparation is done beforhand by the package authors, and ligand preparation was done on-the-fly by protonating it at a pH of 7.4 using Open Babel, generating a conformation using ETKG from RDKit, optimizing the structure with MMFF94, andcomputing charges for all atoms using Open Babel, all while maintaining any stereochemistry in the original SMILES string. The prepared molecule is then docked into the protein binding site using AutoDock Vina with default values of exhaustiveness, binding modes, and energy range. The prepared HMGCR binding site from the DUD-E database was used for docking. The HLG scoring function used RDKit to make 3D structures by adding protons, creating a conformer using ETKG from RDKit, and optimizing the structure with MMFF94. A CAM-B3LYP/sto-3g calculation was then performed with PySCF and the HOMO and LUMO energies were retrieved. Note that the small basis set used in this work was chosen to make the proof-of-concept calculations fast; each LLM adversarial turn could generate dozens of molecules and so quick calculations were required. In production, any basis set can be used according to the user's computational resources.  

Two auxiliary functions were provided in this work: a 'Lipinski' module and a 'related' module. The former usses RDKit to calculate the QED, aLogP, molecular weight, etc for a SMILES string, and the latter queries the PubChem API with the SMILES and searches for structurally similar molecules. 'Lipinski' is used to steer molecular design towards feasible drug molecules, and 'related' is used to either perform a 'sense check' on the strucutre, or to look for other scaffolds in nearby chemical space.   

### LLMs and Agents

Ten LLMs were used in this work. Seven open-weight (OW) models were used in zero- and one-shot molecule design, and three closed-weight (CW) frontier models were used in zero-shot, one-shot and agentic molecular design. The OW models (deepseek-v3.1:671b, gpt-oss:120b, gpt-oss:20b, devstral-2:123b, cogito-2.1:671b, nemotron-3-nano:30b, and kimi-k2:1t) were used via the Ollama API on the Ollama cloud. The models were chosen to provide a range of sizes from different labs. On the smaller side are OpenAI's gpt-oss and nemotron-3-nano with 20B and 30B parameters respectively; on the larger side are deepseek-v3.1, cogito-2.1 and kimi-k2 at 671B, 671B and 1T parameters. 

The CW models (GPT5.2, Claude Haiku 4.5 and Gemini 3 Flash) were used via the OpenAI, Anthropic and Google APIs. The models were chosen to represent the three most commonly used commercial LLMs. The specific models were chosen to be of similar, middle-of-the-road prices. 
OpenAI's GPT 5.3 had a cost of $1.75 per M input tokens and $14 per M output tokens at the time this work was performed; Claude Haiku had costs of $1 per M input and $5 per M output tokens, and Gemini 3 Flash had a cost of $0.50 per M input and $3 per M output tokens.

In order to give the CW models access to tools, LangGraph was used. The LangChain chat interfaces were used for each model and the add_tools method was employed. A simple graph was created for each model with a START node, a model call node, and and END node. Models could calls tools as often as they liked within the model call node. Models maintained state through a ```messages``` list, which included the system message (see below), Human messages and AI messages. Note that tool calling and tool response messages were not kept in the messages list. In this work, the first Human message was the set of input data for each task. Each subsequent Human messages was the response from the adversarial model (see below).

#### Zero-shot

Zero-shot molecule design was carried out in two ways: giving the models freedom to propose any molecule (zero-shot) and telling them the fragments used in the initial dataset and encourahging their use (zero-shot with fragment suggestions). The system prompt used for the zero-shot with fragment suggestions method for docking is shown in the supporting data. The prompt for the plain zero-shot method was the same, but included only the first paragraph, excluding the fragment suggestions. The first user message was 'HMGCR.' The system prompt for the HLG zero-shot design session is also shown in the supporting data, with the same midification for the zero-shot with no fragment suggestions. The first user message was 'cam-b3lyp.' Full model responses can be found in the Github repository. 

#### One-shot

One shot molecule design was carried out similary to the zero-shot design, but the first user message contained an initial dataset for docking or HLG generated with the substitution tool. The prompts for docking and HLG design are given in the supporting information. The initial datasets and full models responses are available in the Github repository. 

#### Adversarial design

In adversarial design, the first model is given the initial dataset made with the substitution tool and instructions to use the tools and that data to recommend molecles with the target scores. The output from that model is then passed directly to the adversary model, which is instructed to critique the suggestions and offer advice, corrections and suggestions. The system prompt for adversarial design contains tool descriptions and instructions for tool use, as well as information on the iterative processes, including the existance of the adversary model. The system prompt for the adversary model tells it that it is serving as an adversary and desribes the tools available to the other model so that it can suggest new experiments. The prompts are available in the supporting data, and the initial datasets and full models responses for tboth models are available in the Github repository. 

### Extracting data from the design sessions

At the end of each session, the models suggest up to five final molecules with the desired properties. For adversarial design, often the models have verified the scores (docking score, HLG) with the tools, but other times they offer 'estimates' of the scores. The SMILES for the final molecules were extracted from the model replies and verified with the same scoring functions (an auxilliary functions) used by the models. In zero and one-shot sessions, the SMILES suggested by the models do not complile into viable molecules; in the adversarial sessions, the models sometimes trim their suggestions to fewer than five molecules. Although the prompts include information on how to embed a new ring into an existing SMILES by using higher numbers (i.e., ```c6ccccc6``` rather than ```c1ccccc1```) so as to not conflict with existing rings, in the adversarial session, the Gemini model created molecules incorrected by embedding new rings with the same numbers as exiting rings. In this case both the original SMILES proposed by Gemini and the 'corrected' SMILES taht Gemini though it was creating were verified.

## Results: Minimization of docking scores for HMGCR calculated by AutoDock Vina

When prompted to generate inhibitors for HMGCR, the three CW models, DeepSeek and Kimi K2 produced variations on the standard Type II statin molecules, featuring the carboxy-diol pharmacophore structure in particular. The other OW models produced random drug-like molecules of approximately the correct size and polarity (See Figure 1, as well as Figures 1, 4, 7, 10, 13, 16, 19, 22, 25 and 27 in the supporting data). For the CW plus DeepSeek and Kimi-K2 (CWDK) models, Claude and Kimi-K2 had molecules with the the overall lowest docking score (-8.30, Table 1), though Kimi-K2 produced a higher QED (0.64 vs. 0.46 for Claude, Table 6). Gemini had the second lowest docking score (-8.10) and the lowest average score (-8.0), though it only produced two viable SMILES, had a lower QED (0.39) and a relatively high aLogP (4.39). GPT 5.2 produced molecules of average quality, and was outperformed by Cogito 2.1 in both Docking score, QED and aLogP (Table 7). GPT OSS 20 and 120 had the highest average scores of all models tested. 

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

<figure>
    <img src="../results/dock_finalist_images/ZERO_SHOT_finalists.png"
         alt="molecules">
    <figcaption>Figure 1. Lowest docking score zero-shot molecules for GPT 5.2, Claude and Gemini.</figcaption>
</figure>

When asked to generate HMGCR inhibitors and given a set of SMILES fragments to work with, the already well performing Claude maintained roughly the same docking scores (Table 2), while GPT 5.2, Gemini, DeepSeek, GPT OSS 20, and Devstral saw improved scores. The remaining models saw higher docking scores, and Nemotron failed to produce any viable SMILES strings. Gemini and Kimi-K2 largely ignored the suggested fragments and produced more statin-like molecules, while all other models used the fragments (usually the napthalene core) and added the carboxyl suggested fragment (see Figure 2, as well as Figures 2, 5, 8, 11, 14, 17, 20, 23 and 28 in the supporting data). All models other than Gemini improved their QED scores (Tables 6, 7). aLogP values generally improved, other than Claude, Gemini, DeepSeek and OSS 120, which saw their aLogP values more closer to the edges of the Rule of 5 boundaries. In the zero-shot with suggested fragments design session, Gemini had the best docking score overall (-8.50, as well as the best average score) followed by GPT 5.2 and Devstral 2 (-8.30) and Claude (-8.10). 

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

<figure>
    <img src="../results/dock_finalist_images/ZERO_SHOT_FRAGMENTS_finalists.png"
         alt="molecules">
    <figcaption>Figure 2. Lowest docking score zero-shot molecules with fragment suggestions for GPT 5.2, Claude and Gemini.</figcaption>
</figure>

When the models were given the SMILES/docking scores dataset and asked to generate HMGCR inhibitors, docking scores improved across the board, show strong few-shot learning from the models. All models other than OSS 20 saw lower 'best' docking scores and average docking scores, while OSS 20 saw a slightly increased 'best' scores but an improved average score. Gemini still had the lowest docking score (-9.20), followed by Nemotron (-9.10), Claude (-9.00), and GPT 5 (-8.90). While Devstral lagged behind these 4 leaders (-8.60), it had the lowest average docking score (-7.90). All models used the fragments present in the sample dataset, and most models used a napthalene or flavone scaffold, except for DeepSeek which opted for the anthrcene scaffold (See Figure 3, as well as Figures 3, 6, 9, 12, 15, 18, 21, 24, 26 and 29 in the supporting data). Gemini saw a significant improvement in QED and aLogP due to finally letting go of the statin-molecule motif and using the suggested fragments (Table 6). All other models saw smaller changes in QED and aLogP either better or slightly worse (Tables 6, 7). It should be noted that the sample data set had a lowest docking score of -8.6, and only the CW models and Nemotron beat that score, and Devstral tied it.

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

<figure>
    <img src="../results/dock_finalist_images/one_shot_finalists.png"
         alt="molecules">
    <figcaption>Figure 3. Lowest docking score one-shot molecules for GPT 5.2, Claude and Gemini.</figcaption>
</figure>

The CWDK models were tested in adversarial design sessions, where they were given in the intial dataset and allowed the use of scoring and auxilliary tools to test hypotheses on good inhibitor molecules. Additionally, their output was passed to another model which then offered criticism of their proposal. The first model then revised its proposal using the tools to refine the proposed molecules. 

#### Table 4. Docking Scores (kcal/mol) for adversarially designed molecules for each model tested. The highest docking score given in the one-shot dataset was -8.6 kcal/mol.

| Model | Adversary |  No. Mols | Low | High | Ave |
|-------|:-:|:-:|:-:|:-:|---|
| GPT 5.2  | Claude  | 2 | -8.90 | -8.90 | -8.90 |
| Claude   | GPT 5.2 | 5 | -9.90 | -8.10 | -8.96 |
| Gemini   | Claude  | 5 | -9.10 | -8.90 | -8.98 |

<figure>
    <img src="../results/dock_finalist_images/OPENAI_finalists.png"
         alt="molecules">
    <figcaption>Figure 4. Top molecules for GPT 5.2.</figcaption>
</figure>


<figure>
    <img src="../results/dock_finalist_images/ANTHROPIC_finalists.png"
         alt="molecules">
    <figcaption>Figure 5. Top molecules for Claude.</figcaption>
</figure>

<figure>
    <img src="../results/dock_finalist_images/GEMINI_finalists.png"
         alt="molecules">
    <figcaption>Figure 6. Top molecules for Gemini.</figcaption>
</figure>

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

#### Table 6. Average QED and aLogP for from each CW model / design mode.

| Model | design mode | QED | aLogP |
|-------|:-:|:-:|---|
| GPT 5.2  | zero-shot | 0.19 | 5.10 |
| GPT 5.2  | zero/frags| 0.72 | 3.77 |
| GPT 5.2  | one-shot  | 0.64 | 1.20 |
| GPT 5.2  | w/ Claude | 0.72 | 4.04 |
||||||
| Claude   | zero-shot | 0.46 | 1.22 |
| Claude   | zero/frags| 0.57 | 4.80 |
| Claude   | one-shot  | 0.55 | 0.34|
| Claude   | w/ GPT 5.2| 0.67 | 2.18 |
||||||
| Gemini   | zero-shot | 0.39 | 4.39 |
| Gemini   | zero/frags| 0.38 | 5.19 |
| Gemini   | one-shot  | 0.71 | 1.56 |
| Gemini   | w/ Claude | 0.73 | 2.12 |

#### Table 7. Average QED and aLogP for from each OW model / design mode.

| Model | design mode | QED | aLogP |
|-------|:-:|:-:|---|
| Deepseek V3.1  | zero-shot | 0.55 | 2.31 |
| Deepseek V3.1  | zero/frags| 0.57 | 0.96 |
| Deepseek V3.1  | one-shot  | 0.49 | 2.13 |
||||||
| GPT OSS 120B  | zero-shot | 0.55 | 5.15 |
| GPT OSS 120B  | zero/frags| 0.61 | 0.27 |
| GPT OSS 120B  | one-shot  | 0.39 | 3.29 |
||||||
| GPT OSS 20B  | zero-shot | 0.59 | 3.03 |
| GPT OSS 20B  | zero/frags| 0.63 | 2.91 |
| GPT OSS 20B  | one-shot  | 0.68 | 1.61 |
||||||
| Devstral 2  | zero-shot | 0.55 | 1.75 |
| Devstral 2  | zero/frags| 0.70 | 2.71 |
| Devstral 2  | one-shot  | 0.64 | 1.53 |
||||||
| Cogito 2.1  | zero-shot | 0.81 | 3.15 |
| Cogito 2.1  | zero/frags| 0.83 | 2.65 |
| Cogito 2.1  | one-shot  | 0.59 | 1.28 |
||||||
| Nemotron 3 Nano  | zero-shot | 0.62 | 0.58 |
| Nemotron 3 Nano  | zero/frags| 0.00 | 0.00 |
| Nemotron 3 Nano  | one-shot  | 0.37 | 5.19 |
||||||
| Kimi K2  | zero-shot | 0.64 | 3.67 |
| Kimi K2  | zero/frags| 0.74 | 1.73 |
| Kimi K2  | one-shot  | 0.62 | 3.79 |

## Minimization of the HOMO-LUMO gap as calculated with CAM-B3LYP/sto-3g in PySCF.Molecule structures optimized with MMFF.

#### Table 8. HOMO-LUMO gaps (eV) for zero shot molecules for each model tested. 

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

<figure>
    <img src="../results/HL/HL_finalist_images/ZERO_SHOT_finalists.png"
         alt="molecules">
    <figcaption>Figure 7. Lowest HOMO-LUMO gap zero-shot molecules for GPT 5.2, Claude and Gemini.</figcaption>
</figure>


#### Table 9. HOMO-LUMO gaps (eV) for zero shot molecules with suggested fragments for each model tested.

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

<figure>
    <img src="../results/HL/HL_finalist_images/ZERO_SHOT_FRAGMENTS_finalists.png"
         alt="molecules">
    <figcaption>Figure 8. Lowest HOMO-LUMO gap zero-shot molecules with fragment suggestions for GPT 5.2, Claude and Gemini.</figcaption>
</figure>


#### Table 10. HOMO-LUMO gaps (eV) for one shot molecules for each model tested. The lowest HOMO-LUMO gap given in the one-shot dataset was 5.579 eV.

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

<figure>
    <img src="../results/HL/HL_finalist_images/one_shot_finalists.png"
         alt="molecules">
    <figcaption>Figure 9. Lowest HOMO-LUMO gap one-shot molecules for GPT 5.2, Claude and Gemini.</figcaption>
</figure>


#### Table 11. HOMO-LUMO gaps (eV) for adversarially designed molecules for each model tested. TThe lowest HOMO-LUMO gap given in the one-shot dataset was 5.579 eV.
/*correction for the SMILES error in the Claude session.

| Model | Adversary |  No. Mols | High | Low | Ave |
|-------|:-:|:-:|:-:|:-:|---|
| GPT 5.2  | Claude  | 3 | 3.95 | 3.91 | 3.93 |
| Claude   | GPT 5.2 | 3 | 3.10 | 2.98 | 3.06 |
| Claude*   | GPT 5.2 | 3 | 6.49 | 6.03 | 6.28 |
| Gemini   | Claude  | 2 | 1.49 | 1.39 | 1.44 |

<figure>
    <img src="../results/HL/HL_finalist_images/OPENAI_finalists.png"
         alt="molecules">
    <figcaption>Figure 10. Top HOMO-LUMO gap molecules for GPT 5.2.</figcaption>
</figure>


<figure>
    <img src="../results/HL/HL_finalist_images/ANTHROPIC_finalists.png"
         alt="molecules">
    <figcaption>Figure 11. Top HOMO-LUMO gap molecules for Claude.</figcaption>
</figure>

<figure>
    <img src="../results/HL/HL_finalist_images/Corrected-ANTHROPIC_finalists.png"
         alt="molecules">
    <figcaption>Figure 11. Top HOMO-LUMO gap corrected molecules for Claude.</figcaption>
</figure>

<figure>
    <img src="../results/HL/HL_finalist_images/GEMINI_finalists.png"
         alt="molecules">
    <figcaption>Figure 12. Top HOMO-LUMO gap molecules for Gemini.</figcaption>
</figure>


#### Table 12. HOMO-LUMO gap (eV) progression for zero-shot,
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

## References

1. Boiko, D. A.; MacKnight, R.; Kline, B.; Gomes, G. Autonomous Chemical Research with Large Language Models. *Nature* **2023**, *624*, 570–578. https://doi.org/10.1038/s41586-023-06792-0.

2. Zhang, J.; Fang, Y.; Zhang, N.; Shao, X.; Chen, H.; Fan, X. Exploring the Potential of Large Language Models in Molecular Tasks: An Insightful Evaluation with GPT-4. *bioRxiv* **2023**. https://doi.org/10.1101/2023.11.28.568966.

3. Wang, R.; Feng, H.; Wei, G.-W. ChatGPT in Drug Discovery: A Case Study on Anticocaine Addiction Drug Development with Chatbots. *J. Chem. Inf. Model.* **2023**, *63*, 7189–7209. https://doi.org/10.1021/acs.jcim.3c01429.

4. Bran, A. M.; Cox, S.; Schilter, O.; Baldassari, C.; White, A. D.; Schwaller, P. ChemCrow: Augmenting Large-Language Models with Chemistry Tools. *Preprint*, 2023. https://doi.org/10.48550/arxiv.2304.05376.

5. Cavanagh, J. M.; Sun, K.; Gritsevskiy, A.; Bagni, D.; Bannister, T. D.; Head-Gordon, T. SmileyLlama: Modifying Large Language Models for Directed Chemical Space Exploration. *ArXiv* **2024**, *abs/2409.02231*. https://doi.org/10.48550/arxiv.2409.02231.






6. Fan, C.; Cao, Z.; Ma, Z.; Yu, N.; Peng, Y.; Zhang, J.; Gao, Y.; Fu, G. ChatMol: A Versatile Molecule Designer Based on the Numerically Enhanced Large Language Model. *ArXiv* **2025**, *abs/2502.19794*. https://doi.org/10.48550/arxiv.2502.19794.

7. Gao, B.; Huang, Y.; Liu, Y.; Xie, W.; Ma, W.-Y.; Zhang, Y.-Q.; Lan, Y. PharmAgents: Building a Virtual Pharma with Large Language Model Agents. *ArXiv* **2025**, *abs/2503.22164*. https://doi.org/10.48550/arxiv.2503.22164.

8. Kim, H.; Jang, Y.; Ahn, S. MT-Mol: Multi Agent System with Tool-Based Reasoning for Molecular Optimization. *Findings Assoc. Comput. Linguist.: EMNLP* **2025**, 11544–11573. https://doi.org/10.18653/v1/2025.findings-emnlp.619.

9. Ünlü, A.; Rohr, P.; Çelebi, A. An Auditable Agent Platform for Automated Molecular Optimisation. *ArXiv* **2508**, *abs/2508.03444*. https://doi.org/10.48550/arxiv.2508.03444.

2. Ramos, M. C.; Collison, C. J.; White, A. D. A Review of Large Language Models and Autonomous Agents in Chemistry. *Chem. Sci.* **2025**, *16*, 2514–2572. https://doi.org/10.48550/arxiv.2407.01603.




11. AlKharboush, D. F.; Kozielski, F.; Wells, G.; Porta, E. O. J. Fragment-based Drug Discovery: A Graphical Review. *Curr. Res. Pharmacol. Drug Discov.* **2025**, *9*. https://doi.org/10.1016/j.crphar.2025.100233.

12. Woodhead, A. J.; Erlanson, D. A.; de Esch, I. J. P.; Holvey, R. S.; Jahnke, W.; Pathuri, P. Fragment-to-Lead Medicinal Chemistry Publications in 2022. *J. Med. Chem.* **2024**, *67*, 2287–2304. https://doi.org/10.1021/acs.jmedchem.3c02070.

13. Yang, R.; Zhou, H.; Wang, F.; Yang, G. DigFrag as a Digital Fragmentation Method Used for Artificial Intelligence-based Drug Design. *Commun. Chem.* **2024**, *7*. https://doi.org/10.1038/s42004-024-01346-5.

14. Jinsong, S.; Qifeng, J.; Xing, C.; Hao, Y.; Wang, L. Molecular Fragmentation as a Crucial Step in the AI-based Drug Development Pathway. *Commun. Chem.* **2024**, *7*. https://doi.org/10.1038/s42004-024-01109-2.
