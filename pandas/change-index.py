#Changing the index
import pandas as pd
site=pd.DataFrame({'day':["sunday","monday","tuesday","wednesday","thursday","friday","saturday"],
'visitors':[100,200,300,400,500,600,700],'Bounce-rate':[10,20,30,40,50,60,80]})
site.set_index("Bounce-rate",inplace=True)
print(site)