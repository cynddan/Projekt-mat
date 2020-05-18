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
wzor = QLineEdit(widget)
wzor.setReadOnly(True)
wynik = QLineEdit(widget)
wynik.setReadOnly(True)

def obliczenie():
    return

przycisk_oblicz = QPushButton('Oblicz')

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
layout.addWidget(wzor,7,0,1,5)
layout.addWidget(wynik,9,0,1,4)
layout.addWidget(QLabel('Zmienne'),0,0)
layout.addWidget(QLabel('Wartość zmiennej'),2,0)
layout.addWidget(QLabel('Niepewność zmiennej'),4,0)
layout.addWidget(QLabel('Wynik bez wartości'),6,0)
layout.addWidget(QLabel('Wartość'),8,0)
layout.addWidget(przycisk_oblicz, 9,4)


widget.setLayout(layout)
widget.show()
app.exec_()
