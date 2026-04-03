#!/usr/bin/env python3
"""
Generate molecular structure images for the Gemini-led HOMO-LUMO gap session.
"""

from rdkit import Chem
from rdkit.Chem import Draw, AllChem
import os

# Define output directory
output_dir = os.path.join(os.path.dirname(__file__), 'molecule_images')
os.makedirs(output_dir, exist_ok=True)

# Top molecules from Gemini session
gemini_molecules = {
    'gemini_best_1': {
        'smiles': 'c1c(S([NH3+]))c2c(S([NH3+]))c3c(S([NH3+]))c4c([N+](=O)[O-])c5c(S([NH3+]))c6c(S([NH3+]))c7ccccc7cc6cc5cc4cc3cc2cc1',
        'gap': 0.8579,
        'description': 'Octacene-5-S([NH3+])-1-NO2 - Best validated'
    },
    'gemini_best_2': {
        'smiles': 'c1ccc2cc3cc4c(C#N)c5c(C#N)c6c(C#N)c7c(C#N)c8ccccc8cc7cc6cc5cc4cc3cc2c1',
        'gap': 1.0,
        'description': 'Tetracyano-octacene - Neutral alternative'
    }
}

def generate_molecule_image(smiles, filename, size=(500, 500)):
    """Generate a 2D molecular structure image from SMILES string."""
    try:
        mol = Chem.MolFromSmiles(smiles)
        if mol is None:
            print(f"Error: Could not parse SMILES: {smiles}")
            return False
        
        AllChem.Compute2DCoords(mol)
        img = Draw.MolToImage(mol, size=size)
        img.save(filename)
        print(f"Generated: {os.path.basename(filename)}")
        return True
    except Exception as e:
        print(f"Error generating image: {e}")
        return False

def main():
    print("Generating Gemini Session Molecular Images")
    print("=" * 50)
    
    for mol_name, mol_data in gemini_molecules.items():
        output_file = os.path.join(output_dir, f"{mol_name}.png")
        print(f"\n{mol_name} (Gap: {mol_data['gap']:.4f} eV)")
        print(f"  {mol_data['description']}")
        generate_molecule_image(mol_data['smiles'], output_file)
    
    print(f"\nImages saved to: {output_dir}")

if __name__ == "__main__":
    main()
