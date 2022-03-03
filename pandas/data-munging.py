import pandas as pd
data=pd.read_csv('C:\Users\khadk\OneDrive\Desktop\Sample-Spreadsheet-10-rows.csv',index_col=0)
data.to_html('mun.html')
