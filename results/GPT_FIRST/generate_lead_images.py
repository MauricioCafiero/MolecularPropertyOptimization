#!/usr/bin/env python3
"""
Generate individual molecular structure images for GPT_FIRST leads
"""

from rdkit import Chem
from rdkit.Chem import Draw, AllChem
from pathlib import Path

# Create molecule_images directory if it doesn't exist
output_dir = Path("/workspaces/MolecularPropertyOptimization/results/GPT_FIRST/molecule_images")
output_dir.mkdir(parents=True, exist_ok=True)

# Define GPT leads
molecules = {
    "Lead_A_tBu_maximum_affinity": {
        "smiles": "O=c1c(O)c(-c2ccc(CC(C)(C)C)cc2)oc2cccc(C(C(=O)O))c12",
        "score": "-9.2"
    },
    "Lead_B_OCF3_optimized_balance": {
        "smiles": "O=c1c(O)c(-c2ccc(OC(F)(F)(F))cc2)oc2cccc(C(C(=O)O))c12",
        "score": "-9.1"
    }
}

# Generate images
print("Generating GPT lead molecular structure images...")

for mol_key, mol_data in molecules.items():
    try:
        mol = Chem.MolFromSmiles(mol_data["smiles"])
        if mol is not None:
            AllChem.Compute2DCoords(mol)
            img = Draw.MolToImage(mol, size=(400, 400))
            
            img_filename = f"{mol_key}.png"
            img_path = output_dir / img_filename
            img.save(img_path)
            
            print(f"✓ Generated: {mol_key}")
        else:
            print(f"✗ Failed to parse SMILES for {mol_key}")
    except Exception as e:
        print(f"✗ Error generating {mol_key}: {e}")

print("Done!")
