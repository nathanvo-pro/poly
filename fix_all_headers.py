import glob
import re

for file in glob.glob('*/*.md'):
    if 'CheatSheet' in file or 'Dashboard' in file:
        continue
        
    with open(file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        
    new_lines = []
    
    # 1. Title fixes
    # If the file is a Synthesis, we ensure there is exactly one H1 at the very top.
    
    for i, line in enumerate(lines):
        # Fix H1 chapters that should be H2
        if line.startswith('# Chapitre') or line.startswith('# Cours'):
            new_lines.append('#' + line)
        # Fix H2 that are not chapters
        elif line.startswith('## '):
            lower_line = line.lower()
            if 'chapitre' in lower_line or 'cours' in lower_line:
                # keep it as H2
                # Optionally standardise prefix "## Chapitre X :"
                new_lines.append(line)
            else:
                # Demote non-chapter H2s to H3
                new_lines.append('#' + line)
        else:
            new_lines.append(line)
            
    with open(file, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)
        
print("Fixed headers in all Synthesis and Exercises files.")
