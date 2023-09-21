# -*- coding: utf-8 -*-

###   NUMPY 

import numpy as np 

array1 = np.array([[1,2,3],[5,6,8]])

print('\n')

print(array1)
print('\n')

print(type(array1))

array2 = np.array([[1,2,3,4,5], [6,7,8,9,0]])

array3 = np.array([[6,7,2,9,1], [9,1,3,4,5]])

array3.shape
print('\n')

print(array3.shape)
print('\n')

print(array3)
print('\n')

array4 = array2 + array3

print('\n')

print(array4)

print('\n')

a5 = np.zeros(10)
a6 = np.ones(10)
a7 = np.ones(10, dtype=int)
print('\n')

print(a5)
print('\n')

print(a6)
print('\n')
print(a7)

val1 = a7.sum()
print('\n')

print(val1)
