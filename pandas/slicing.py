#various DataFrame Operations
# 1.Slicing the DataFrame
import pandas as pd
sli={'index':[2001,2002,2003,2004],'interest rate':[2,3,2,2],
                'GDP per Thousand':[50,55,65,55]}
            
value=pd.DataFrame(sli)
# print(value.head(2)) #Displaying only the first two rows
print(value.tail(2)) #Displaying only the last two rows