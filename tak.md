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
print('\n')

#CW3
panstwa = np.array(['China', 'Japan', 'Germany', 'USA', 'South Korea', 'India', 'Brazil', 'Mexico', 'Spain', 'Russia'])
rok1999 = np.array([0.56, 8.1, 5.3, 5.63, 2.36, 0.53, 1.1, 0.99, 2.28, 0.94])
rok2014 = np.array([19.91, 8.27, 5.6, 4.25, 4.12, 3.15, 2.31, 1.91, 1.89, 1.69])

procenty = ((rok2014/rok1999)*100)
przyrost = procenty - 100
print(np.round(przyrost, 2)) #dziwny output
print(panstwa[min(rok1999) == rok1999])
print(panstwa[rok2014<rok1999])

#CW4
imiona = np.array(['anna', 'zofia', 'sylwia', 'katarzyna', 'teresa', 'tomasz', 'cezary', 'zenon', 'filip', 'adrian'])
wiek = np.array([21, 40, 13, 31, 34, 14, 13, 28, 20, 15])
plec = np.array('k', 'k', 'k', 'k', 'k', 'm', 'm', 'm', 'm', 'm')
waga = np.array([65, 80, 64, 69, 74, 61, 66, 61, 69, 77])
wzrost = np.array([179, 179, 151, 177, 170, 157, 151, 153, 160, 160])
okulary = np.array('nie', 'tak', 'nie', 'tak', 'nie', 'tak', 'nie', 'tak', 'nie', 'tak', 'nie')
print(len(okulary))

```
