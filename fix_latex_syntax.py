import re
import glob

# We need to fix inline math $ ... $ that contains \tag{} or \begin{align} ... \end{align}
# because KaTeX only supports them in display math $$ ... $$

for file in glob.glob('*/*.md'):
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
        
    original = content
        
    # Fix $ \begin{align} ... \end{align} $ -> $$ \begin{align} ... \end{align} $$
    content = re.sub(r'(?<!\$)\$\s*\\begin\{align\}(.*?)\\end\{align\}\s*\$(?!\$)', 
                     r'$$\n\\begin{align}\1\\end{align}\n$$', content, flags=re.DOTALL)
                     
    # Fix $ ... \tag{X} $ -> $$ ... \tag{X} $$
    content = re.sub(r'(?<!\$)\$\s*(.*?\\tag\{.*?\}\s*)\$(?!\$)', 
                     r'$$\n\1\n$$', content, flags=re.DOTALL)
                     
    if content != original:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Fixed LaTeX in {file}")

print("Done fixing LaTeX syntax.")
