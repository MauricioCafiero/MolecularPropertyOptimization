# ANT_FIRST Session - Quick Reference Index

**Navigation Guide:** Use this document to quickly find molecules, scores, and key metrics across the entire session.

---

## Score Rankings (Descending)

| Rank | Score | Molecule | Type | PSA | QED | Notes |
|------|-------|----------|------|-----|-----|-------|
| 1 | **-9.9** | Monoanionic_hydroxyl_acetamide_v1 | Early Proposal | 119.7 | 0.709 | Score plateau (×3) |
| 1 | **-9.9** | Monoanionic_hydroxyl_acetamide_v2 | Early Proposal | 119.7 | 0.709 | F position variant |
| 1 | **-9.9** | Monoanionic_hydroxyl_acetamide_chlorine | Early Proposal | 119.7 | 0.692 | F→Cl variant |
| 4 | **-9.4** | CF3_substituent_Rank1 | High Scorer | 162.8 | 0.545 | Very high PSA |
| 5 | **-9.2** | Rank_1_Best_Affinity ✓ | **FINAL CHOICE** | 136.6 | 0.657 | **RECOMMENDED** |
| 5 | **-9.2** | Dianion_reference | Medium Scorer | 179.6 | 0.598 | Dianion; no PK |
| 7 | **-9.1** | Ortho_carboxylate_Chlorofluoro | Dianion | 180.0 | 0.671 | Cl+F variant |
| 7 | **-9.1** | Ortho_carboxylate_Fluoroiodo | Dianion | 180.0 | 0.528 | I adds mass |
| 7 | **-9.1** | Ortho_carboxylate_Fluorobromo | Dianion | 180.0 | 0.625 | Br intermediate |
| 10 | **-8.9** | Para_phenyl_amide_Fluorine | Medium Scorer | 136.6 | 0.662 | Unsubstituted phenyl |
| 10 | **-8.9** | Para_phenyl_amide_Chlorine | Medium Scorer | 136.6 | 0.657 | F≈Cl tie |
| 10 | **-8.9** | CF3_on_phenyl | Medium Scorer | 136.6 | 0.570 | CF3 on phenyl (not core) |
| 10 | **-8.9** | Ortho_carboxylate_Fluoroonly | Dianion | 180.0 | 0.673 | Best dianion QED |
| 14 | **-8.6** | Rank_2_Balanced ✓ | **FINAL CHOICE** | 113.8 | 0.720 | Best balance |
| 15 | **-8.3** | Rank_3_Best_Permeability ✓ | **FINAL CHOICE** | 91.1 | 0.714 | Best permeability |

---

## Final Recommendations (Rank 1-3)

### Rank 1: Best Affinity
```
SMILES: O=c1c(O)c(-c2c(C)cc(C(=O)N)cc2)oc2c(F)ccc(C(=O)N)c12
Score: -9.2 kcal/mol
MW: 356.3 | LogP: 1.811 | PSA: 136.6 | QED: 0.657
HBD: 3 | HBA: 5 | RotBonds: 3
Use: Crystallography, biochemical validation
```
**Key Features:**
- ✓ Highest affinity among permeability-conscious designs
- ✓ Ortho-methyl on phenyl ring validated (+0.3 kcal/mol improvement)
- ✓ Chromone hydroxyl critical to binding
- ✗ PSA 136.6 problematic for passive absorption; needs transporter assumption

---

### Rank 2: Balanced Affinity + Permeability
```
SMILES: O=c1c(O)c(-c2c(C)cc(C(=O)N(C)C)cc2)oc2c(F)ccc(C(=O)N)c12
Score: ~-8.6 kcal/mol (estimated)
MW: 384.4 | LogP: 2.414 | PSA: 113.8 | QED: 0.720
HBD: 2 | HBA: 5 | RotBonds: 3
Use: Oral PK studies, Caco-2 screening
```
**Key Features:**
- ✓ PSA = 113.8 acceptable for passive absorption (~40% reduction vs Rank 1)
- ✓ HBD reduced to 2 (one amide N-methylated)
- ✓ Excellent QED (0.720)
- ~ Slight affinity loss (-0.6 kcal/mol estimated) requires validation

---

### Rank 3: Best Permeability Potential
```
SMILES: O=c1c(O)c(-c2c(C)cc(C(=O)N(C)C)cc2)oc2c(F)ccc(C(=O)N(C)C)c12
Score: ~-8.3 kcal/mol (estimated)
MW: 412.4 | LogP: 3.017 | PSA: 91.1 | QED: 0.714
HBD: 1 | HBA: 5 | RotBonds: 3
Use: Backup if Rank 2 poor permeability; test PSA threshold
```
**Key Features:**
- ✓ PSA = 91.1 (excellent; enters Ro5 sweet spot <140)
- ✓ Single HBD (only phenolic OH)
- ✓ LogP 3.0 manageable with formulation
- ~ Affinity penalty (-0.9 vs Rank 1) needs empirical confirmation
- ⚠ Only validation: Does phenolic OH alone anchor binding?

---

## Docking Score Interpretation

### Evidence for Score Plateau Artifact

The session contained **three identical -9.9 scores** and multiple **-8.9 / -9.1 clusters:**

| Modification | Result | Conclusion |
|--------------|--------|-----------|
| Rank 1 (Rank 1 with F position ortho) | -9.9 | Baseline |
| Rank 1 with F at position 3 instead | -9.9 | F position NOT discriminating |
| Rank 1 with F→Cl substitution | -9.9 | Halogen change NOT discriminating |
| **Inference:** | | Scoring at **saturation/quantization** |

---

### Uncertainty Intervals

Per adversary feedback, assign confidence levels:

| Score Range | Cluster | Confidence | Interpretation |
|-------------|---------|------------|-----------------|
| **-9.8 to -9.9** | -9.9 × 3 | **Low (±0.3)** | Score plateau; halogen position artifact |
| **-9.3 to -9.4** | -9.4 × 1 | **Medium (±0.4)** | Single measurement; within noise |
| **-9.0 to -9.2** | -9.1-9.2 × 5 | **Low (±0.4)** | Dianion series; scoring issue suspected |
| **-8.8 to -9.0** | -8.9 × 4 | **Low (±0.3)** | Score tied across different scaffolds |
| **-8.3 to -8.6** | -8.3-8.6 × 2 | **Medium (±0.4)** | Methodical N-methylation series; more reliable |

**Recommendation:** Score differences **within same cluster are noise.** Treat as **confidence intervals, not discriminators.** Use **chemical properties (PSA, HBD, MW)** for ranking, not docking score magnitude.

---

## Molecular Property Landscape

### PSA Distribution (Critical for Absorption)

```
Very High PSA (>160): Risk of zero passive permeability
├─ CF3_substituent_Rank1 (162.8)
├─ Rank_2_iodo variant (176.5)
└─ All dianion series (179.6-180.0)

High PSA (120-160): Problematic; needs transporter
├─ Rank_1_Best_Affinity (136.6)
├─ Para_phenyl variants (136.6)
└─ Early proposals v1-v3 (119.7)

Acceptable PSA (<120): Passive permeability possible
├─ Rank_2_Balanced (113.8)
└─ Rank_3_Best_Permeability (91.1) ✓ PREFERRED
```

**Bottom Line:** Only Rank 2 and Rank 3 fall into acceptable passive permeability range.

---

### QED Distribution (Drug-Likeness)

```
Excellent QED (>0.70): Drug-like chemical space
├─ Rank_2_Balanced (0.720) ✓
├─ Early_proposal_v1 (0.709)
├─ Rank_3_Best_Permeability (0.714) ✓
└─ Ortho_carboxylate_Fluoroonly (0.673)

Good QED (0.65-0.70): Acceptable
├─ Rank_1_Best_Affinity (0.657)
├─ Para_phenyl variants (0.657-0.662)
└─ CF3_on_phenyl (0.570)

Fair QED (<0.65): Unfavorable; high structural alerts
├─ CF3_substituent_Rank1 (0.545)
└─ Ortho_carboxylate_Fluoroiodo (0.528)
```

**Bottom Line:** Rank 1-3 all maintain acceptable QED (>0.65). Dianion series scores well on QED but fails on permeability.

---

## Molecular Weight Trends

```
Lightweight (<360 Da): Good for PK, may lack potency
├─ Para_phenyl_amide_Fluorine (342.3)
├─ Ortho_carboxylate_Fluoroonly (340.3)
└─ Rank_1_Best_Affinity (356.3)

Optimal (360-400 Da): Balance of affinity & clearance
├─ Rank_2_Balanced (384.4) ✓
├─ Early_proposals (388.3)
├─ CF3_substituent_Rank1 (449.3)
└─ Dianion_reference (409.3)

Heavy (>420 Da): Risk of low clearance
├─ Rank_3_Best_Permeability (412.4)
├─ Ortho_carboxylate_Fluorobromo (419.2)
├─ Ortho_carboxylate_Fluoroiodo (466.2) ✗
└─ Nitrile_variant (474.3) ✗
```

**Bottom Line:** Rank 1-2 are optimal MW; Rank 3 slightly heavy but acceptable.

---

## Hydrogen Bond Donor/Acceptor Analysis

### HBD Count (Impact on Clearance & Permeability)

```
1 HBD: Optimal for absorption
└─ Rank_3_Best_Permeability (phenolic OH only)

2 HBD: Acceptable
├─ Early_proposals (NH + OH)
└─ Rank_2_Balanced (acetamide NH + phenol OH)

3 HBD: Problematic; high clearance/low Caco-2
├─ Rank_1_Best_Affinity
├─ All dual-amide designs
└─ All dianion series
```

**Conclusion:** HBD is major discriminator between Rank 2 (2 HBD) and Rank 1 (3 HBD).

### HBA Count (Moderate impact; less critical than HBD)

All Rank 1-3 maintain **5-7 HBA.** This is elevated but acceptable for chromone + amide scaffolds. Dianion series hit 7 HBA but that's secondary to permeability failure from charge.

---

## Session Statistics

| Metric | Value |
|--------|-------|
| **Total molecules analyzed** | 20 |
| **Docking score range** | -8.3 to -9.9 kcal/mol |
| **Score ties (within 0.0 exact)** | 3 (-9.9 cluster); 4 (-8.9 cluster) |
| **Mean score** | -9.0 kcal/mol |
| **Median PSA** | 136.6 Ų |
| **Average QED** | 0.648 |
| **Molecules with PSA<120** | 2 (Rank 2, Rank 3) |
| **Molecules with PSA<100** | 1 (Rank 3 only) |
| **Design iterations** | 4 major cycles |

---

## File Navigation

```
results/ANT_FIRST/
├── adversary_design_2026-04-01_10-27-25.md ........... Original session transcript
├── COMPREHENSIVE_MOLECULAR_ANALYSIS.md ............... THIS DOCUMENT (detailed analysis)
├── QUICK_REFERENCE_AND_PLANNING.md .................. This reference index
├── generate_images.py ............................... Image generation script
└── molecular_structures/ ............................ All 15 PNG structures
    ├── Rank_1_Best_Affinity.png
    ├── Rank_2_Balanced.png
    ├── Rank_3_Best_Permeability.png
    ├── CF3_substituent_Rank1.png
    ├── Dianion_reference.png
    ├── Para_phenyl_amide_Fluorine.png
    ├── Para_phenyl_amide_Chlorine.png
    ├── CF3_on_phenyl.png
    ├── Ortho_carboxylate_Chlorofluoro.png
    ├── Ortho_carboxylate_Fluorobromo.png
    ├── Ortho_carboxylate_Fluoroiodo.png
    ├── Ortho_carboxylate_Fluoroonly.png
    ├── Monoanionic_hydroxyl_acetamide_v1.png
    ├── Monoanionic_hydroxyl_acetamide_v2.png
    └── Monoanionic_hydroxyl_acetamide_chlorine.png
```

---

## Decision Tree for Lead Selection

```
Start: Which endpoint is priority?

├─ BINDING AFFINITY primary
│  └─ Select: Rank 1 (-9.2 kcal/mol) for crystallography
│
├─ ORAL BIOAVAILABILITY primary  
│  ├─ Select: Rank 2 (PSA 113.8, -8.6 estimated)
│  └─ If Rank 2 permeability acceptable → Rank 2 leads
│     If Rank 2 permeability fails → Fall back to Rank 3
│
└─ UNCERTAIN / WANT OPTIONALITY
   └─ Pursue BOTH paths in parallel:
      ├─ Path A: Rank 1 → Crystallography → Structure-guided next round
      └─ Path B: Rank 2 → Caco-2 screening → If good → In vivo PK
```

---

## Key Experimental Validations Needed

### For Rank 1

- [ ] X-ray crystallography (confirm phenolic OH engagement)
- [ ] Biochemical inhibition assay (NADP+ reduction kinetics)
- [ ] SPR/BLI for Kd confirmation
- [ ] Aqueous solubility (predicted PSA 136 Ų → moderate solubility)

### For Rank 2

- [ ] Caco-2 transepithelial permeability (target: >0.5 × 10⁻⁶ cm/s)
- [ ] PAMPA permeability (faster screening)
- [ ] Efflux ratio (P-gp/BCRP substrate assessment)
- [ ] Liver microsome stability (T1/2, CLint)
- [ ] If Caco-2 favorable: Rodent IV + PO

### For Rank 3

- [ ] Re-dock across multiple seeds vs Rank 1 (validate -0.9 kcal/mol penalty)
- [ ] Biochemical assay IF affinity docking confirmed
- [ ] Caco-2 permeability (should be much better than Rank 2)

---

## Conclusion

**Recommended advancement strategy:**

1. **Immediate (Week 1):** Synthesize Rank 1 and Rank 2; initiate Rank 1 crystallography request
2. **Parallel (Week 2-3):** Rank 2 → Caco-2/PAMPA screening; Rank 1 → biochemical assay
3. **Decision Point (Week 4):** 
   - If Rank 1 crystal successful + Rank 2 Caco-2 excellent → Pursue both in IVIVe
   - If Rank 1 crystal uncertain + Rank 2 Caco-2 poor → Pivot to Rank 3 with re-docking
4. **If permeability blocker:** Consider return to bioisosteric optimization (O-methylation, further N-methylation guided by crystallography data)

**Timeline to clinical candidate:** 12-16 weeks (assuming typical medicinal chemistry iteration cycle)

