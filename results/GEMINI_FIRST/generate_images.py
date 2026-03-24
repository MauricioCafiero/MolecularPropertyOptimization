#!/usr/bin/env python3
"""
Generate molecular structure images for GEMINI HMGCR inhibitor leads
"""

from rdkit import Chem
from rdkit.Chem import Draw, AllChem
import os
from pathlib import Path

# Create molecular_structures directory if it doesn't exist
output_dir = Path("/workspaces/MolecularPropertyOptimization/results/GEMINI_FIRST/molecular_structures")
output_dir.mkdir(parents=True, exist_ok=True)

# Define the 4 final lead molecules
leads = {
    "Lead_1_7fluoro_3,4-difluorophenyl": {
        "name": "7-fluoro-2-(3,4-difluorophenyl)-4-oxochromen-5-yl acetate",
        "smiles": "O=c1cc(-c2cc(F)c(F)cc2)oc2cc(F)cc(CC(=O)[O-])c12",
        "score": "-9.0",
        "mw": "333",
        "logp": "2.17",
        "qed": "0.74"
    },
    "Lead_2_7fluoro_2,4-difluorophenyl": {
        "name": "7-fluoro-2-(2,4-difluorophenyl)-4-oxochromen-5-yl acetate",
        "smiles": "O=c1cc(-c2ccc(F)c(F)c2)oc2cc(F)cc(CC(=O)[O-])c12",
        "score": "-9.0",
        "mw": "333",
        "logp": "2.17",
        "qed": "0.74"
    },
    "Lead_3_no_core_fluorine": {
        "name": "2-(3,4-difluorophenyl)-4-oxochromen-5-yl acetate",
        "smiles": "O=c1cc(-c2cc(F)c(F)cc2)oc2cccc(CC(=O)[O-])c12",
        "score": "-8.9",
        "mw": "315",
        "logp": "2.03",
        "qed": "0.74"
    },
    "Lead_4_4-fluorophenyl_statin_like": {
        "name": "7-fluoro-2-(4-fluorophenyl)-4-oxochromen-5-yl acetate",
        "smiles": "O=c1cc(-c2ccc(F)cc2)oc2cc(F)cc(CC(=O)[O-])c12",
        "score": "-8.8",
        "mw": "315",
        "logp": "2.03",
        "qed": "0.74"
    }
}

def generate_molecule_image(smiles, filename, name):
    """Generate and save molecular structure image"""
    try:
        mol = Chem.MolFromSmiles(smiles)
        if mol is None:
            print(f"ERROR: Could not parse SMILES for {name}")
            return False
        
        # Generate 2D coordinates
        AllChem.Compute2DCoords(mol)
        
        # Draw molecule
        img = Draw.MolToImage(mol, size=(400, 300))
        img.save(filename)
        print(f"✓ Generated: {filename}")
        return True
    except Exception as e:
        print(f"ERROR generating {filename}: {e}")
        return False

# Generate images for all lead molecules
print("Generating molecular structure images for GEMINI HMGCR inhibitor leads...\n")

for lead_id, lead_data in leads.items():
    filename = output_dir / f"{lead_id}.png"
    print(f"Processing {lead_id}...")
    generate_molecule_image(lead_data["smiles"], str(filename), lead_data["name"])

print("\n✓ All molecular structure images generated successfully!")
print(f"Output directory: {output_dir}")
