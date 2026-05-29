# Key Conclusions from FAO-MOLPROP Study

## Overall Framework

- **Modularity**: The FAO-MOLPROP (Fragment-based, AI-assisted Optimization of molecular properties) workflow is highly modular, requiring only changes to input fragments and scoring functions for different tasks
- **Generality**: Successfully demonstrated for two distinct tasks (docking score minimization and HOMO-LUMO gap minimization), proving applicability to any computationally-scored molecular property
- **Fragment-based approach**: Using 9 scaffolds and 567 potential substituents created a flexible design space of 14,742+ unique molecules
- **Tool-augmented LLMs**: Modern frontier LLMs with tool access can perform chemistry tasks without fine-tuning, marking a significant advance from 2024 capabilities

## Model Performance - Docking Task (HMGCR Inhibitor Design)

### Zero-shot Performance
- **Best performers**: Claude and Kimi K2 achieved lowest docking scores (-8.30 kcal/mol) in zero-shot mode
- **Knowledge-based advantage**: GPT 5.2, Claude, DeepSeek, and Kimi K2 produced statin-like molecules with carboxy-diol pharmacophores, demonstrating chemistry knowledge
- **Fragment suggestions**: Adding fragment suggestions improved some models but was inconsistent across all models

### Progressive Improvement
- **Adversarial design superiority**: All CWDK models (closed-weight + DeepSeek + Kimi K2) improved from zero-shot through adversarial design
- **Biggest improvements**: 
  - DeepSeek: 2.1 kcal/mol improvement (lowest score), 1.6 kcal/mol (average)
  - Claude: 1.6 kcal/mol improvement (lowest score), 1.8 kcal/mol (average)
- **Claude leadership**: Achieved best overall docking score of -9.90 kcal/mol in first-generation adversarial design
- **Third-generation results**: Claude reached -9.60 kcal/mol despite additional synthesis/binding constraints

### Drug-likeness Metrics
- **QED convergence**: All models converged to QED ~0.7 (except DeepSeek ~0.5) in adversarial design
- **aLogP optimization**: Models achieved aLogP values of ~2.0 (Claude, Gemini, Kimi K2) to ~4.0 (GPT 5.2, DeepSeek), within drug-like range
- **Target comparison**: Rosuvastatin (most potent known statin) has aLogP 2.40, which several models approached
- **SAS scores**: Third-generation adversarial design decreased SAS scores by 0.5-2 units across all models, indicating improved synthetic accessibility

### Binding Site Analysis
- **First generation**: Only Claude's zero-shot molecule bound to main catalytic site; all OW models bound correctly
- **Third generation**: With binding site verification tools, Claude and GPT 5.2 maintained correct binding; others overlapped with HMG-CoA substrate site

### Comparison to Previous Work
- **Superior to fine-tuned models**: Adversarial designs outperformed author's previous transformer-decoder model:
  - Better average docking scores (all adversarial < -8.08 kcal/mol except GPT 5.2 3G)
  - Higher QED values (0.44 vs ~0.7)
  - More moderate aLogP (4.8 vs 1.5-4.0 range)
- **Beats known statins**: Average adversarial scores surpassed known statin average (-7.95 kcal/mol)

## Model Performance - HOMO-LUMO Gap Task

### Zero-shot Performance
- **Best low values**: GPT OSS 120B (2.21 eV) and Claude (2.75 eV) achieved lowest gaps
- **Strategy recognition**: Models correctly identified conjugated chains and polycyclic aromatics as design targets
- **Fragment interference**: Suggested fragments worsened performance, increasing lowest values to >5.3 eV

### Progressive Improvement
- **One-shot recovery**: Providing scored examples allowed models to recover from fragment suggestion limitations
- **Claude consistency**: Maintained low values (2.46 eV) in one-shot, only slightly higher than zero-shot
- **Adversarial excellence**: 
  - Gemini achieved lowest overall gaps (1.39-1.49 eV)
  - GPT 5.2 produced best personal performance (3.91-3.95 eV)
  - Claude maintained competitive performance (2.98-3.10 eV)

### Design Strategy
- **Iterative refinement**: Adversarial process allowed gradual construction of optimal polycyclic aromatic systems
- **Tool verification**: Models used HLG calculation tools to verify designs before final output
- **Error detection**: Claude made SMILES ring-numbering errors despite warnings, highlighting areas for improvement

## Cross-Task Patterns

### Learning Capabilities
- **Context utilization**: Models showing biggest improvements (DeepSeek, Claude) are most adept at learning from provided context
- **Tool integration**: Adversarial design with tool access consistently outperformed zero-shot and one-shot approaches
- **Iterative refinement**: Multi-turn adversarial conversations enabled exploration of chemical space beyond single-shot attempts

### SMILES Generation Quality
- **Adversarial advantage**: Tool-augmented adversarial sessions produced fewer invalid SMILES due to verification capabilities
- **Model differences**: Zero/one-shot sessions produced many invalid SMILES; adversarial sessions nearly eliminated this issue
- **Deliberate reduction**: In adversarial mode, models sometimes chose to propose <5 molecules, prioritizing quality over quantity

### Additional Constraints Handling
- **Third-generation tradeoffs**: Adding binding site and synthesis constraints slightly increased docking scores but improved overall drug-likeness
- **Multi-objective optimization**: Models successfully balanced multiple objectives (score, QED, aLogP, SAS, binding site)
- **Tool-guided decisions**: Lipinski and SAS/NP tools helped models discard promising scores in favor of more realistic drug candidates

## Model-Specific Insights

### Closed-Weight Models
- **GPT 5.2**: Consistent performer, occasionally explored alternative scaffolds (3G design)
- **Claude**: Most consistent leader in docking tasks, achieved best absolute scores
- **Gemini**: Excelled at HOMO-LUMO gap minimization, occasionally made SMILES syntax errors

### Open-Weight Models
- **DeepSeek**: Strong learner, showed greatest improvement through iterations
- **Kimi K2**: Performed well in zero-shot, competitive with closed-weight models
- **GPT OSS models**: Variable performance, smaller model (20B) struggled more
- **Nemotron**: Failed to produce viable SMILES in most tests

## Methodological Advantages

### Flexibility
- **User control**: Scaffold and substituent selection allows tailoring to specific project requirements
- **Modular scoring**: Any computational property can be optimized by swapping scoring function
- **Auxiliary tools**: Optional functions (Lipinski, PubChem, binding site analysis) enhance capabilities without complexity

### Efficiency
- **No fine-tuning required**: Frontier LLMs perform chemistry tasks with general weights
- **On-the-fly calculations**: Tools execute during inference rather than requiring pre-computed training data
- **Resource scaling**: Basis set choice (sto-3g used here) allows balancing speed vs. accuracy

### Comparison to Existing Methods
- **PharmAgents/MT-Mol**: FAO-MOLPROP is more streamlined (2 LLMs vs 4-8) and more customizable
- **ChatMol/SmileyLlama**: No training required; more efficient for new targets
- **DigFrag**: Combines fragment-based approach with LLM reasoning rather than just neural networks

## Limitations and Areas for Improvement

### Technical Issues
- **SMILES syntax errors**: Some models (Gemini, Claude) made ring-numbering mistakes despite prompts
- **Fragment guidance paradox**: Suggested fragments helped docking but hurt HOMO-LUMO gap tasks
- **Binding site variation**: Third-generation designs sometimes bound to substrate site rather than inhibitor site

### Model Limitations
- **Variable quality**: Open-weight model performance ranged widely (Nemotron failed, DeepSeek/Kimi K2 competed with closed-weight)
- **Invalid outputs**: Zero/one-shot modes produced many invalid SMILES strings
- **Chemistry knowledge gaps**: Some models lacked statin pharmacophore knowledge

## Practical Applications

### Drug Discovery
- **Lead optimization**: Successfully designed molecules with better scores than known statins
- **Multi-objective optimization**: Balanced docking scores with ADME properties
- **Synthesis considerations**: SAS scores guide toward synthetically accessible molecules

### Materials Science
- **HOMO-LUMO gaps**: Demonstrated applicability beyond drug design to optoelectronic properties
- **General applicability**: Framework applicable to any molecular property (conductivity, stability, etc.)

### Research Efficiency
- **Rapid iteration**: Adversarial design enables quick exploration of chemical space
- **Automated screening**: Fragment-based approach automates tedious manual design steps
- **Verification built-in**: Tool access ensures proposals are computationally validated before human review

## Future Directions

- **Improved prompts**: Better guidance on SMILES syntax to reduce errors
- **Additional constraints**: Incorporation of more synthesis planning tools
- **Broader testing**: Application to diverse molecular property optimization tasks
- **Model updates**: Testing with newer/improved LLMs as they become available
- **Experimental validation**: Synthesis and testing of top candidates from computational screening
