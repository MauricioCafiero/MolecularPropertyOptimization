#!/usr/bin/env python3
"""
Generate molecular structure images for the GPT 5.2-led HOMO-LUMO gap session.
"""

from rdkit import Chem
from rdkit.Chem import Draw, AllChem
import os

# Define output directory
output_dir = os.path.join(os.path.dirname(__file__), 'molecule_images')
os.makedirs(output_dir, exist_ok=True)

# Top molecules from GPT session
gpt_molecules = {
    'gpt_best_1': {
        'smiles': 'c1(C#CC#N)ccc2c(C#C(C#N))c3c(C#C(C#N))cc(C#CC#N)c(C#CC#N)c3c(C#Cc7ccc8cc9ccccc9cc8c7)c2c1',
        'gap': 3.95,
        'description': 'No-ester, 5 nitrile-alkynes - Best practical'
    },
    'gpt_best_2': {
        'smiles': 'c1(C#CC(=O)OC)ccc2c(C#C(C#N))c3c(C#C(C#N))cc(C#CC#N)c(C#CC#N)c3c(C#Cc7ccc8cc9ccccc9cc8c7)c2c1',
        'gap': 4.04,
        'description': 'Constrained growth with 4 nitrile-alkynes'
    },
    'gpt_best_3': {
        'smiles': 'c1(C#CC(=O)OC)ccc2c(C#C(OC(=O)C))c3ccc(C#CC#N)c(C#CC#N)c3c(C#Cc7ccc8cc9ccccc9cc8c7)c2c1',
        'gap': 4.55,
        'description': 'Dual nitrile-alkyne optimized positioning'
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
    print("Generating GPT 5.2 Session Molecular Images")
    print("=" * 50)
    
    for mol_name, mol_data in gpt_molecules.items():
        output_file = os.path.join(output_dir, f"{mol_name}.png")
        print(f"\n{mol_name} (Gap: {mol_data['gap']:.2f} eV)")
        print(f"  {mol_data['description']}")
        generate_molecule_image(mol_data['smiles'], output_file)
    
    print(f"\nImages saved to: {output_dir}")

if __name__ == "__main__":
    main()
