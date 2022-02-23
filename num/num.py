import numpy as np
a=np.array([(1,2,3),(10,2,4)])
b=np.array([1,2,3])
print(a)
# checking the type 
print(type(a)) 
print(type(b))
#Checking the dimensions
print(a.ndim)
print(b.ndim)
#Checking the byte size of each of the element
print(a.itemsize)
#checking the datatype of an element
print(a.dtype)
#Checking the size of an array
print(a.size)
#Columns and rows
print(a.shape)