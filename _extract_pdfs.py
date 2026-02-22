import fitz

for fname in ['an_ch2.pdf', 'an_ch3.pdf']:
    doc = fitz.open(f'Analyse_Numerique/{fname}')
    outname = f'_temp_{fname.replace(".pdf", ".txt")}'
    with open(outname, 'w', encoding='utf-8') as f:
        for page in doc:
            f.write(page.get_text())
            f.write('\n--- PAGE BREAK ---\n')
    print(f'{fname}: {len(doc)} pages -> {outname}')
    doc.close()
