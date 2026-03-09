import re

# Read the file
with open('llm_preds.txt', 'r') as f:
    content = f.read()

# Split by model sections
sections = re.split(r'(Analysing \w+ ={40,})', content)

# Process sections
output = sections[0]  # Keep the header

for i in range(1, len(sections), 2):
    if i+1 < len(sections):
        section_header = sections[i]
        section_content = sections[i+1]
        
        # Extract all valid scores (non-zero)
        scores = []
        for line in section_content.strip().split('\n'):
            if ':' in line and 'invalid' not in line.lower():
                try:
                    score = float(line.split(':')[-1].strip())
                    if score != 0.0:  # Exclude 0.0 scores
                        scores.append(score)
                except ValueError:
                    pass
        
        # Calculate average
        if scores:
            avg_score = sum(scores) / len(scores)
            avg_line = f'\nAverage score: {avg_score:.2f} (n={len(scores)})\n'
        else:
            avg_line = '\nAverage score: N/A (no valid scores)\n'
        
        output += section_header + '\n' + section_content.strip() + avg_line + '\n'

# Write back to file
with open('llm_preds.txt', 'w') as f:
    f.write(output)

print('Updated file with average scores')
print(f'Processed {(len(sections)-1)//2} model sections')
