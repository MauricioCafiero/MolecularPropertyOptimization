#!/usr/bin/env python3
"""
Generate molecular structure images for the top molecules from each model in the one-shot experiment.
"""

from rdkit import Chem
from rdkit.Chem import Draw
import os

# Define output directory
output_dir = 'molecule_images'

# Create output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Dictionary of top molecules from each model
top_molecules = {
    'deepseek': 'O=c1cc(-c2cccc(C(C(=O)[O-]))c2)oc2cccc(C=C([N+](=O)[O-]))c12',
    'gpt_oss_120b': 'O=c1c(C(=O)[O-])c(-c2ccc(C(=O)[O-])cc2)oc2cccc(C(=O)[O-])c12',
    'gpt_oss_20b': 'O=c1c(O(C#N))c(-c2cc(C(C(=O)[O-]))ccc2)oc2ccccc12',
    'devstral': 'O=c1cc(-c2ccccc2)oc2cccc(C(C(=O)[O-]))c12',
    'cogito': 'O=c1cc(-c2cccc(C(C(=O)[O-]))c2)oc2cccc(C(C(=O)[O-]))c12',
    'nemotron': 'c1c2c(ccccc2)c(ccccc1)C(=O)Oc3ccccc3C(=O)Oc4ccccc4',
    'gemini': '[O-]C(=O)Cc1cccc2oc(cc(=O)c12)-c3ccc4ccccc4c3',
    'kimi': 'O=C(O)C(C(=O)O)c1cc2cc3cc4ccccc4cc3cc2o1',
    'gpt5p2': 'O=c1cc(-c2ccc(C=C([N+](=O)[O-]))cc2)oc2cccc(C(C(=O)[O-]))c12',
    'claude': 'O=c1cc(-c2cc3ccccc3cc2C(=O)[O-])oc2c(C(C(=O)[O-]))ccc(C(=O)[O-])c12'
}

# Scores for reference
scores = {
    'deepseek': -8.2,
    'gpt_oss_120b': -7.9,
    'gpt_oss_20b': -7.5,
    'devstral': -8.6,
    'cogito': -8.5,
    'nemotron': -9.1,
    'gemini': -9.2,
    'kimi': -7.5,
    'gpt5p2': -8.9,
    'claude': -9.0
}

def generate_molecule_image(smiles, filename, size=(400, 400)):
    """
    Generate a 2D molecular structure image from SMILES string.
    
    Args:
        smiles: SMILES string
        filename: Output filename (including path)
        size: Image size as (width, height) tuple
    """
    try:
        mol = Chem.MolFromSmiles(smiles)
        if mol is None:
            print(f"Error: Could not parse SMILES: {smiles}")
            return False
        
        # Generate 2D coordinates
        from rdkit.Chem import AllChem
        AllChem.Compute2DCoords(mol)
        
        # Draw molecule
        img = Draw.MolToImage(mol, size=size)
        
        # Save image
        img.save(filename)
        print(f"✓ Generated: {filename}")
        return True
        
    except Exception as e:
        print(f"✗ Error generating image for {filename}: {e}")
        return False

def main():
    print("=" * 80)
    print("Generating molecular structure images for top molecules")
    print("=" * 80)
    
    success_count = 0
    total_count = len(top_molecules)
    
    for model_name, smiles in top_molecules.items():
        output_file = os.path.join(output_dir, f"{model_name}_top.png")
        score = scores[model_name]
        
        print(f"\n{model_name} (Score: {score}):")
        print(f"  SMILES: {smiles}")
        
        if generate_molecule_image(smiles, output_file):
            success_count += 1
    
    print("\n" + "=" * 80)
    print(f"Summary: {success_count}/{total_count} images generated successfully")
    print("=" * 80)
    
    # List all generated files
    print("\nGenerated files:")
    for model_name in top_molecules.keys():
        output_file = os.path.join(output_dir, f"{model_name}_top.png")
        if os.path.exists(output_file):
            print(f"  ✓ {model_name}_top.png")
        else:
            print(f"  ✗ {model_name}_top.png (missing)")

if __name__ == "__main__":
    main()
