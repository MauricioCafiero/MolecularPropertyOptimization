#!/usr/bin/env python3
"""
Generate molecular structure images for the top HOMO-LUMO gap molecules from each model.
"""

from rdkit import Chem
from rdkit.Chem import Draw
import os

# Define output directory
output_dir = r'molecule_images'

# Create output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Dictionary of top molecules from each model (best HOMO-LUMO gap)
top_molecules = {
    'deepseek_hl': 'n1c2ccccc2c(C(=O)O(O))c3ccccc3c1=O',
    'gpt_oss_20b_hl': 'n1c2ccccc2c3ccccc3c1',
    'devstral_hl': 'c1ccc2cc3ccccc3cc2c1(C(=O)N(Cl))',
    'cogito_hl': 'O=C(O)c1ccc2sc3c(c2c1)ccc(C(=O)N(Cl))c3',
    'nemotron_hl': 'c1c(S([NH3+]))cccc1',
    'gemini_hl': 'N#CC=Cc1ccc(-c2c3ccccc3cc4ccccc24)cc1',
    'kimi_hl': 'O=c1c(S([NH3+]))c(-c2ccccc2)oc2ccccc12',
    'gpt5p2_hl': 'N#CC=CCc1ccc2cccc3ccc1c23',
    'claude_hl': 'C1=Cc2ccc3ccccc3c2C1'
}

# HOMO-LUMO gaps for reference
gaps = {
    'deepseek_hl': 3.46,
    'gpt_oss_20b_hl': 7.55,
    'devstral_hl': 5.92,
    'cogito_hl': 7.57,
    'nemotron_hl': 9.50,
    'gemini_hl': 5.95,
    'kimi_hl': 7.53,
    'gpt5p2_hl': 7.08,
    'claude_hl': 7.34
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
        
        # Draw molecule with larger font for better visibility
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
    print("Generating HOMO-LUMO Gap Molecular Structure Images")
    print("=" * 80)
    
    success_count = 0
    total_count = len(top_molecules)
    
    for model_name, smiles in top_molecules.items():
        output_file = os.path.join(output_dir, f"{model_name}_top.png")
        gap = gaps[model_name]
        
        print(f"\n{model_name} (Gap: {gap:.2f} eV):")
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
            file_size = os.path.getsize(output_file) / 1024  # KB
            print(f"  ✓ {model_name}_top.png ({file_size:.1f} KB)")
        else:
            print(f"  ✗ {model_name}_top.png (missing)")
    
    print("\n" + "=" * 80)
    print("Gap Summary:")
    print("=" * 80)
    sorted_gaps = sorted(gaps.items(), key=lambda x: x[1])
    print(f"{'Model':<25} {'HOMO-LUMO Gap (eV)':<20}")
    print("-" * 45)
    for model, gap in sorted_gaps:
        print(f"{model:<25} {gap:>8.2f} eV")
    
    print("\n" + "=" * 80)
    print(f"Widest Gap:  {sorted_gaps[-1][0]} ({sorted_gaps[-1][1]:.2f} eV)")
    print(f"Narrowest Gap: {sorted_gaps[0][0]} ({sorted_gaps[0][1]:.2f} eV)")
    print(f"Gap Range: {sorted_gaps[-1][1] - sorted_gaps[0][1]:.2f} eV")
    print("=" * 80)

if __name__ == "__main__":
    main()
