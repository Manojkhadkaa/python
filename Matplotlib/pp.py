from matplotlib import pyplot as plt
plt.bar([1,3,5,7,9],[5,2,7,8,2],label="Line one", color='g') 
plt.bar([2,4,6,8,10],[8,9,10,11,6],label="Line Two",color='r')
plt.title("Info")
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.legend()
plt.show()
