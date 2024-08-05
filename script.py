import pdfkit

options = {
    'page-size': 'Letter',
    "enable-local-file-access": "",
    'margin-top': '0',
    'margin-right': '0',
    'margin-bottom': '0',
    'margin-left': '0',
}

pdfkit.from_file('report.html', 'index.pdf', options=options)