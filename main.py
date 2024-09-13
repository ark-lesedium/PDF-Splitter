from PyPDF2 import PdfReader, PdfWriter

# Replace 'your_document.pdf' with your file name
input_pdf = "your_document.pdf"
pdf_reader = PdfReader(input_pdf)

# Splitting the affidavit pages (1 and 2)
affidavit_writer = PdfWriter()
for page_num in range(0, 2):
    affidavit_writer.add_page(pdf_reader.pages[page_num])

with open("affidavit.pdf", "wb") as affidavit_output:
    affidavit_writer.write(affidavit_output)

# Splitting the bank statement pages (3 and 4)
statement_writer = PdfWriter()
for page_num in range(2, 4):
    statement_writer.add_page(pdf_reader.pages[page_num])

with open("bank_statement.pdf", "wb") as statement_output:
    statement_writer.write(statement_output)

print("PDF has been successfully split into 'affidavit.pdf' and 'bank_statement.pdf'!")
