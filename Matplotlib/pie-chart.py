import matplotlib.pyplot as plt

slices=(7,2,2,13)
activities=('sleeping','eating','working','coding')
cols=('m','c','b','r')
plt.pie(slices, 
    labels=activities,
    colors=cols,
    startangle=90,
    
    autopct='%1.1f%%',
    shadow=True,
    )
plt.title("Pie Chart")
plt.show()
