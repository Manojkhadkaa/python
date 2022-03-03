import matplotlib.pyplot as plt
population_age=[0,1,2,3,4,10,20,30,26,40,60,80,90,100,78,73,75,62,68,79,83,89]
bins=[0,20,30,40,50,60,70,80,90,100]
plt.hist(population_age,bins,histtype="bar", rwidth=0.8)

plt.show()
plt.title("Histogram")
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")