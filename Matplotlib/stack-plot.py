import matplotlib.pyplot as plt
days=[1,2,3,4,5]

sleeping=[8,5,2,8,11]
eating=[5,6,4,3,8]
playing=[1,3,5,7,9]
working=[2,4,3,6,8]
plt.plot([],[],color='m', label='sleeping',linewidth='5')
plt.plot([],[],color='c', label='eating',linewidth='5')
plt.plot([],[],color='r', label='playing',linewidth='5')
plt.plot([],[],color='k', label='working',linewidth='5')
plt.stackplot(days,sleeping,eating,playing,working,colors=['m','c','r','k'])
plt.title("Stack plot")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.legend()
plt.show()