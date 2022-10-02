import pandas as pd
import matplotlib

df = pd.read_excel("Population.xlsx")
arquivo_excel = pd.ExcelFile("./Population.xlsx")
df.plot.bar()
print(arquivo_excel.sheet_names)