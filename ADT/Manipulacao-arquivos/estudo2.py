import PyPDF2
#lendo um arquivo pdf
with open('arquivo_criado2.pdf', 'rb') as file:
    reader = PyPDF2.PdfReader(file)
    for page in reader.pages:
        print(page.extract_text())
