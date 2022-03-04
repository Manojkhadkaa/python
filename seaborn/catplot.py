import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as ss
b=ss.load_dataset('tips')
graph=ss.catplot(x="day",y="total_bill",data=b)
plt.show()