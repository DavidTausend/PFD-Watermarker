import PyPDF2

template = PyPDF2.PdfFileReader(open('super.pfd', 'rb'))
watermark = PyPDF2.PdfFileReader(open('wtr.pfd', 'rb'))
output = PyPDF2.PdffileWriter() 

for i in range(template.getNumPages()):
    page = template.getpAGE(i)
    page.mergePage(Watermark.getPage(0))
    output.addpage(page)

    with open('watermarked_output.pdf', 'wb') as file:
        output.write(file)