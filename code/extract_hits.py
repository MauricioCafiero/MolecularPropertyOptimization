#read filename from command line
import sys

filename = sys.argv[1]

with open(filename, 'r') as f:
    lines = f.readlines()

extracted_lines = []
for line in lines:
    #if line starts with 'Best score: ', extract the score and the smiles string
    if line.startswith('=========== New best'):
        extracted_lines.append(line)

with open('extracted_hits.txt', 'w') as f:
    for line in extracted_lines:
        f.write(line)