#!/usr/bin/env python3
"""
Generate molecular structure images from preliminary analysis
Creates PNG visualizations of the top-scoring molecules
"""

from rdkit import Chem
from rdkit.Chem import Draw, Descriptors
from pathlib import Path
import os

# Create output directory
output_dir = Path("results/preliminary_results_molecules")
output_dir.mkdir(parents=True, exist_ok=True)

# Define top molecules from preliminary analysis
molecules_data = [
    {
        "name": "gpt_5p2_HMGCR_top",
        "smiles": "O=c1cc(-c2ccccc2)oc2cccc(N(S(=O)(=O)C))c12",
        "label": "GPT-5p2 HMGCR\nScore: -8.3",
        "score": -8.3,
        "target": "HMGCR",
        "model": "gpt_5p2"
    },
    {
        "name": "gemini_3_flash_HMGCR_top",
        "smiles": "O=c1cc(-c2ccc(F)cc2)oc2cccc(N(C(=O)))c12",
        "label": "Gemini-3-Flash HMGCR\nScore: -8.7",
        "score": -8.7,
        "target": "HMGCR",
        "model": "gemini_3_flash_preview"
    },
    {
        "name": "anthropic_HMGCR_top",
        "smiles": "O=c1cc(-c2ccc3ccccc3c2)oc2cccc(N(C(=O)))c12",
        "label": "Anthropic HMGCR\nScore: -9.2",
        "score": -9.2,
        "target": "HMGCR",
        "model": "anthropic_hmgcr"
    },
    {
        "name": "gpt_5p2_tools_first_MAOB_top",
        "smiles": "O=c1cc(-c2cc(C(F)(F)(F))c(C#C(C(F)(F)(F)))cc2)oc2ccccc12",
        "label": "GPT-5p2 Tools (1st) MAOB\nScore: -12.2",
        "score": -12.2,
        "target": "MAOB",
        "model": "gpt_5p2_tools_first"
    },
    {
        "name": "gpt_5p2_tools_second_MAOB_top",
        "smiles": "O=c1cc(-c2cc(C(F)(F)(F))c(C#C(C(F)(F)(F)))c(F)c2)oc2ccccc12",
        "label": "GPT-5p2 Tools (2nd) MAOB\nScore: -12.5",
        "score": -12.5,
        "target": "MAOB",
        "model": "gpt_5p2_tools_second"
    }
]

# Generate individual molecule images
print("Generating individual molecule images...")
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

# Generate grid image with all molecules
print("\nGenerating grid image...")
valid_mols = []
valid_labels = []

for mol_data in molecules_data:
    smiles = mol_data["smiles"]
    mol = Chem.MolFromSmiles(smiles)
    
    if mol is not None:
        valid_mols.append(mol)
        # Create label with model and score
        label = f"{mol_data['model']} ({mol_data['target']})\nScore: {mol_data['score']}"
        valid_labels.append(label)

if valid_mols:
    grid_img = Draw.MolsToGridImage(
        valid_mols,
        molsPerRow=3,
        subImgSize=(400, 400),
        legends=valid_labels,
        returnPNG=False
    )
    grid_path = output_dir / "all_prelim_molecules_grid.png"
    grid_img.save(grid_path)
    print(f"✓ Generated grid image: all_prelim_molecules_grid.png")

print(f"\nAll images saved to: {output_dir}")
