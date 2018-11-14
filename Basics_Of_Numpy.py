# Numpy supports all data types likes bool, integer, float, complex etc.
# They are defined by the numpy.dtype class 


"""
There are a couple of mechanisms for creating arrays in NumPy:
 a. Conversion from other Python structures (e.g., lists, tuples).
 b. Built-in NumPy array creation (e.g., arange, ones, zeros, etc.).
 c. Reading arrays from disk, either from standard or custom formats 
     (e.g. reading in from a CSV file).
"""


import numpy as np

# Converting an python list to ndarray
a = np.array([1,2,3,4,5,6])


# Converting an python tuple to ndarray

# arange() -- creates arrays with regularly incrementing values.
b = np.arange(2,40,3)

#Reshaping it another shape
c = a.reshape(2,3)

c.shape
c.dtype

np.float64(22)


"""
Arrays Operations - Basic operations apply element-wise. 
The result is a new array with the resultant elements.
Operations like *= and += will modify the existing array.
"""

a = np.arange(5) 
b = np.arange(5) 


print a+b 

print a-b 

print a**2 

print a>3 

print np.sin(a) 

print a*b 


# zeros(shape) -- creates an array filled with 0 values with the specified 
#Shape. The default dtype is float64.

np.int64(2.3)

np.zeros((2,3))


# ones(shape) -- creates an array filled with 1 values
np.ones((3,3))


"""
Mean, Median, Mode, and introducing NumPy

Mean vs. Median

Let's create some fake income data, centered around 27,000 
with a normal distribution and standard deviation of 15,000, with 10,000 data points. 
Then, compute the mean (average)
    
"""

incomes = np.random.normal(27000, 15000, 10000)

#Computing Value
np.mean(incomes)

#Computing Median
np.median(incomes)

#Computing Value
np.std(incomes)



# linspace() -- creates arrays with a specified number of elements, 
#and spaced equally between the specified beginning and end values.
np.linspace(0,10,50)

ran = np.random.randint(1,10,30)


#Normal Distribution 
d = np.random.normal(50,25,300)

inc = np.random.normal(27000,15000,1000)
