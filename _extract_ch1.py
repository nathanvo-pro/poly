import fitz

fname = 'an_ch1.pdf'
doc = fitz.open(f'Analyse_Numerique/{fname}')
outname = f'_temp_{fname.replace(".pdf", ".txt")}'

with open(outname, 'w', encoding='utf-8') as f:
    for page in doc:
        f.write(page.get_text())
        f.write('\n--- PAGE BREAK ---\n')
        
print(f'Extracted {fname}: {len(doc)} pages -> {outname}')
doc.close()
