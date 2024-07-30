import pandas
from fpdf import FPDF
import glob
from pathlib import Path

filepaths = glob.glob("animals/*.txt")
pdf = FPDF(orientation="P",unit="mm",format="A4")


for filepath in filepaths:
    filename = Path(filepath).stem.title()
    pdf.add_page()
    pdf.set_font(family="Times",style="B",size=18)
    pdf.cell(w=0,txt=filename,h=12,align="L",ln=1,border=0)

    with open(filepath, "r") as files:
        file = files.read()
        print(file)
        pdf.set_font(family="Times",style="I",size=14)
        pdf.cell(w=0,txt=file,h=0,align="L",ln=0,border=0)

pdf.output("123.pdf")

