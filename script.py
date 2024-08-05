import pdfkit

pdfkit.from_file('report.html', 'index.pdf', options={"enable-local-file-access": ""})