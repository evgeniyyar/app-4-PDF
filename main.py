import pandas
import glob

filepaths = glob.glob("invoices/*.xlsx")

for filepath in filepaths:
    df = pandas.read_excel(filepath, sheet_name="Sheet 1")
    print(df)





