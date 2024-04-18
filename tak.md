```python
import numpy
import numpy as np

my_array = np.arange(10, 40, 2)
print(my_array)
print('\n')

print(my_array.shape)
print('\n')

my_array.resize(3,5)

print(my_array)
print('\n')

print(my_array+3)
print('\n')

print(my_array*2)
print('\n')

my_array[my_array % 6 == 2] = 0
print(my_array)
print('\n')

def change(A, x):
    A1 = np.copy(my_array)
    A1[A1 == 0] = x
    return A1

print(change(my_array, 2))
print('\n')
print(my_array)
print('\n')

#CW2
A = np.array([[1, 1, 2],[2, 1, 0],[4, 1, 2]])
print(A)
B = np.array([[2, 5, 7], [2, 8, 0],[4, 3, 1]])
print(B)
C = numpy.matmul(A, B)
print('\n')
print(C)
print('\n')
print(numpy.linalg.det(A)) #wyznacznik
print('\n')
print(np.flip(A)) #odwracanie
print('\n')
print(np.linalg.matrix_power(A, -3))# potegowanie


```
