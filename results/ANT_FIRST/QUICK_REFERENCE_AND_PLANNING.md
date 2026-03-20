# Quick Reference: Design Session Summary

## 📋 Session Overview
- **Target**: HMG-CoA Reductase (HMGCR) inhibitors
- **Duration**: 8 turns (4 rounds of model proposals + 4 rounds of adversarial feedback)
- **Final Status**: 3 lead molecules identified with validated statin-like pharmacophore

---

## 🏆 FINAL LEAD MOLECULES

### PRIMARY RECOMMENDATION: Lead #1
```
SMILES: O=c1cc(-c2ccc(C)cc2)oc2cc(F)cc(CC(O)C(O)C(=O)O)c12

Docking Score:  -9.6 kcal/mol
QED:            0.634 (good)
MW:             372.3 Da
LogP:           2.256 (excellent)
PSA:            107.97 Ų (borderline, may need prodrug)
HBA/HBD:        6 hydrogen bond acceptors / 3 donors
```
**Key Features**:
- ✓ True statin-like diol-acid pharmacophore (CC(O)C(O)C(=O)O)
- ✓ Fluorine on core for metabolic stability
- ✓ Clean, no obvious liabilities
- ⚠ High PSA suggests prodrug may be needed for oral absorption

---

### POTENCY VARIANT: Lead #2
```
SMILES: O=c1cc(-c2c(Cl)cc(C)cc2)oc2cc(F)cc(CC(O)C(O)C(=O)O)c12

Docking Score:  -10.4 kcal/mol (0.8 kcal/mol better than Lead #1)
QED:            0.601
MW:             406.8 Da
LogP:           2.910
PSA:            107.97 Ų
HBA/HBD:        6/3
```
**Key Features**:
- ✓ Highest predicted affinity
- ✓ Ortho-chloro may control biaryl geometry
- ⚠ Higher MW, lower QED
- ⚠ Unvalidated whether Cl effect is real or score artifact

**When to use**: If enzyme assay shows Lead #1 is weaker than predicted

---

### FLEXIBLE VARIANT: Lead #3
```
SMILES: O=c1cc(-c2ccc(C)cc2)oc2cc(F)cc(CCC(O)C(O)C(=O)O)c12

Docking Score:  -9.4 kcal/mol
QED:            0.601
MW:             386.4 Da
LogP:           2.647
PSA:            107.97 Ų
Rotatable Bonds: 6 (vs 5 for Lead #1)
```
**Key Features**:
- ✓ Extended tail; slight increase in flexibility
- ⚠ Lower docking score (0.2 kcal/mol worse)
- ⚠ Extra rotatable bonds typically hurt binding entropy

**When to use**: Only if Lead #1 cellular potency is poor despite good enzyme activity (conformational sampling issue)

---

## 📊 Design Evolution

### Round 1: Initial Proposals
**Model Claim**: High-scoring coumarin molecules with generic H-bonding improvements
**Problems Found**:
- ❌ Dianions (molecules 2 & 4) with unrealistic phenoxides
- ❌ Missing statin-like diol-acid pharmacophore
- ❌ Mixed protonation states (QED on neutral, docking on anionic)
- ❌ Overconfident that anions are "realistic"

### Round 2: First Refinement  
**Model Change**: Removed dianions; added fluorine; improved drug properties
**Problems Found**:
- ❌ Still single carboxylate only (not diol-acid)
- ❌ Phenolic OH has high metabolic liability
- ❌ Score comparisons still unreliable

### Round 3: Pharmacophore Shift
**Model Change**: Attempted to add statin-like "diol-acid" tail
**Critical Error Found**:
- ❌ SMILES had only ONE OH, not a diol
- ❌ Docking scores counterintuitive (removing groups improved score)
- ❌ Protonation logic still incomplete

### Round 4: Final Correction
**Model Change**: **Fixed SMILES to include true secondary diol** (CC(O)C(O)C(=O)O)
**Result**: ✓ Proper pharmacophore now matches statin pattern
**Remaining Issues**:
- ⚠ Docking scores unvalidated (no replicates)
- ⚠ Poses not compared to known HMGCR binders
- ⚠ Permeability strategy incomplete

---

## 🔬 Critical Design Insight

**The Statin Pharmacophore Pattern**

Real HMGCR inhibitors (like simvastatin, atorvastatin) use:
```
A diol-acid moiety: 
    - Two hydroxyl groups (OH)
    - One carboxylic acid (COOH)
    - Positioned to form dense H-bond network in catalytic site
```

**What the Final Leads Have**:
✓ True diol-acid: CC(O)C(O)C(=O)O
✓ Rigid aromatic core: Coumarin + phenyl
✓ Proper substituents: F for metabolism, alkyl for lipophilicity

**What They Lack** (compared to real statins):
- Longer/more flexible diol-acid tail (might be necessary)
- Validation that poses actually match HMGCR's known binding site
- Prodrug formulation for permeability (high PSA issue)

---

## ⚠️ Key Unresolved Issues

### 1. Docking Score Reliability
- Reported differences (0.2–0.8 kcal/mol) within typical noise
- No replicates, rescoring, or pose validation
- Recommendation: **Run with explicit validation**

### 2. Protonation State Handling  
- At pH 7.4, carboxylic acids are mostly deprotonated (anionic)
- But anionic form may not permeate membranes well
- Need BOTH: docking for potency (anionic) + prodrug for absorption (neutral/ester)

### 3. Pose Validation Missing
- No comparison to HMGCR crystal structures with known inhibitors
- No confirmation that diol-acid occupies right catalytic site
- **Critical next step**: Dock into HMGCR PDB structure (e.g., 1HWK)

### 4. Permeability Strategy Vague
- PSA ~108 Ų with 3 HBD = poor passive permeability
- Likely requires prodrug (ester masking) or active transport
- Specific prodrug options not yet proposed

### 5. Structural Liabilities Not Assessed
- Coumarin ring: photoreactivity risk, CYP inhibition potential
- Lactone: metabolic conjugation site
- Need liability screening

---

## 🧪 Recommended Experimental Path

### Phase 1: Validate Predictions (Fast, Low Cost)
```
1. Retrieve HMGCR crystal structure (PDB: 1HWK or similar with statin)
2. Dock Lead #1 & #2 with validated protocol
   - Both neutral and anionic forms
   - Same conditions for fair comparison
3. Perform pose alignment vs. simvastatin pose
4. Apply rescoring (MM-PBSA/MM-GBSA)
```
**Duration**: 1-2 weeks  
**Cost**: Negligible (computational)  
**Risk**: Low (validate before synthesis)

### Phase 2: Synthesize (If Poses are Good)
```
Test set:
- Lead #1 (primary)
- Lead #1 analogs: p-F, p-CF3 variants (test para effect)
- Prodrugs of Lead #1: methyl ester, cyclic carbonate (test permeability)
- Lead #2 (potency variant, if budget allows)
```
**Duration**: 4-8 weeks  
**Cost**: ~$10-50K  
**Risk**: Medium (synthesis failure possible)

### Phase 3: Biochemical Assay (If Synthesis Works)
```
HMGCR enzyme inhibition assay:
- Measure IC50 for all synthesized molecules
- Compare to statin standards (simvastatin, atorvastatin)
- Validate docking predictions
```
**Duration**: 2-4 weeks  
**Cost**: ~$5-10K  
**Risk**: Low (standard assay)

### Phase 4: Cell & ADME Testing (If Potency is Good)
```
- Cell assay: Cholesterol synthesis inhibition (HepG2/CHO)
- Permeability: Caco-2 transepithelial transport
  - Test parent acids and prodrugs side-by-side
- PK: Oral/IV dosing in mice; plasma levels, metabolism
- Safety: Metabolic stability (HLM), off-target screening
```
**Duration**: 8-12 weeks  
**Cost**: ~$30-100K  
**Risk**: Medium (compound selection critical)

### Phase 5: Iterative Refinement
- Use data from Phases 3-4 to guide next design cycle
- If enzyme potency good but cell activity weak → optimize prodrug
- If enzyme potency weak → return to design (try scaffold variants)
- If off-target issues detected → modify core or substituents

---

## 📈 Expected Outcomes

### Best Case
- Lead #1 shows excellent enzyme potency (IC50 < 100 nM)
- Prodrug variant shows good Caco-2 permeability
- Lead #2 validates ortho-Cl effect
- Advance to PK testing

### Moderate Case  
- Lead #1 enzyme potency moderate (IC50 100-500 nM)
- Prodrug helps permeability but still transporter-dependent
- Lead #2 shows marginal improvement
- Optimize prodrug; consider cell-based screening for uptake

### Challenging Case
- Lead #1 enzyme potency weak (IC50 > 1000 nM)
- Poses don't match expected HMGCR binding mode
- Design cycle: Try scaffold variants (coumarin swap, tail modifications)
- Return to computational design with validated binding mode

---

## 💡 Key Lessons from Design Session

### What Worked
1. ✓ **Iterative feedback loop** - Model improved after each critique
2. ✓ **Pharmacophore targeting** - Shift to statin-like motif was essential
3. ✓ **Multi-variant strategy** - 3 leads allow hypothesis testing
4. ✓ **Property balancing** - QED, LogP, PSA considered systematically

### What Needs Improvement
1. ❌ **Docking validation** - Scores taken at face value without replication
2. ❌ **Pose inspection** - No comparison to known binders
3. ❌ **Protonation clarity** - Mixed pH states in comparisons
4. ❌ **PK by design** - Permeability strategy vague/incomplete
5. ❌ **SMILES accuracy** - Round 3 error (claiming diol with 1 OH)

---

## 📝 Next Immediate Actions

**Week 1**:
- [ ] Run validation docking (Lead #1 & #2, both protonation states)
- [ ] Overlay poses with HMGCR crystal structure
- [ ] Decide: Proceed with synthesis or iterate design?

**If Go Decision**:
- [ ] Finalize synthetic route for Lead #1, prodrugs, and variants
- [ ] Order starting materials
- [ ] Aim for synthesis within 4-6 weeks

**Parallel**:
- [ ] Prepare HMGCR enzyme assay (cells, substrates, controls)
- [ ] Set up Caco-2 or equivalent permeability assay
- [ ] Identify mouse model for PK (C57BL/6 standard)

---

## 📎 Document Resources

1. **DESIGN_SESSION_COMPREHENSIVE_ANALYSIS.md**
   - Full 8-turn detailed analysis
   - Each round explained with strengths/weaknesses
   - All 15 molecules documented

2. **generate_molecular_images.py**
   - Script to create PNG structure images using RDKit
   - Run: `python generate_molecular_images.py`
   - Outputs: All 15 structures as high-res images

3. **This file**: Quick reference and experimental planning guide

---

**Analysis Date**: March 19, 2026  
**Status**: Ready for experimental validation  
**Confidence**: Medium (design sound, but unvalidated in HMGCR system)

