import sqlite3
import re

# SMILES pattern matching
smiles_pattern = r'[CHONFClBrISPKacnosp0-9@+\-\[\]\(\)\/.=#$%]{5,}'

def insert_QED_aLogP(filename: str):
    """Extract QED and aLogP values from dock_zero_verify_lipinski.out and insert into database"""
    qed_alogp_list = []
    
    with open(filename, 'r', encoding='utf-8', errors='ignore') as f:
        lines = f.readlines()
        print(f"Total lines read: {len(lines)}")
        
        i = 0
        while i < len(lines):
            line = lines[i]
            
            # Look for lines with SMILES and docking score (first line)
            if ':' in line and 'docking score' in line:
                # Extract SMILES from this line
                parts = line.split(':')
                smiles_part = parts[0].strip()
                match = re.search(smiles_pattern, smiles_part)
                
                if match:
                    smiles = match.group(0)
                    
                    # Check the next line for aLogP and QED
                    if i + 1 < len(lines):
                        next_line = lines[i + 1]
                        
                        # Extract aLogP value
                        alogp_match = re.search(r'aLogP\s*=\s*([-\d.]+)', next_line)
                        # Extract QED value
                        qed_match = re.search(r'QED\s*=\s*([-\d.]+)', next_line)
                        
                        if alogp_match and qed_match:
                            alogp = float(alogp_match.group(1))
                            qed = float(qed_match.group(1))
                            
                            qed_alogp_list.append({
                                'SMILES': smiles,
                                'QED': qed,
                                'aLogP': alogp
                            })
                            print(f"Found QED={qed}, aLogP={alogp} for SMILES: {smiles}")
            
            i += 1
    
    # Insert QED and aLogP into database
    conn = sqlite3.connect('../data/gen_molecules.db')
    c = conn.cursor()
    
    for entry in qed_alogp_list:
        smiles = entry['SMILES']
        qed = entry['QED']
        alogp = entry['aLogP']
        
        c.execute('''
            UPDATE molecules
            SET QED = ?, aLogP = ?
            WHERE SMILES = ?
        ''', (qed, alogp, smiles))
    
    conn.commit()
    conn.close()
    
    print(f"Inserted QED and aLogP values for {len(qed_alogp_list)} molecules")
