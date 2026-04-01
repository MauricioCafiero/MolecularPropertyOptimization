#!/usr/bin/env python3
"""
Generate molecular structure images for ANT_FIRST HMGCR inhibitor leads
Includes all molecules tested, from high-scoring finalists to lower-scoring candidates
"""

from rdkit import Chem
from rdkit.Chem import Draw, AllChem, Descriptors
import os
from pathlib import Path

# Create molecular_structures directory if it doesn't exist
output_dir = Path("/workspaces/MolecularPropertyOptimization/results/ANT_FIRST/molecular_structures")
output_dir.mkdir(parents=True, exist_ok=True)

# Define all molecules from the session
# Organized by category: Final Proposals, Earlier Proposals, Alternative Variants

molecules = {
    "FINAL_PROPOSALS": {
        "Rank_1_Best_Affinity": {
            "name": "2-(2-methylphenyl)-4-oxochromen-7-ylmethyl carbamate",
            "smiles": "O=c1c(O)c(-c2c(C)cc(C(=O)N)cc2)oc2c(F)ccc(C(=O)N)c12",
            "score": "-9.2",
            "qed": "0.657",
            "mw": "356.3",
            "logp": "1.811",
            "psa": "136.6",
            "hbd": "3",
            "hba": "5",
            "category": "FINAL_BEST_AFFINITY"
        },
        "Rank_2_Balanced": {
            "name": "2-(2-methylphenyl)-7-(N,N-dimethylcarbamoyl)chromone",
            "smiles": "O=c1c(O)c(-c2c(C)cc(C(=O)N(C)C)cc2)oc2c(F)ccc(C(=O)N)c12",
            "score": "-8.6",
            "qed": "0.720",
            "mw": "384.4",
            "logp": "2.414",
            "psa": "113.8",
            "hbd": "2",
            "hba": "5",
            "category": "FINAL_BALANCED"
        },
        "Rank_3_Best_Permeability": {
            "name": "2-(2-methylphenyl)-7,4-di(N,N-dimethylcarbamoyl)chromone",
            "smiles": "O=c1c(O)c(-c2c(C)cc(C(=O)N(C)C)cc2)oc2c(F)ccc(C(=O)N(C)C)c12",
            "score": "-8.3",
            "qed": "0.714",
            "mw": "412.4",
            "logp": "3.017",
            "psa": "91.1",
            "hbd": "1",
            "hba": "5",
            "category": "FINAL_PERMEABLE"
        }
    },
    
    "HIGH_SCORING_VARIANTS": {
        "CF3_substituent_Rank1": {
            "name": "2-(carboxyphenyl)-7-(trifluoromethyl)chromone-amide",
            "smiles": "O=c1c(O)c(-c2c(C(=O)[O-])c(NC(=O)C)ccc2)oc2c(C(F)(F)(F))ccc(C(=O)N)c12",
            "score": "-9.4",
            "qed": "0.545",
            "mw": "449.3",
            "logp": "1.605",
            "psa": "162.8",
            "hbd": "3",
            "hba": "7",
            "category": "HIGH_SCORE_CF3"
        },
        "Nitrile_variant": {
            "name": "2-(cyano-carboxyphenyl)-7-CF3chromone-amide",
            "smiles": "O=c1c(O)c(-c2c(C(=O)[O-])c(NC(=O)C)cc(C#N)cc2)oc2c(C(F)(F)(F))ccc(C(=O)N)c12",
            "score": "-9.1",
            "qed": "0.487",
            "mw": "474.3",
            "logp": "2.1",
            "psa": "176.5",
            "hbd": "3",
            "hba": "7",
            "category": "HIGH_SCORE_NITRILE"
        },
        "Dianion_reference": {
            "name": "2-(carboxyphenyl)-4,7-dicarboxychromone",
            "smiles": "O=c1c(O)c(-c2c(C(=O)[O-])c(NC(=O)C)ccc2)oc2c(C(=O)[O-])ccc(C(C))c12",
            "score": "-9.2",
            "qed": "0.598",
            "mw": "409.3",
            "logp": "-0.4",
            "psa": "179.6",
            "hbd": "1",
            "hba": "7",
            "category": "HIGH_SCORE_DIANION"
        }
    },
    
    "MEDIUM_SCORING_VARIANTS": {
        "Para_phenyl_amide_Fluorine": {
            "name": "2-(4-carbamoylphenyl)-7-fluorochromone-2-ol",
            "smiles": "O=c1c(O)c(-c2ccc(C(=O)N)cc2)oc2c(F)ccc(C(=O)N)c12",
            "score": "-8.9",
            "qed": "0.662",
            "mw": "342.3",
            "logp": "1.503",
            "psa": "136.6",
            "hbd": "3",
            "hba": "5",
            "category": "MEDIUM_PARA_AMIDE"
        },
        "Para_phenyl_amide_Chlorine": {
            "name": "2-(4-carbamoylphenyl)-7-chlorochromone-2-ol",
            "smiles": "O=c1c(O)c(-c2ccc(C(=O)N)cc2)oc2c(Cl)ccc(C(=O)N)c12",
            "score": "-8.9",
            "qed": "0.657",
            "mw": "358.7",
            "logp": "2.017",
            "psa": "136.6",
            "hbd": "3",
            "hba": "5",
            "category": "MEDIUM_PARA_AMIDE_CL"
        },
        "CF3_on_phenyl": {
            "name": "2-(trifluoromethyl-carbamoylphenyl)-7-fluorochromone",
            "smiles": "O=c1c(O)c(-c2cc(C(F)(F)(F))c(C(=O)N)cc2)oc2c(F)ccc(C(=O)N)c12",
            "score": "-8.9",
            "qed": "0.570",
            "mw": "410.3",
            "logp": "2.521",
            "psa": "136.6",
            "hbd": "3",
            "hba": "5",
            "category": "MEDIUM_CF3_PHENYL"
        }
    },
    
    "LOW_TO_MEDIUM_SCORING": {
        "Ortho_carboxylate_Chlorofluoro": {
            "name": "2-(2-carboxyphenyl)-5-fluoro-4-chlorochromone carboxylic acid",
            "smiles": "O=c1cc(-c2c(C(=O)[O-])cc(F)c(Cl)c2)oc2cccc(C(C(=O)[O-]))c12",
            "score": "-9.1",
            "qed": "0.671",
            "mw": "374.7",
            "logp": "0.908",
            "psa": "180.0",
            "hbd": "0",
            "hba": "7",
            "category": "LOW_DIANION_1"
        },
        "Ortho_carboxylate_Fluoroiodo": {
            "name": "2-(2-carboxyphenyl)-5-fluoro-4-iodochromone carboxylic acid",
            "smiles": "O=c1cc(-c2c(C(=O)[O-])cc(F)c(I)c2)oc2cccc(C(C(=O)[O-]))c12",
            "score": "-9.1",
            "qed": "0.528",
            "mw": "466.2",
            "logp": "1.312",
            "psa": "180.0",
            "hbd": "0",
            "hba": "7",
            "category": "LOW_DIANION_IODO"
        },
        "Ortho_carboxylate_Fluorobromo": {
            "name": "2-(2-carboxyphenyl)-5-fluoro-4-bromochromone carboxylic acid",
            "smiles": "O=c1cc(-c2c(C(=O)[O-])cc(F)c(Br)c2)oc2cccc(C(C(=O)[O-]))c12",
            "score": "-9.1",
            "qed": "0.625",
            "mw": "419.2",
            "logp": "1.017",
            "psa": "180.0",
            "hbd": "0",
            "hba": "7",
            "category": "LOW_DIANION_BR"
        },
        "Ortho_carboxylate_Fluoroonly": {
            "name": "2-(2-carboxyphenyl)-5-fluorochromone carboxylic acid",
            "smiles": "O=c1cc(-c2c(C(=O)[O-])cc(F)cc2)oc2cccc(C(C(=O)[O-]))c12",
            "score": "-8.9",
            "qed": "0.673",
            "mw": "340.3",
            "logp": "0.255",
            "psa": "180.0",
            "hbd": "0",
            "hba": "7",
            "category": "LOW_DIANION_SIMPLE"
        }
    },
    
    "EARLY_PROPOSALS_CRITIQUED": {
        "Monoanionic_hydroxyl_acetamide_v1": {
            "name": "2-hydroxy-7-(carboxyphenyl) chromone with acetamide and ortho-fluorine",
            "smiles": "O=c1c(O)c(-c2c(C(=O)[O-])c(NC(=O)C)c(F)cc2)oc2cc(F)cc(C)c12",
            "score": "-9.9",
            "qed": "0.709",
            "mw": "388.3",
            "logp": "2.07",
            "psa": "119.7",
            "hbd": "2",
            "hba": "6",
            "category": "EARLY_MONOANIONIC_V1"
        },
        "Monoanionic_hydroxyl_acetamide_v2": {
            "name": "2-hydroxy-7-(carboxyphenyl) chromone with acetamide and 3-fluorine",
            "smiles": "O=c1c(O)c(-c2c(C(=O)[O-])c(NC(=O)C)c(F)cc2)oc2ccc(F)c(C)c12",
            "score": "-9.9",
            "qed": "0.709",
            "mw": "388.3",
            "logp": "2.07",
            "psa": "119.7",
            "hbd": "2",
            "hba": "6",
            "category": "EARLY_MONOANIONIC_V2"
        },
        "Monoanionic_hydroxyl_acetamide_chlorine": {
            "name": "2-hydroxy-7-(carboxyphenyl) chromone with acetamide and 3-chlorine",
            "smiles": "O=c1c(O)c(-c2c(C(=O)[O-])c(NC(=O)C)c(F)cc2)oc2ccc(Cl)c(C)c12",
            "score": "-9.9",
            "qed": "0.692",
            "mw": "404.8",
            "logp": "2.59",
            "psa": "119.7",
            "hbd": "2",
            "hba": "6",
            "category": "EARLY_MONOANIONIC_CL"
        }
    }
}

# Generate images for each molecule
print("Generating molecular structure images...")

for category_name, category_mols in molecules.items():
    for mol_key, mol_data in category_mols.items():
        try:
            mol = Chem.MolFromSmiles(mol_data["smiles"])
            if mol is not None:
                # Generate 2D coordinates
                AllChem.Compute2DCoords(mol)
                
                # Create image
                img = Draw.MolToImage(mol, size=(400, 400))
                
                # Save image
                img_filename = f"{mol_key}.png"
                img_path = output_dir / img_filename
                img.save(img_path)
                
                print(f"✓ Generated: {mol_key}")
            else:
                print(f"✗ Failed to parse SMILES for {mol_key}")
        except Exception as e:
            print(f"✗ Error generating image for {mol_key}: {e}")

print(f"\nAll images saved to: {output_dir}")
print(f"Total molecules processed: {sum(len(cat) for cat in molecules.values())}")
