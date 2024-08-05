import pdfkit
from jinja2 import Environment, FileSystemLoader
import tempfile
import os

def generate_report(month, year, total_units, units_with_leaking, days, avg_water_leaking,
                    water_saved, water_wasted, co2_saved, co2_wasted, money_saved, money_wasted,
                    template_file='report.html', output_pdf='index.pdf'):

    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template(template_file)

    context = {
        'month': month,
        'year': year,
        'total_units': total_units,
        'units_with_leaking': units_with_leaking,
        'days': days,
        'avg_water_leaking': avg_water_leaking,
        'water_saved': water_saved,
        'water_wasted': water_wasted,
        'co2_saved': co2_saved,
        'co2_wasted': co2_wasted,
        'money_saved': money_saved,
        'money_wasted': money_wasted
    }

    html_content = template.render(context)

    with tempfile.NamedTemporaryFile(delete=False, suffix='.html', dir='.') as temp_file:
        temp_file.write(html_content.encode('utf-8'))
        temp_file_path = temp_file.name

    options = {
        'page-size': 'Letter',
        "enable-local-file-access": "",
        'margin-top': '0',
        'margin-right': '0',
        'margin-bottom': '0',
        'margin-left': '0',
    }

    pdfkit.from_file(temp_file_path, output_pdf, options=options)
    print(f'Temporary HTML file created at: {temp_file_path}')
    print(f'PDF generated at: {output_pdf}')

    os.remove(temp_file_path)

def main():
    generate_report(
        month='Janeiro',
        year='2024',
        total_units='15.000',
        units_with_leaking='254',
        days='3,5',
        avg_water_leaking='38,64',
        water_saved='9346,096',
        water_wasted='1992,22',
        co2_saved='4712,12',
        co2_wasted='922,11',
        money_saved='98.543,15',
        money_wasted='21.161,21'
    )

if __name__ == "__main__":
    main()