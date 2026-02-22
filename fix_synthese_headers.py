import glob
import os

for file in glob.glob('*/Synthese_*.md'):
    with open(file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    new_lines = []
    for line in lines:
        if line.startswith('#### '):
            new_lines.append('#' + line)
        elif line.startswith('### '):
            new_lines.append('#' + line)
        elif line.startswith('## '):
            lower_line = line.lower()
            if 'cours ' in lower_line or 'chapitre' in lower_line:
                new_lines.append(line)
            else:
                new_lines.append('#' + line)
        else:
            new_lines.append(line)
            
    with open(file, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)

# Fix Exercices
for file in glob.glob('*/Exercices_*.md'):
    with open(file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        
    new_lines = []
    in_cours_1_2 = False
    for line in lines:
        if line.startswith('## Cours 1 & 2'):
            new_lines.append('## Cours 1 : Fondamentaux C++\n')
            in_cours_1_2 = True
        elif in_cours_1_2 and line.startswith('### ⭐⭐⭐ Niveau 3'):
            new_lines.append('## Cours 2 : File I/O, Strings, Structs\n\n')
            new_lines.append(line)
            in_cours_1_2 = False
        else:
            new_lines.append(line)
            
    with open(file, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)
