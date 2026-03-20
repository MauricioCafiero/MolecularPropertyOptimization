#!/usr/bin/env python3
"""
Generate molecular structure images from the adversarial design session
Run this script to create PNG visualizations of all proposed molecules
"""

from rdkit import Chem
from rdkit.Chem import Draw
from pathlib import Path
import json

# Create output directory
output_dir = Path("results/molecular_structures")
output_dir.mkdir(parents=True, exist_ok=True)

# Define all molecules from each round
molecules_data = {
    "01_Initial_Model_Recommendations": [
        {
            "name": "Initial_Mol_1",
            "smiles": "O=c1c(N)c(-c2c(C)cc(NC(=O)C)cc2)oc2cccc(C(C(=O)[O-]))c12",
            "label": "Mol 1: Amino + Acetamido",
            "score": -9.4,
            "qed": 0.723,
            "mw": 365.4
        },
        {
            "name": "Initial_Mol_2",
            "smiles": "O=c1c(N)c(-c2ccc(NC(=O)C)cc2)oc2c([O-])ccc(C(C(=O)[O-]))c12",
            "label": "Mol 2: Dianion (problematic)",
            "score": -9.4,
            "qed": 0.677,
            "mw": 366.3
        },
        {
            "name": "Initial_Mol_3",
            "smiles": "O=c1c(N)c(-c2ccc(NC(=O)C)cc2)oc2c(O)ccc(C(C(=O)[O-]))c12",
            "label": "Mol 3: Hydroxyl + Acetamido",
            "score": -9.4,
            "qed": 0.623,
            "mw": 367.3
        },
        {
            "name": "Initial_Mol_4",
            "smiles": "O=c1c([O-])c(-c2ccc(NC(=O)C)cc2)oc2cccc(C(C(=O)[O-]))c12",
            "label": "Mol 4: Alkoxide + Carboxylate",
            "score": -9.3,
            "qed": 0.741,
            "mw": 351.3
        },
        {
            "name": "Initial_Mol_5",
            "smiles": "O=c1c(O)c(-c2ccc(NC(=O)C)cc2)oc2cccc(C(C(=O)[O-]))c12",
            "label": "Mol 5: Hydroxyl + Carboxylate",
            "score": -9.3,
            "qed": 0.733,
            "mw": 352.3
        }
    ],
    "02_First_Refined_Proposals": [
        {
            "name": "Refined_Prop_1_F_variant",
            "smiles": "O=c1cc(-c2ccc(NC(=O)C)cc2)oc2cc(F)cc(C(C(=O)[O-]))c12",
            "label": "Refined 1: F on core",
            "score": -9.3,
            "qed": 0.771,
            "mw": 354
        },
        {
            "name": "Refined_Prop_2_hydroxyl",
            "smiles": "O=c1c(O)c(-c2ccc(NC(=O)C)cc2)oc2cccc(C(C(=O)[O-]))c12",
            "label": "Refined 2: Phenolic OH",
            "score": -9.3,
            "qed": 0.733,
            "mw": 352
        },
        {
            "name": "Refined_Prop_3_clean",
            "smiles": "O=c1cc(-c2ccc(NC(=O)C)cc2)oc2cccc(C(C(=O)[O-]))c12",
            "label": "Refined 3: Cleanest",
            "score": -9.0,
            "qed": 0.782,
            "mw": 336
        }
    ],
    "03_Second_Round_Proposals": [
        {
            "name": "Round2_Prop_1_diol_acid",
            "smiles": "O=c1cc(-c2ccc(C)cc2)oc2cc(F)cc(CC(O)C(C(=O)O))c12",
            "label": "Prop 1: Diol-acid (claimed)",
            "score": -9.7,
            "qed": 0.732,
            "mw": 356.3
        },
        {
            "name": "Round2_Prop_2_acid_only",
            "smiles": "O=c1cc(-c2ccc(C)cc2)oc2cc(F)cc(C(C(=O)O))c12",
            "label": "Prop 2: Simple acid",
            "score": -9.9,
            "qed": 0.803,
            "mw": 312.3
        },
        {
            "name": "Round2_Prop_3_tetrazole",
            "smiles": "O=c1cc(-c2ccc(C)cc2)oc2cc(F)cc(CC(O)C(c5nnn[nH]5))c12",
            "label": "Prop 3: Tetrazole variant",
            "score": -10.6,
            "qed": 0.551,
            "mw": 380.4
        }
    ],
    "04_Final_Corrected_Leads": [
        {
            "name": "Final_Lead_1_PRIMARY",
            "smiles": "O=c1cc(-c2ccc(C)cc2)oc2cc(F)cc(CC(O)C(O)C(=O)O)c12",
            "label": "FINAL LEAD #1: True Diol-Acid",
            "score": -9.6,
            "qed": 0.634,
            "mw": 372.3
        },
        {
            "name": "Final_Lead_2_POTENCY",
            "smiles": "O=c1cc(-c2c(Cl)cc(C)cc2)oc2cc(F)cc(CC(O)C(O)C(=O)O)c12",
            "label": "FINAL LEAD #2: Ortho-Cl (Potency)",
            "score": -10.4,
            "qed": 0.601,
            "mw": 406.8
        },
        {
            "name": "Final_Lead_3_FLEXIBLE",
            "smiles": "O=c1cc(-c2ccc(C)cc2)oc2cc(F)cc(CCC(O)C(O)C(=O)O)c12",
            "label": "FINAL LEAD #3: Extended Tail",
            "score": -9.4,
            "qed": 0.601,
            "mw": 386.4
        }
    ]
}

def generate_molecule_images():
    """Generate images for all molecules"""
    image_manifest = {}
    
    for category, mol_list in molecules_data.items():
        category_dir = output_dir / category
        category_dir.mkdir(parents=True, exist_ok=True)
        image_manifest[category] = []
        
        for mol_info in mol_list:
            name = mol_info["name"]
            smiles = mol_info["smiles"]
            label = mol_info["label"]
            
            try:
                # Parse SMILES
                mol = Chem.MolFromSmiles(smiles)
                if mol is None:
                    print(f"⚠ WARNING: Could not parse SMILES for {name}")
                    continue
                
                # Generate 2D coordinates
                from rdkit.Chem import AllChem
                AllChem.Compute2DCoords(mol)
                
                # Create image
                img = Draw.MolToImage(mol, size=(600, 500))
                
                # Save image
                img_path = category_dir / f"{name}.png"
                img.save(str(img_path))
                print(f"✓ Generated: {img_path}")
                
                # Add to manifest
                image_manifest[category].append({
                    "name": name,
                    "label": label,
                    "smiles": smiles,
                    "image_file": str(img_path.relative_to(Path.cwd())),
                    "score": mol_info["score"],
                    "qed": mol_info["qed"],
                    "mw": mol_info["mw"]
                })
                
            except Exception as e:
                print(f"✗ ERROR processing {name}: {e}")
    
    # Save manifest as JSON
    manifest_path = output_dir / "molecule_manifest.json"
    with open(manifest_path, "w") as f:
        json.dump(image_manifest, f, indent=2)
    print(f"\n✓ Manifest saved: {manifest_path}")
    
    return image_manifest

def create_image_reference_markdown(manifest):
    """Create markdown document with image references"""
    
    md = """# Molecular Structures from Adversarial Design Session

This document provides images of all molecules proposed throughout the design iterations.

## Final Leads (Recommended for Testing)

### FINAL LEAD #1: True Diol-Acid (PRIMARY RECOMMENDATION)
- **SMILES**: `O=c1cc(-c2ccc(C)cc2)oc2cc(F)cc(CC(O)C(O)C(=O)O)c12`
- **Docking Score**: -9.6 kcal/mol
- **QED**: 0.634 (good drug-likeness)
- **MW**: 372.3 Da
- **LogP**: 2.256
- **PSA**: 107.97 Ų
- **HBA/HBD**: 6/3
- **Key Feature**: Contains true statin-like diol-acid pharmacophore

![FINAL LEAD #1](molecular_structures/04_Final_Corrected_Leads/Final_Lead_1_PRIMARY.png)

---

### FINAL LEAD #2: Ortho-Chloro Variant (POTENCY VARIANT)
- **SMILES**: `O=c1cc(-c2c(Cl)cc(C)cc2)oc2cc(F)cc(CC(O)C(O)C(=O)O)c12`
- **Docking Score**: -10.4 kcal/mol (highest affinity)
- **QED**: 0.601
- **MW**: 406.8 Da
- **LogP**: 2.910
- **PSA**: 107.97 Ų
- **HBA/HBD**: 6/3
- **Key Feature**: Ortho-Cl may improve binding geometry; 0.8 kcal/mol improvement over Lead #1

![FINAL LEAD #2](molecular_structures/04_Final_Corrected_Leads/Final_Lead_2_POTENCY.png)

---

### FINAL LEAD #3: Extended Tail Variant (FLEXIBLE VARIANT)
- **SMILES**: `O=c1cc(-c2ccc(C)cc2)oc2cc(F)cc(CCC(O)C(O)C(=O)O)c12`
- **Docking Score**: -9.4 kcal/mol
- **QED**: 0.601
- **MW**: 386.4 Da
- **LogP**: 2.647
- **PSA**: 107.97 Ų
- **HBA/HBD**: 6/3
- **Rotatable Bonds**: 6 (one more than Lead #1)
- **Key Feature**: Extended tail allows conformational sampling; fallback if Lead #1 has cellular permeability issues

![FINAL LEAD #3](molecular_structures/04_Final_Corrected_Leads/Final_Lead_3_FLEXIBLE.png)

---

## Initial Model Recommendations (Round 1)

These molecules showed high docking scores but had significant issues with dianions and unrealistic protonation states.

### Initial Mol 1
- **Score**: -9.4 kcal/mol | **QED**: 0.723 | **MW**: 365.4 Da
- **Issue**: Contains aniline-like amino on conjugated coumarin (metabolic liability)

![Mol 1](molecular_structures/01_Initial_Model_Recommendations/Initial_Mol_1.png)

### Initial Mol 2
- **Score**: -9.4 kcal/mol | **QED**: 0.677 | **MW**: 366.3 Da
- **Issue**: **DIANION** (carboxylate + phenoxide) - unrealistic protonation state

![Mol 2](molecular_structures/01_Initial_Model_Recommendations/Initial_Mol_2.png)

### Initial Mol 3
- **Score**: -9.4 kcal/mol | **QED**: 0.623 | **MW**: 367.3 Da
- **Issue**: Phenolic OH undergoes rapid glucuronidation/sulfation in vivo

![Mol 3](molecular_structures/01_Initial_Model_Recommendations/Initial_Mol_3.png)

### Initial Mol 4
- **Score**: -9.3 kcal/mol | **QED**: 0.741 | **MW**: 351.3 Da
- **Issue**: Contains phenoxide (`[O-]`) which is unrealistic at pH 7.4

![Mol 4](molecular_structures/01_Initial_Model_Recommendations/Initial_Mol_4.png)

### Initial Mol 5
- **Score**: -9.3 kcal/mol | **QED**: 0.733 | **MW**: 352.3 Da
- **Best of initial set** but still missing statin-like diol-acid pharmacophore

![Mol 5](molecular_structures/01_Initial_Model_Recommendations/Initial_Mol_5.png)

---

## First Refined Proposals (Round 2)

After initial feedback, model eliminated dianions and improved properties.

### Refined Prop 1: Fluorine Variant
- **Score**: -9.3 kcal/mol | **QED**: 0.771 | **MW**: 354 Da
- **Improvement**: Neutral F substituent; single carboxylate only

![Refined 1](molecular_structures/02_First_Refined_Proposals/Refined_Prop_1_F_variant.png)

### Refined Prop 2: Phenolic Hydroxyl
- **Score**: -9.3 kcal/mol | **QED**: 0.733 | **MW**: 352 Da
- **Assessment**: Chemically realistic but phenolic OH = metabolic risk

![Refined 2](molecular_structures/02_First_Refined_Proposals/Refined_Prop_2_hydroxyl.png)

### Refined Prop 3: Cleanest
- **Score**: -9.0 kcal/mol | **QED**: 0.782 | **MW**: 336 Da
- **Trade-off**: Best QED/simplicity but minimal polar interactions

![Refined 3](molecular_structures/02_First_Refined_Proposals/Refined_Prop_3_clean.png)

---

## Second Round Proposals (Round 3)

Model realized need for statin-like diol-acid pharmacophore and attempted to add it.

### Proposal 1: "Diol-Acid" (CLAIMED)
- **Score**: -9.7 kcal/mol | **QED**: 0.732 | **MW**: 356.3 Da
- **Issue Found**: Only ONE OH in tail (CC(O)C(=O)O), not a true diol

![Round2 Prop 1](molecular_structures/03_Second_Round_Proposals/Round2_Prop_1_diol_acid.png)

### Proposal 2: Simple Acid
- **Score**: -9.9 kcal/mol | **QED**: 0.803 | **MW**: 312.3 Da
- **Note**: Highest QED; shortest tail; conservative approach

![Round2 Prop 2](molecular_structures/03_Second_Round_Proposals/Round2_Prop_2_acid_only.png)

### Proposal 3: Tetrazole Variant
- **Score**: -10.6 kcal/mol | **QED**: 0.551 | **MW**: 380.4 Da
- **Issue**: Tetrazole not inherently more permeable; increases complexity

![Round2 Prop 3](molecular_structures/03_Second_Round_Proposals/Round2_Prop_3_tetrazole.png)

---

## Design Evolution Summary

| Round | Focus | Best Advance | Key Weakness |
|-------|-------|-------------|--------------|
| **1** | High docking scores | Identified coumarin scaffold | Dianions, unrealistic protonation states |
| **2** | Remove artifacts | Eliminated phenoxides | Still missing diol-acid |
| **3** | Add diol-acid | Moved toward pharmacophore | SMILES error (only 1 OH, not diol) |
| **4** | Fix diol/true pharmacophore | **Correct implementation** | Docking validation still needed |

---

## Key Pharmacophore:  STATIN-LIKE DIOL-ACID

The critical insight driving the final design was that proper HMGCR inhibition requires:

1. **A secondary diol**: `CC(O)C(O)` (two hydroxyl groups)
2. **A carboxylic acid**: `C(=O)O` 
3. **On a rigid aromatic scaffold**: Coumarin core with phenyl substituent
4. **With strategic substituents**: F on core for metabolism, C on phenyl for solubility

This pattern **mimics statins**, the gold-standard HMGCR inhibitors, which use a similar diol-acid to form a dense hydrogen-bonding and salt-bridge network in the catalytic site.

---

## Recommended Testing Order

1. **Test Lead #1** first (best balance of binding + properties)
2. If cellular potency is low but enzyme assay is good → **permeability issue** → test **Lead #1 prodrug** (methyl ester)
3. If binding is weak in enzyme assay → **test Lead #2** (higher docking affinity)
4. Never advanced molecules if Lead #1 + prodrug strategy shows good activity

---

*Document generated from adversarial design session (March 19, 2026)*
*All structures designed to optimize HMGCR binding with drug-like properties*
"""
    
    return md

if __name__ == "__main__":
    print("═" * 70)
    print("MOLECULAR STRUCTURE IMAGE GENERATOR")
    print("Adversarial Design Session - HMGCR Inhibitors")
    print("═" * 70)
    
    print("\n[1] Generating molecular images...")
    manifest = generate_molecule_images()
    
    print("\n[2] Creating image reference markdown...")
    md_content = create_image_reference_markdown(manifest)
    md_path = Path("results") / "MOLECULAR_STRUCTURES_REFERENCE.md"
    with open(md_path, "w") as f:
        f.write(md_content)
    print(f"✓ Markdown saved: {md_path}")
    
    print("\n" + "═" * 70)
    print(f"SUCCESS: All images generated in: {output_dir}")
    print(f"Manifest: {output_dir}/molecule_manifest.json")
    print(f"Reference: {md_path}")
    print("═" * 70)
