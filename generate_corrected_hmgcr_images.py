#!/usr/bin/env python3
"""
Generate corrected molecular structure images from preliminary analysis
Creates PNG visualizations of the correct HMGCR top molecules for tool-augmented analyses
"""

from rdkit import Chem
from rdkit.Chem import Draw, Descriptors
from pathlib import Path

# Create output directory
output_dir = Path("results/PRELIM_ANALYSIS/preliminary_results_molecules")

# Define corrected HMGCR molecules (tool-augmented analyses)
molecules_data = [
    {
        "name": "gpt_5p2_tools_first_HMGCR_top",
        "smiles": "O=c1cc(-c2ccc(NC(=O)C)cc2)oc2cccc(N(C(=O)))c12",
        "label": "GPT-5p2 Tools (1st) HMGCR\nScore: -9.1",
        "score": -9.1,
        "target": "HMGCR",
        "model": "gpt_5p2_tools_first"
    },
    {
        "name": "gpt_5p2_tools_second_HMGCR_top",
        "smiles": "O=c1cc(-c2cc(F)c(NC(=O)C)cc2)oc2cccc(N(C(=O)))c12",
        "label": "GPT-5p2 Tools (2nd) HMGCR\nScore: -9.2",
        "score": -9.2,
        "target": "HMGCR",
        "model": "gpt_5p2_tools_second"
    }
]

# Generate individual molecule images
print("Generating corrected HMGCR molecule images...")
for mol_data in molecules_data:
    smiles = mol_data["smiles"]
    mol = Chem.MolFromSmiles(smiles)
    
    if mol is not None:
        # Calculate properties
        mw = Descriptors.MolWt(mol)
        logp = Descriptors.MolLogP(mol)
        
        # Create image
        img = Draw.MolToImage(mol, size=(400, 400))
        
        # Save individual image
        img_path = output_dir / f"{mol_data['name']}.png"
        img.save(img_path)
        print(f"✓ Generated: {mol_data['name']}.png (MW: {mw:.1f}, LogP: {logp:.2f})")
    else:
        print(f"✗ Failed to parse SMILES: {mol_data['name']} - {smiles}")

print(f"\nAll images saved to: {output_dir}")
