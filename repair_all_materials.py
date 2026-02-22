import glob
import re
import os

def repair_content(content):
    # 1. Fix nested dollars produced by inconsistent formatting
    # Case: $$ $x = ... $$
    content = re.sub(r'\$\$\s*\$([^\$]+?)\$\s*\$\$', r'$$\1$$', content, flags=re.DOTALL)
    # Case: $$ $x = ... (end of line)
    content = re.sub(r'\$\$\s*\$([^\$\n]+)', r'$$\n\1', content)
    
    # 2. Fix common backslash corruption (backslash interpreted as escape)
    # \f (form feed) was corrupted to \x0c
    content = content.replace('\x0c', '\\f')
    # \t (tab) was corrupted to \x09
    content = content.replace('\x09', '\\t')
    
    # 3. Fix \neq corruption where \n was interpreted as newline
    # Looking for a newline followed immediately by 'eq' or 'ne'
    content = re.sub(r'\n(eq|ne|neq)\b', r'\n\\neq', content)
    
    # Custom fixes for literal broken strings found in the audit
    content = content.replace('rac', '\\frac') # literal corrupted \frac
    content = content.replace('	imes', '\\times') # literal corrupted \times
    
    # Fix broken matrix/norm lines
    content = re.sub(r'max_{v\s+eq 0}', r'max_{v \\neq 0}', content)
    
    return content

processed = 0
repaired_files = []

for file in glob.glob('*/*.md'):
    try:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        repaired = repair_content(content)
        
        if repaired != content:
            with open(file, 'w', encoding='utf-8') as f:
                f.write(repaired)
            repaired_files.append(file)
        processed += 1
    except Exception as e:
        print(f"Error processing {file}: {e}")

print(f"Processed {processed} files. Repaired {len(repaired_files)} files: {repaired_files}")
