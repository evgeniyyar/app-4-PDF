import pandas
import glob
from fpdf import FPDF
from pathlib import Path

filepaths = glob.glob("invoices/*.xlsx")

for filepath in filepaths:
    df = pandas.read_excel(filepath,sheet_name="Sheet 1")
    pdf = FPDF(orientation="P",unit="mm",format="A4")
    pdf.add_page()
    pdf.set_font(family="Times",style="B",size=18)
    filename = Path(filepath).stem.split("-")[0]
    pdf.cell(w=50, h=8, txt=f"Invoice nr.{filename}", align="L", ln=1, border=0)
    print(filename)

    pdf.output(f"{filename}.pdf")

print(filepath)