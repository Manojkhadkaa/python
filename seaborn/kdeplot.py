import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as ss
b=ss.load_dataset('tips')
# graph=ss.displot(x="day",y="total_bill",data=b)
graph=ss.kdeplot(x="total_bill",hue="day",data=b)
plt.show()