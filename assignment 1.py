from pathlib import Path  # Python Standard Library

import pandas as pd  # pip install pandas
import xlwings as xw  # pip install xlwings


this_dir = Path(__file__).parent if '__file__' in locals() else Path.cwd()
wb_file_path = this_dir / 'assignment 1.xlsx'

wb = xw.Book(wb_file_path)
sht = wb.sheets['Sheet1']
rng = sht.range('A1:E77')

df = rng.options(pd.DataFrame, index=False, header=True).value
print(df)
