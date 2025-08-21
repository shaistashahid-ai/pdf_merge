from PyPDF2 import PdfMerger

# List of PDF files you want to merge
pdf_files = ["file1.pdf", "file2.pdf", "file3.pdf"]

# Create a PDF merger object
merger = PdfMerger()

# Append all PDFs
for pdf in pdf_files:
    merger.append(pdf)

# Write the merged PDF to a new file
merger.write("merged_output.pdf")
merger.close()

print("PDFs merged successfully into merged_output.pdf")
