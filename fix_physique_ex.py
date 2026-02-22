import re

with open('Physique/Exercices_Physique.md', 'r', encoding='utf-8') as f:
    lines = f.readlines()

header_block = []
difficulties = []
current_diff = None
current_ex = []

for line in lines:
    if line.startswith('## '):
        if 'Niveau' in line:
            if current_ex:
                difficulties[-1]['exercises'].append(current_ex)
                current_ex = []
            current_diff = {'title': line.strip(), 'exercises': []}
            difficulties.append(current_diff)
        else:
            header_block.append(line)
    elif line.startswith('### '):
        if current_ex:
            if current_diff:
                current_diff['exercises'].append(current_ex)
            else:
                header_block.extend(current_ex)
        current_ex = [line]
    else:
        if current_ex:
            current_ex.append(line)
        else:
            header_block.append(line)
if current_ex and current_diff:
    current_diff['exercises'].append(current_ex)

chapters = {}
for diff in difficulties:
    diff_title = diff['title']
    for ex in diff['exercises']:
        ex_title = ex[0]
        m = re.search(r'\[Ch\.\s*(\d+)\]', ex_title)
        if m:
            ch_num = int(m.group(1))
            if ch_num not in chapters:
                chapters[ch_num] = {}
            if diff_title not in chapters[ch_num]:
                chapters[ch_num][diff_title] = []
            chapters[ch_num][diff_title].append(ex)
        else:
            if 0 not in chapters:
                chapters[0] = {}
            if diff_title not in chapters[0]:
                chapters[0][diff_title] = []
            chapters[0][diff_title].append(ex)

new_lines = []
new_lines.extend(header_block)

for ch_num in sorted(chapters.keys()):
    if ch_num == 0:
        new_lines.append(f'## Exercices Globaux\n\n')
    else:
        new_lines.append(f'## Chapitre {ch_num}\n\n')
    
    for diff_title, ex_list in chapters[ch_num].items():
        new_lines.append('#' + diff_title + '\n\n')
        for ex in ex_list:
            ex[0] = '#' + ex[0]
            new_lines.extend(ex)
            new_lines.append('\n')

with open('Physique/Exercices_Physique.md', 'w', encoding='utf-8') as f:
    f.writelines([l.replace('\n\n\n', '\n\n') for l in new_lines])
    
print("Reorganized Physique Exercises")
