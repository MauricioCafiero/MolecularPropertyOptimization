#!/usr/bin/env python3
"""
Generate RDKit molecule images from SMILES strings extracted from the design session.
Images are saved as PNG files for embedding in markdown documentation.
"""

import os
import re
from pathlib import Path
from rdkit import Chem
from rdkit.Chem import Draw, Descriptors

# Output directory for images
OUTPUT_DIR = Path("/workspaces/MolecularPropertyOptimization/results/GPT_FIRST/molecule_images")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Dictionary of molecule SMILES and metadata
# Key: short name / identifier
# Value: {smiles, affinity, properties}

MOLECULES = {
    # Turn 1 - Initial proposals
    "turn1_mol1_tBu_9.0": {
        "smiles": "O=c1cc(-c2ccc(CC(C)(C)C)cc2)oc2cccc(C(C(=O)[O-]))c12",
        "affinity": "-9.0",
        "name": "tert-Butyl variant",
        "description": "tert-Butyl on pendant phenyl (best from scan)"
    },
    "turn1_mol2_phenyl_meta_8.7": {
        "smiles": "O=c1cc(-c2cc(c7ccccc7)ccc2)oc2cccc(C(C(=O)[O-]))c12",
        "affinity": "-8.7",
        "name": "Phenyl extension (meta)",
        "description": "Phenyl growth at meta position"
    },
    "turn1_mol3_phenyl_ortho_8.7": {
        "smiles": "O=c1cc(-c2cccc(c7ccccc7)c2)oc2cccc(C(C(=O)[O-]))c12",
        "affinity": "-8.7",
        "name": "Phenyl extension (ortho)",
        "description": "Phenyl growth at ortho position"
    },
    "turn1_mol4_phenolic_oh_8.8": {
        "smiles": "O=c1cc(-c2c(O)cccc2)oc2cccc(C(C(=O)[O-]))c12",
        "affinity": "-8.8",
        "name": "Phenolic OH variant",
        "description": "Phenolic OH on pendant phenyl"
    },
    
    # Turn 3 - Follow-up exploration
    "turn3_mol_oh_core_9.2": {
        "smiles": "O=c1c(O)c(-c2ccc(CC(C)(C)C)cc2)oc2cccc(C(C(=O)[O-]))c12",
        "affinity": "-9.2",
        "name": "OH on core (best)",
        "description": "Hydroxyl at optimal position on fused core"
    },
    "turn3_mol_f_phenyl_8.9": {
        "smiles": "O=c1cc(-c2ccc(C(C)(C)C)cc2)oc2cccc(C(C(=O)[O-]))c12F",
        "affinity": "-8.9",
        "name": "Fluorine variant",
        "description": "Fluorine on core ring"
    },
    
    # Turn 5 - COOH conversion
    "turn5_champion_cooh_9.2": {
        "smiles": "O=c1c(O)c(-c2ccc(CC(C)(C)C)cc2)oc2cccc(C(C(=O)O))c12",
        "affinity": "-9.2",
        "name": "Champion (COOH form)",
        "description": "Best affinity: core-OH + tBu + COOH (neutral)"
    },
    
    # Turn 5 - Bioisostere exploration
    "turn5_ocf3_bioisostere_9.1": {
        "smiles": "O=c1c(O)c(-c2ccc(OC(F)(F)(F))cc2)oc2cccc(C(C(=O)O))c12",
        "affinity": "-9.1",
        "name": "OCF₃ bioisostere",
        "description": "tBu replacement with OCF₃: improved LogP, -0.1 affinity loss"
    },
    
    # Turn 5 & 6 - Additional replacements
    "turn5_cf3_8.7": {
        "smiles": "O=c1c(O)c(-c2ccc(C(F)(F)(F))cc2)oc2cccc(C(C(=O)O))c12",
        "affinity": "-8.7",
        "name": "CF₃ variant",
        "description": "Plain CF₃ replacement (poor bioisostere)"
    },
    "turn5_ipr_8.7": {
        "smiles": "O=c1c(O)c(-c2ccc(CC(C)C)cc2)oc2cccc(C(C(=O)O))c12",
        "affinity": "-8.7",
        "name": "iPr variant",
        "description": "Isopropyl downsizing (-0.5 penalty)"
    },
    "turn5_me_8.8": {
        "smiles": "O=c1c(O)c(-c2ccc(C)cc2)oc2cccc(C(C(=O)O))c12",
        "affinity": "-8.8",
        "name": "Me variant",
        "description": "Methyl downsizing (best QED 0.776)"
    },
}

def generate_molecule_image(smiles, molecule_id, size=300):
    """
    Generate a PNG image for a single molecule from SMILES.
    
    Args:
        smiles: SMILES string
        molecule_id: unique identifier for filename
        size: image size in pixels
    
    Returns:
        Path to generated image, or None if failed
    """
    try:
        mol = Chem.MolFromSmiles(smiles)
        if mol is None:
            print(f"  ⚠️  Failed to parse SMILES for {molecule_id}")
            return None
        
        # Generate image
        img = Draw.MolToImage(mol, size=(size, size))
        
        # Save image
        output_path = OUTPUT_DIR / f"{molecule_id}.png"
        img.save(str(output_path))
        print(f"  ✓ Generated: {molecule_id}.png")
        return output_path
    except Exception as e:
        print(f"  ✗ Error for {molecule_id}: {e}")
        return None

def generate_comparison_image(smiles_dict, comparison_id, cols=4):
    """
    Generate a grid image comparing multiple molecules.
    
    Args:
        smiles_dict: dict with mol_id -> smiles mappings
        comparison_id: unique identifier for filename
        cols: number of columns in grid
    
    Returns:
        Path to generated image, or None if failed
    """
    try:
        mols = []
        labels = []
        valid_ids = []
        
        for mol_id, smiles in smiles_dict.items():
            mol = Chem.MolFromSmiles(smiles)
            if mol is not None:
                mols.append(mol)
                labels.append(mol_id.replace('turn', 'T').replace('_', '\n'))
                valid_ids.append(mol_id)
            else:
                print(f"  ⚠️  Skipped invalid SMILES: {mol_id}")
        
        if not mols:
            return None
        
        # Generate grid image
        img = Draw.MolsToGridImage(mols, molsPerRow=cols, subImgSize=(250, 250), 
                                   legends=labels, returnPNG=False)
        
        # Save image
        output_path = OUTPUT_DIR / f"{comparison_id}.png"
        img.save(str(output_path))
        print(f"  ✓ Generated comparison: {comparison_id}.png ({len(mols)} molecules)")
        return output_path
    except Exception as e:
        print(f"  ✗ Error for {comparison_id}: {e}")
        return None

def main():
    """Generate all molecule images."""
    print("Generating molecule images from SMILES...\n")
    
    # Generate individual molecule images
    print("Individual molecules:")
    image_index = {}
    for mol_id, mol_data in MOLECULES.items():
        img_path = generate_molecule_image(mol_data["smiles"], mol_id)
        if img_path:
            image_index[mol_id] = {
                "path": str(img_path.relative_to(Path("/workspaces/MolecularPropertyOptimization"))),
                "affinity": mol_data["affinity"],
                "name": mol_data["name"],
                "description": mol_data["description"]
            }
    
    # Generate comparison images by turn
    print("\nComparison grids:")
    
    # Turn 1 - Initial proposals
    turn1_mols = {
        k: v["smiles"] for k, v in MOLECULES.items() 
        if k.startswith("turn1_")
    }
    if turn1_mols:
        generate_comparison_image(turn1_mols, "turn1_initial_proposals", cols=2)
    
    # Turn 3 - Follow-up exploration
    turn3_mols = {
        k: v["smiles"] for k, v in MOLECULES.items()
        if k.startswith("turn3_")
    }
    if turn3_mols:
        generate_comparison_image(turn3_mols, "turn3_followup_exploration", cols=2)
    
    # Turn 5 - Bioisosteres and co-leads
    turn5_mols = {
        k: v["smiles"] for k, v in MOLECULES.items()
        if k.startswith("turn5_")
    }
    if turn5_mols:
        generate_comparison_image(turn5_mols, "turn5_bioisostere_panel", cols=3)
    
    # All champions
    champions = {
        k: v["smiles"] for k, v in MOLECULES.items()
        if any(x in k for x in ["9.2", "9.1"])
    }
    if champions:
        generate_comparison_image(champions, "all_top_leads", cols=2)
    
    # Save index
    print("\nSaving image index...")
    import json
    index_path = OUTPUT_DIR / "image_index.json"
    with open(index_path, "w") as f:
        json.dump(image_index, f, indent=2)
    print(f"  ✓ Index saved: {index_path.relative_to(Path('/workspaces/MolecularPropertyOptimization'))}")
    
    print(f"\n✅ All images saved to: {OUTPUT_DIR.relative_to(Path('/workspaces/MolecularPropertyOptimization'))}")

if __name__ == "__main__":
    main()
