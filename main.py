from PyPDF2 import PdfFileReader, PdfFileWriter

file_pdf = PdfFileReader('JavaScript.pdf')
out_pdf = PdfFileWriter()

for i in range(file_pdf.numPages):
    page_details = file_pdf.getPage(i)
    out_pdf.addPage(page_details)

password = "12345678"
out_pdf.encrypt(password)

with open("JavaScript.pdf","wb") as filename:
    out_pdf.write(filename)