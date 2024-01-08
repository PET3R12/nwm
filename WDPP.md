```python


def czestosc(str, d = {}):
    for znak in str:
        if znak in d:
            d[znak] += 1
        else:
            d[znak] = 1
    return d


#b)
print(f'\nb)')
def f1(d):
    wynik = {}
    for k in d:
        if k.isalpha():
            wynik[k] = wynik.get(k, 0) + 1
    return wynik

print(f1("abrakadabra"))

#zad2
print(f'\nzad2')
def f1(d):
    wynik = {}
    for k in d:
        if k.isalpha():
            k = k.lower()
            wynik[k] = wynik.get(k, 0) + 1
    return wynik
print(f1("AbrakAdabra"))

#zad3
print(f'\nzad3')

plik = open('../kok', 'r') #komenda otwiera plik
linie = plik.readlines() #wprowadza wszystkie linie do zmiennej linie
plik.close() # zamyka
print(linie) #printuje linie ktore maja typ listy


def f1(d):
    wynik = {}
    for linia in d:
        for litery in linia:
            if litery.isalpha():
                litery = litery.lower()
                if litery in wynik:
                    wynik[litery] += 1
                else:
                    wynik[litery] = 1

    return wynik
print(f1(linie))

#zad4
print(f'\nzad4')
def f2(e):
    wynik = {}
    for linia in e:
        linia = linia.split()
        print(linia)
        for litera in linia:
            if litera.isalpha():
                if litera in wynik:
                    wynik[litera] += 1
                else:
                    wynik[litera] = 1
    return wynik

print(f2(linie))

haslo = input('Podaj haslo: ')

def weryfikacja_hasla(haslo):
    litery_m = []
    litery_d = []
    cyfry = []
    znaki_specjalne = []
    if len(haslo) < 8:
        return False
    for element in haslo:
        if element .isupper():
            litery_d.append(element)
        elif element .islower():
            litery_m.append(element)
        elif element .isdigit():
            cyfry.append(element)
        else:
            znaki_specjalne.append(element)
    if litery_m == [] or litery_d == [] or cyfry == [] or znaki_specjalne == []:
        return False
    else:
        return True
print(weryfikacja_hasla(haslo))


rok = int(input('Podaj rok: '))
def rok_przestępny():
    if rok %4 == 0:
        return True
    else:
        return False
print(rok_przestępny())

```
