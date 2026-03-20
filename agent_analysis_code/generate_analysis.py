#!/usr/bin/env python3
"""
Generate RDKit images for HMGCR design session analysis
"""

from rdkit import Chem
from rdkit.Chem import Draw
import os
from pathlib import Path

# Create results subdirectory for images
img_dir = Path("/workspaces/MolecularPropertyOptimization/results/molecular_images")
img_dir.mkdir(exist_ok=True)

# Dictionary of key molecules from the design session
molecules = {
    # Turn 1 - Initial Model Proposals
    "turn1_mol1": {
        "smiles": "O=c1cc(-c2ccccc2)oc2c(C(C(=O)[O-]))cc(C=C([N+](=O)[O-]))cc12",
        "name": "Turn 1 - Molecule 1: Carboxylate + nitro-alkenyl",
        "dock": "-9.0 to -9.4",
        "turn": 1
    },
    "turn1_mol2": {
        "smiles": "O=c1cc(-c2ccccc2)oc2c(C(C(=O)[O-]))cc(O(C#N))cc12",
        "name": "Turn 1 - Molecule 2: Carboxylate + cyano-alkoxy",
        "dock": "-8.8 to -9.2",
        "turn": 1
    },
    
    # Turn 3 - Phase 1 Results (A-F)
    "turn3_A": {
        "smiles": "O=c1cc(-c2ccccc2)oc2cccc(C(C(=O)[O-]))c12",
        "name": "Turn 3 - Lead A: Original best hit",
        "dock": "-8.6",
        "turn": 3
    },
    "turn3_B": {
        "smiles": "O=c1cc(-c2cc(Cl)ccc2)oc2cccc(C(C(=O)[O-]))c12",
        "name": "Turn 3 - Molecule B: Cl on pendant phenyl",
        "dock": "-8.6",
        "turn": 3
    },
    "turn3_C": {
        "smiles": "O=c1cc(-c2ccc(C#N)cc2)oc2cccc(C(C(=O)[O-]))c12",
        "name": "Turn 3 - Molecule C: CN on pendant phenyl",
        "dock": "-8.6",
        "turn": 3
    },
    "turn3_D": {
        "smiles": "O=c1cc(-c2cc(F)ccc2)oc2cccc(C(C(=O)[O-]))c12",
        "name": "Turn 3 - Molecule D: F on pendant phenyl",
        "dock": "-8.6",
        "turn": 3
    },
    
    # Turn 5 - Phase 2b (Molecule G - breakthrough)
    "turn5_G": {
        "smiles": "O=c1cc(-c2cc(Cl)ccc2)oc2cccc(CCc1ccccc1C(C(=O)[O-]))c12",
        "name": "Turn 5 - Molecule G: BREAKTHROUGH benzyl-phenylacetic acid",
        "dock": "-9.1",
        "turn": 5
    },
    
    # Turn 7 - Phase 2c (-9.5 variants)
    "turn7_1": {
        "smiles": "O=c1cc(-c2c(F)c(Cl)ccc2)oc2cccc(CCc1ccccc1C(C(=O)[O-]))c12",
        "name": "Turn 7 - Candidate 1: Best -9.3 variant",
        "dock": "-9.3",
        "turn": 7,
        "logp": "4.434"
    },
    "turn7_best": {
        "smiles": "O=c1cc(-c2c(F)c(Cl)ccc2)oc2ccc(Cl)c(CCc1ccccc1C(C(=O)[O-]))c12",
        "name": "Turn 7 - -9.5 Variant A (demoted): Extra Cl on xanthone",
        "dock": "-9.5",
        "turn": 7,
        "logp": "5.087",
        "status": "DEMOTED (LogP > 5.0)"
    },
    "turn7_B": {
        "smiles": "O=c1cc(-c2c(F)c(Cl)ccc2)oc2ccc(C)c(CCc1ccccc1C(C(=O)[O-]))c12",
        "name": "Turn 7 - Variant B: FINAL LEAD (Me on xanthone)",
        "dock": "-9.5",
        "turn": 7,
        "logp": "4.742",
        "qed": "0.678",
        "status": "✓ SELECTED"
    },
    "turn7_C": {
        "smiles": "O=c1cc(-c2c(F)c(Cl)ccc2)oc2cccc(CCc1cc(C)ccc1C(C(=O)[O-]))c12",
        "name": "Turn 7 - Variant C: Me on appended phenyl",
        "dock": "-9.5",
        "turn": 7,
        "logp": "4.824",
        "status": "Backup"
    },
    
    # Turn 13 - Pyridine substitution (LogP improvement)
    "turn13_pyridine1": {
        "smiles": "O=c1cc(-c2c(F)c(Cl)ccc2)oc2ccc(C)c(CCc1ncccc1C(C(=O)[O-]))c12",
        "name": "Turn 13 - Pyridine Variant 1: ADME-improved lead",
        "dock": "-9.3",
        "turn": 13,
        "logp": "4.214",
        "qed": "0.701",
        "status": "✓ ADME-OPTIMIZED"
    },
    "turn13_pyridine2": {
        "smiles": "O=c1cc(-c2c(F)c(Cl)ccc2)oc2ccc(C)c(CCc1ccncc1C(C(=O)[O-]))c12",
        "name": "Turn 13 - Pyridine Variant 2: Alternate isomer",
        "dock": "-9.2",
        "turn": 13,
        "logp": "4.214",
        "qed": "0.701"
    },
}

# Generate images
generated = {}
for mol_id, mol_data in molecules.items():
    try:
        smiles = mol_data["smiles"]
        mol = Chem.MolFromSmiles(smiles)
        if mol is not None:
            img = Draw.MolToImage(mol, size=(400, 300))
            img_path = img_dir / f"{mol_id}.png"
            img.save(img_path)
            generated[mol_id] = str(img_path)
            print(f"✓ Generated: {mol_id}")
        else:
            print(f"✗ Invalid SMILES for {mol_id}: {smiles}")
    except Exception as e:
        print(f"✗ Error generating {mol_id}: {e}")

print(f"\nTotal images generated: {len(generated)}")
print(f"Images saved to: {img_dir}")
