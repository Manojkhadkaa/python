from operator import imod
from matplotlib import pyplot as plt
from matplotlib import style
x=[5,8,10]
y=[10,16,6]
style.use("ggplot")
x2=[6,9,11]
y2=[6,15,7]
plt.plot(x,y,'g',label='line one', linewidth=5) #g-green color
plt.plot(x2,y2,'c',label='line two' ,linewidth=5 )
plt.title("Info")
plt.xlabel("X-Axis")
plt.ylabel("Y-axis")
plt.legend()
plt.grid(True,color='k') #Grid line
plt.show()