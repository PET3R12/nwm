```python


def czestosc(str, d = {}):
    for znak in str:
        if znak in d:
            d[znak] += 1
        else:
            d[znak] = 1
    return d

#weryfikacja hasła

def is_alpha_wdp(arg):
    return 'A' <= arg <= 'Z'


def is_num(arg):
    return '0' <= arg <= '9'


def quantity(arg):
    result = {}
    for i in arg:
        if i in result:
            result[i] += 1
        else:
            result[i] = 1
    return result


def password():
    p = input("Password: \n")
    tab = quantity(p)
    for i in tab:
        print(i)



def trojkat(wysokosc):
    dlugosc = int(input('Podaj dlugosc: '))
    wysokosc = int(input('Podaj wysokość: '))
    print(wysokosc * '*')


def rok_przestepny():
    obecny_rok = int(input('Podaj obecny rok: '))
    if obecny_rok %4 == 0:
        return 'To jest rok przestępny'
    else:
        return 'To nie jest rok przestępny'
print(rok_przestepny())

```
