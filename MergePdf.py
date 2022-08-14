from PyPDF2 import PdfFileMerger

#Create and instance of PdfFileMerger() class
merger = PdfFileMerger()

#Create a list with file names
pdf_files = ['pdf_files/my documents.pdf', 'pdf_files/my document 1.pdf']

for pdf_file in pdf_files:
    #Append PDF files
    merger.append(pdf_file)

#Write out the merged PDF
merger.write("merged_2_pages.pdf")
merger.close()

