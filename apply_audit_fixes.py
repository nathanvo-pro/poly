import re

# Fix Analyse Numerique
file_an = 'Analyse_Numerique/Synthese_Analyse_Numerique.md'
with open(file_an, 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_lines_an = ['# Synthèse — Analyse Numérique\n\n']
skip_next = False
for line in lines:
    if skip_next:
        skip_next = False
        continue
        
    lower_line = line.lower()
    if line.startswith('## Résumé du Chapitre'):
        new_lines_an.append('#' + line)
    elif line.startswith('## Chapitre 3 — Factorisation QR et systèmes surdéterminés'):
        # There's a duplicate of this line right below the "Résumé du Chapitre 3" content
        # Actually it's just the real chapter 3 start. Wait, the audit showed:
        # - ## Résumé du Chapitre 3
        # - ## Chapitre 3 — Factorisation QR et systèmes surdéterminés
        # Let's just keep everything as is except demoting Résumé.
        new_lines_an.append(line)
    else:
        new_lines_an.append(line)

with open(file_an, 'w', encoding='utf-8') as f:
    f.writelines(new_lines_an)

# Fix Physique
file_ph = 'Physique/Synthese_Physique.md'
with open(file_ph, 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_lines_ph = []
for line in lines:
    if line.startswith('# Physh1002 - Chapitre 1'):
        new_lines_ph.append('# Synthèse — Physique (PHYSH1002)\n')
    else:
        new_lines_ph.append(line)

with open(file_ph, 'w', encoding='utf-8') as f:
    f.writelines(new_lines_ph)

print("Fixed Structural issues in Analyse_Numerique and Physique")
