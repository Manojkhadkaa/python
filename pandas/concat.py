import pandas as pd
df1=pd.DataFrame({'index':[2001,2002,2003,2004],'HPI':[80,85,88,85],'interest rate':[2,3,2,2],
                'GDP per Thousand':[50,55,65,55]})

df2=pd.DataFrame({'index':[2005,2006,2007,2008],'HPI':[80,85,88,85],'interest rate':[2,3,2,2],
                'GDP per Thousand':[50,55,65,55]})
            
concat=pd.concat([df1,df2])
print(concat)