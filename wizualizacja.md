```python
#CW1
print('CW1:')
class Car:
    def __init__(self, marka, rok):
        self.marka = marka
        self.rok = rok
car1 = Car('Audi', 1893)
car2 = Car('BMW', 1949)
print(car1.rok)
print(car2.marka)
car1 = car2
print(car1.marka)

#CW2
print('\nCW2:')

class Fruit:
    def __init__(self, color, weight):
        self.color = color
        self.weight = weight

    def __str__(self):
        return 'color ' + self.color + ' waga ' + str(self.weight)

    def isFresh(self):
        if self.color in ['czarny', 'brazowy', 'niebieskie']:
            return False
        else:
            return True

    def greater(self, other):
        return self.weight > other.weight

class Apple(Fruit):
    def __init__(self, weight, color='red', shape='okragly'):
        Fruit.__init__(self, color, weight)
        self.shape = shape

    def isApple(self):
        if self.shape not in ['okragly']:
            return False
        else:
            return True

class Banana(Fruit):
    pass
class Orange(Fruit):
    pass

jbk = Apple(20, 'brazowy', 'okragly')
bnn = Banana('zolty', 20)
print(Apple.isApple(jbk))
print(bnn)

#CW2
print('\nCW2')

class Account:
    def __init__(self, saldo_poczotkowe):
        self.saldo_poczotkowe = saldo_poczotkowe
    m = 0
    def __str__(self):
        return "Stan konta: " + str(self.saldo_poczotkowe) + 'zl'

    def przelew_mk(konto1, konto2, kwota):
        konto1.saldo_poczotkowe += -kwota
        konto2.saldo_poczotkowe += kwota

    def przelew_zewnetrzny(self, kwota):
        self.saldo_poczotkowe += kwota

    def wplata(self, kwota):
        self.saldo_poczotkowe += kwota

    def wyplata(self, kwota):
        self.saldo_poczotkowe += -kwota

konto1 = Account(30)
konto2 = Account(30)
print(konto1)
print(konto2)
Account.przelew_mk(konto1, konto2, 6)
Account.przelew_zewnetrzny(konto1, 5)
Account.wplata(konto1, 30)
Account.wyplata(konto2, 18)
print(konto1)
print(konto2)

class FirmAccount(Account):
    def wynagrodzenie(self, pracownik, ZUS,  kwota):
        kwota_ZUS = kwota/9.76
        ZUS.saldo_poczotkowe += kwota_ZUS
        pracownik.saldo_poczotkowe += (kwota - kwota_ZUS)

BUDIMEX = FirmAccount(40)
FirmAccount.wynagrodzenie(BUDIMEX, konto1, 50)

```
