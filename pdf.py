import tabula
from PyPDF2 import PdfReader


with open ("arquivo1.pdf", "rb") as pdf_file:
    pdf_reader = PdfReader(pdf_file)

    num_pages = len(pdf_reader.pages)

    for page_num in range (num_pages):
        page = pdf_reader.pages[num_pages]
        text = page.extract_text()
        print(text)



file = open("arquivo1.pdf", "rb")
pdf = pyPDF2.PdfFileReader(file)

pages = pdf.getNumPages()
page = pdf.getPage(0)
conteudo = page.extractText()
print(conteudo)
