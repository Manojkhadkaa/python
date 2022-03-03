import pandas as pd
df1=pd.DataFrame({'index':[2001,2002,2003,2004],'interest rate':[2,3,2,2],
                'GDP per Thousand':[50,55,65,55]})

df2=pd.DataFrame({'index':[2001,2003,2004,2005],'HPI':[80,85,88,85],'unemployment':[5,7,9,2]})

joining=df1.join(df2)
print(joining)