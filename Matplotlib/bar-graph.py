from matplotlib import pyplot as plt
plt.bar([1,3,5,7,9],[5,2,7,8,2],label="Line one") 
plt.bar([2,4,6,8,10],[8,6,2,5,6], label="line two" ,color='g')
plt.title("Info")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend()
plt.show()