import numpy as np
import pandas as pd
#seria liczb calkowitych
df = pd.Series([1, 2, 3, 4, 5])
print(df)

#seria ze stringami
dt = pd.Series(['a', 'b', 'c', 'd', 'e'])
print('\n')
print(dt)
#lista na serie
lista = [1, 2, 3, 4, 5]
d = pd.Series(lista)
print('\n')
print(d)
#seria na liste
print('\nTUTAJ\n')
l1 = list(d)

#z tablicy na serie

print('\n')

#z tablicy na serie
tablica = np.array([[1, 1, 2],[2, 1, 0],[4, 1, 2]])
print(tablica)
print('\n')
seria = pd.Series(tablica[1])
print(seria)
print('\n')
#z serii na tablice
tab = np.array(df)
print(tab)
print('\n')

#dodawanie itd.
s1 = pd.Series(list(range(1, 5)))
s2 = pd.Series(list(range(6, 10)))
print(s1)
print('\n')
print(s2)
print('\n')
print(s1 + s2)
print('\n')
print(s2 - s1)
print('\n')
print(s1 * s2)
print('\n')
print(s2/s1)
print('\n')

from random import *
#ostatnia kropka
seria = pd.Series([randrange(-100, 101, 1)/10, randrange(-100, 101, 1)/10, randrange(-100, 101, 1)/10])
print(seria)

s2 = pd.Series([x for x in seria if x < 0])
print(s2)

#b)
my_list = [1, 32, -37, 91, 12, 11, -5]
my_dict = {'a' : [1, 3, 2],
           'b' : [2, 5, 7],
           'c' : [3, 4, 8],
           'd': [4, 10, 12]}

my_array = np.array([[1, 2, 5],[-2, 3, 3], [5, 2, 6]])
my_series = pd.Series ([1, 32, -37, 91, 12, 11, -5],
                       index = ['a','b','c','d','e','f','g'])

ramka_danych = pd.DataFrame(
    {"a" : my_list,
     "b" : my_dict[1]}
)
print(ramka_danych)





