import sympy as sp
import numpy as np


liczba = False
symbole = []
wartosci_zmiennych = []
pochodna = []
wartosc_symboli = []
niepewnosci = []
stale = []
niepewnosc_sqr = 0


while liczba == False:
    try:
        liczba_zmiennych = int(input('liczba zmiennych: '))
    except ValueError:
        print('podaj liczbe')
    else:
        liczba = True

wzor = sp.sympify(input('wzor: '))

for i in range(liczba_zmiennych):
    symbole.append(input('zmienna: '))
    wartosci_zmiennych.append(input('jej wartosc: '))
    niepewnosci.append(sp.sympify(input('jej niepewnosc: ')))


for symbol_iter in range(liczba_zmiennych):
    pochodna.append(wzor.diff(symbole[symbol_iter]))
    wartosc_symboli.append((symbole[symbol_iter],wartosci_zmiennych[symbol_iter]))

for pochodna_czastkowa in range(len(pochodna)):
    niepewnosc_sqr =niepewnosc_sqr + pochodna[pochodna_czastkowa].subs(wartosc_symboli) * niepewnosci[pochodna_czastkowa]

sp.pprint(sp.sqrt(niepewnosc_sqr))