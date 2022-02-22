#Importing calculator functions
#import calculator
a=20
b=10
#result= calculator.add(a,b)
#print(result)

#The from import statement
from calculator import add, subtract
result=add(a,b)
print(result)
r1=subtract(a,b)
print(r1)

#from imporrt *
from calculator import *
print(add(a,b))