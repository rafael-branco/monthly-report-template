import pdfkit

config = pdfkit.configuration(wkhtmltopdf="C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe")
pdfkit.from_file('report.html', 'index.pdf')