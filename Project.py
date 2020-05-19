import sympy as sp
import numpy as np
from PyQt5.QtWidgets import *


app = QApplication([])
widget = QWidget()

widget.setWindowTitle("Prawo Propagacji Niepewności")
layout = QGridLayout()

zmienna1 = QLineEdit(widget)
zmienna2 = QLineEdit(widget)
zmienna3 = QLineEdit(widget)
wartosc1 = QLineEdit(widget)
wartosc2 = QLineEdit(widget)
wartosc3 = QLineEdit(widget)
niepewnosc1 = QLineEdit(widget)
niepewnosc2 = QLineEdit(widget)
niepewnosc3 = QLineEdit(widget)
wzor_pole = QLineEdit(widget)
wzor_pochodna = QLineEdit(widget)
wzor_pochodna.setReadOnly(True)
wynik = QLineEdit(widget)
wynik.setReadOnly(True)

zmienna1.setText('x')
zmienna2.setText('y')
zmienna3.setText('z')
wartosc1.setText('1')
wartosc2.setText('1')
wartosc3.setText('1')
niepewnosc1.setText('1')
niepewnosc2.setText('1')
niepewnosc3.setText('1')

def obliczenie():
    try:
        symbole = []
        niepewnosc_sqr = 0
        pochodna = []
        wartosc_symboli = []
        niepewnosci = []
        wartosci_zmiennych = []
        pochodne = ''

        wzor = sp.sympify(wzor_pole.text())
        symbole.extend((zmienna1.text(), zmienna2.text(), zmienna3.text()))
        wartosci_zmiennych.extend((wartosc1.text(), wartosc2.text(), wartosc3.text()))
        niepewnosci.extend((sp.sympify(niepewnosc1.text()), sp.sympify(niepewnosc2.text()), sp.sympify(niepewnosc3.text())))
    except:
        wynik.setText('Podaj wzór')

    else:
        for symbol_iter in range(len(symbole)):
            pochodna.append(wzor.diff(symbole[symbol_iter]))
            wartosc_symboli.append((symbole[symbol_iter],wartosci_zmiennych[symbol_iter]))

        for pochodna_czastkowa in range(len(symbole)):
            niepewnosc_sqr = niepewnosc_sqr + (pochodna[pochodna_czastkowa].subs(wartosc_symboli) * niepewnosci[pochodna_czastkowa])**2
            if pochodna[pochodna_czastkowa] !=0:
                if pochodne != "":
                    pochodne += ' + ' + str(pochodna[pochodna_czastkowa])
                else:
                    pochodne = str(pochodna[pochodna_czastkowa])
        
        wzor_pochodna.setText(pochodne)
        wynik.setText(str(sp.sqrt(niepewnosc_sqr)))



przycisk_oblicz = QPushButton('Oblicz')
przycisk_oblicz.clicked.connect(obliczenie)

widget.resize(400,200)

layout.addWidget(zmienna1,1,0)
layout.addWidget(zmienna2,1,2)
layout.addWidget(zmienna3,1,4)
layout.addWidget(wartosc1,3,0)
layout.addWidget(wartosc2,3,2)
layout.addWidget(wartosc3,3,4)
layout.addWidget(niepewnosc1,5,0)
layout.addWidget(niepewnosc2,5,2)
layout.addWidget(niepewnosc3,5,4)
layout.addWidget(wzor_pole,7,0,1,5)
layout.addWidget(wzor_pochodna,9,0,1,5)
layout.addWidget(wynik,11,0,1,4)
layout.addWidget(QLabel('Zmienne'),0,0)
layout.addWidget(QLabel('Wartość zmiennej'),2,0)
layout.addWidget(QLabel('Niepewność zmiennej'),4,0)
layout.addWidget(QLabel('Wzór'),6,0)
layout.addWidget(QLabel('Pochodne cząstkowe'),8,0)
layout.addWidget(QLabel('Wartość'),10,0)
layout.addWidget(przycisk_oblicz, 11,4)


widget.setLayout(layout)
widget.show()
app.exec_()