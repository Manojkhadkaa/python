import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as ss
b=ss.load_dataset('tips')
# graph=ss.displot(x="day",y="total_bill",data=b)
graph=ss.scatterplot(x="total_bill",y="day",hue="size",data=b)
plt.show()