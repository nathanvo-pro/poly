import glob
import re
import os

courses = ['Informatique_OOP', 'Physique', 'Analyse_Numerique']

print("=========================================")
print("          AUDIT DES COURS")
print("=========================================")

for course in courses:
    print(f"\n\n>>> COURS : {course}")
    files = glob.glob(f"{course}/*")
    
    synthese = f"{course}/Synthese_{course}.md"
    exercices = f"{course}/Exercices_{course}.md"
    flashcards = f"{course}/Flashcards_{course}.csv"
    
    # 1. Synthese Audit
    print("\n--- SYNTHESE ---")
    if synthese.replace('/', '\\') in [f.replace('/', '\\') for f in files]:
        with open(synthese, 'r', encoding='utf-8') as f:
            content = f.read()
            lines = content.split('\n')
            
            # Check Headers
            h1s = [l for l in lines if l.startswith('# ')]
            h2s = [l for l in lines if l.startswith('## ')]
            
            print(f"H1 count: {len(h1s)} (devrait être 1)")
            if len(h1s) != 1: print("  -> " + str(h1s))
            
            print(f"Chapitres (H2): {len(h2s)}")
            for h in h2s: print("  - " + h)
            
            # Check for LaTeX blocks without closing
            math_display = len(re.findall(r'\$\$', content))
            if math_display % 2 != 0:
                print(f"⚠️ ATTENTION : Nombre impair de balises $$ ({math_display}) -> problème de LaTeX")
                
            # Check for generic unclosed tags
            if '<details>' in content and content.count('<details>') != content.count('</details>'):
                print("⚠️ ATTENTION : Balises <details> non fermées")
            
            # Check equation tags
            if '\\begin{align}' in content and content.count('\\begin{align}') != content.count('\\end{align}'):
                print("⚠️ ATTENTION : Balises align non fermées")
                
            # Check numbering
            print("Vérification numérotation (H3):")
            h3s = [l for l in lines if l.startswith('### ')]
            print(f"  {len(h3s)} sous-titres H3 trouvés.")
            
    else:
        print("MANQUANTE !")

    # 2. Exercices Audit
    print("\n--- EXERCICES ---")
    if exercices.replace('/', '\\') in [f.replace('/', '\\') for f in files]:
        with open(exercices, 'r', encoding='utf-8') as f:
            content = f.read()
            lines = content.split('\n')
            
            h2s = [l for l in lines if l.startswith('## ')]
            print(f"Chapitres (H2): {len(h2s)}")
            for h in h2s: print("  - " + h)
            
            # Check missing answers
            ex_count = len([l for l in lines if 'Niveau' in l or '**Exercice' in l or '### Exercice' in l])
            details_count = content.count('<details>')
            print(f"Nombre de balises <details> (réponses masquées): {details_count}")
            
            # Check for LaTeX blocks without closing
            math_display = len(re.findall(r'\$\$', content))
            if math_display % 2 != 0:
                print(f"⚠️ ATTENTION : Nombre impair de balises $$ ({math_display}) -> problème de LaTeX")
    else:
        print("MANQUANTS !")
        
print("\n=========================================")
