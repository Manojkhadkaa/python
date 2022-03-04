import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as ss
# a=ss.get_dataset_names() #Already defined dataset in seaborn
# print(a)
tips=ss.load_dataset('tips')
# print(tips.head(5))
a=ss.relplot(x="time",y="tip", data=tips ,kind="line")
# graph = ss.FacetGrid(tips, col ="sex",  hue ="day")
# graph.map(plt.scatter, "total_bill", "tip", edgecolor ="w").add_legend()
plt.show()