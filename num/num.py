from cmath import sqrt
import numpy as np
a=np.array([(1,2,3,4),(10,2,4,6)])
b=np.array([1,2,3])
# print(a)
# # checking the type 
# print(type(a)) 
# print(type(b))
# #Checking the dimensions
# print(a.ndim)
# print(b.ndim)
# #Checking the byte size of each of the element
# print(a.itemsize)
# #checking the datatype of an element
# print(a.dtype)
# #Checking the size of an array
# print(a.size)
# #Columns and rows
# print(a.shape)

# #Reshaping the size 
# print(a.reshape(4,2))

#Slicing  first row as 0 second rows as 1
# print(a[0,3])
# print(a[0:,3])

# print(a.max())
# print(a.min())
# print(a.sum())

# print(a.sum(axis=0)) #Sum of all the column element
# print(a.sum(axis=1)) #Sum of all the rows element
# print(np.sqrt(a)) #Square root of each of the element
print(np.std(a))