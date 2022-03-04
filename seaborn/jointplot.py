import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as ss
b=ss.load_dataset('tips')
graph=ss.jointplot(x="tip",y="total_bill",hue="size",data=b)
plt.show()