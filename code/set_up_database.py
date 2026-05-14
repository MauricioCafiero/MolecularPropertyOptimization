import sqlite3
from all_mol_lists import *
import re

def set_up_database():
    conn = sqlite3.connect('../data/gen_molecules.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS molecules (
            id INTEGER PRIMARY KEY,
            model_mode_name TEXT NOT NULL,
            SMILES TEXT NOT NULL,
            Score REAL,
            QED REAL,
            aLogP REAL,
            SAS REAL,
            NP REAL
        )
    ''')
    conn.commit()
    conn.close()    
    print("Database setup complete.")

smiles_pattern = r'[CHONFClBrISPKacnosp0-9@+\-\[\]\(\)\/.=#$%]{5,}'

def insert_SAS_NP():
    SAS_list = []
    NP_list = []

    with open('../results/SAS_NP_all.txt', 'r', encoding='utf-8', errors='ignore') as f:
        lines = f.readlines()
        print(f"Total lines read: {len(lines)}")
        for line in lines:
            parts = line.split()
            try:
                matches = re.findall(smiles_pattern, parts[1])
            except:
                matches = None
            if matches:
                try:
                    SAS = float(parts[3])
                    NP = float(parts[5])
                except:
                    SAS = -999
                    NP = -999
                SAS_list.append(SAS)
                NP_list.append(NP)

    #insert SAS and NP into database
    conn = sqlite3.connect('../data/gen_molecules.db')
    c = conn.cursor()
    c.execute('SELECT id FROM molecules')
    rows = c.fetchall()
    for i, row in enumerate(rows):
        id = row[0]
        if i < len(SAS_list):
            SAS = SAS_list[i]
            NP = NP_list[i]
            c.execute('''
                UPDATE molecules
                SET SAS = ?, NP = ?
                WHERE id = ?
            ''', (SAS, NP, id))
    conn.commit()
    conn.close()

def initial_setup():
    print("Inserting model mode names and SMILES values into the database...")
    for name, smiles_list in hash_lists.items():
        print(f"Inserting {len(smiles_list)} molecules for model mode: {name}")
        conn = sqlite3.connect('../data/gen_molecules.db')
        c = conn.cursor()
        for smiles in smiles_list:
            c.execute('''
                INSERT INTO molecules (model_mode_name, SMILES)
                VALUES (?, ?)
            ''', (name, smiles))
        conn.commit()
        conn.close()

    print("Inserting SAS and NP values into the database...")
    insert_SAS_NP()

def insert_scores(filename: str, score_index: int):
    pairs = []
    with open(filename, 'r') as f:
        lines = f.readlines()
        print(f"Total lines read: {len(lines)}")
        for line in lines:
            parts = line.split()
            try:
                match = re.search(smiles_pattern, parts[0])
                #print(match)
                if match is not None and len(parts) > score_index:
                    score = parts[score_index]
                    smiles = match.group(0)
                    pair_dict = {"SMILES": smiles, "Score": score}
                    pairs.append(pair_dict)
                    print(f"Found score: {score} for SMILES: {smiles}")
            except:
                pass

    # add scores to database for matching SMILES
    conn = sqlite3.connect('../data/gen_molecules.db')
    c = conn.cursor()
    for pair in pairs:
        smiles = pair["SMILES"]
        score = pair["Score"]
        c.execute('''
            UPDATE molecules
            SET Score = ?
            WHERE SMILES = ?
        ''', (score, smiles))
    conn.commit()
    conn.close()

print("Setting up the database...")
#set_up_database()
#initial_setup()
#insert_scores('../results/ZERO_SHOT/dock_zero_verify_lipinski.out', 5)

#print all columns where score < -9.0
conn = sqlite3.connect('../data/gen_molecules.db')
c = conn.cursor()
c.execute('SELECT * FROM molecules WHERE Score < -9.0')
rows = c.fetchall()
print(f"Total rows with Score < -9.0: {len(rows)}")
for row in rows:
    print(row)
conn.close()

#print table
print_flag = False
if print_flag:
    conn = sqlite3.connect('../data/gen_molecules.db')
    c = conn.cursor()
    c.execute('SELECT * FROM molecules WHERE Score is not null')
    rows = c.fetchall()
    print(f"Total rows with non-null scores: {len(rows)}")
    for row in rows:
        print(row)
    conn.close()
