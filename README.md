# Monthly Report Template

This project is designed to generate a monthly sustainability report in PDF format.

## Project Structure

```
MONTHLY-REPORT-TEMPLATE
│   .gitignore
│   index.pdf
│   README.md
│   report.html
│   requirements.txt
│   script.py
├───images
│   ├───background.jpg
│   ├───clock.png
│   ├───coin.png
│   ├───co2.png
│   ├───full_logo.png
│   ├───small_logo.png
│   ├───water-leak1.png
│   ├───water-leak2.png
│   ├───water.png
└───venv
    ├───...
```

## Requirements

- Python 3.x
- Virtualenv (optional but recommended)

## Setup

1. Clone the repository:

   ```sh
   git clone https://github.com/rafael-branco/monthly-report-template.git
   cd monthly-report-template
   ```
2. Create a virtual environment (optional but recommended):

   ```sh
   python -m venv venv
   ```
3. Activate the virtual environment:

   - On Windows:
     ```sh
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```sh
     source venv/bin/activate
     ```
4. Install the required packages:

   ```sh
   pip install -r requirements.txt
   ```

## How to Generate the Report

1. Ensure all necessary images are in the `images` directory:

   - `background.jpg`
   - `clock.png`
   - `coin.png`
   - `co2.png`
   - `full_logo.png`
   - `small_logo.png`
   - `water-leak1.png`
   - `water-leak2.png`
   - `water.png`
2. Edit the `script.py` file if you need to change the report data.
3. Run the script to generate the PDF report:

   ```sh
   python script.py
   ```
4. The generated report `index.pdf` will be created in the project root directory.

## Example

To generate the report with default data, simply run:

```sh
python script.py
```

The output will be a PDF file named `index.pdf` containing the sustainability report for the specified month and year.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.