"""
Escriban una funcion la cual reciba un numero entero
y retorne la suma de sus valores

Ejemplo:

2536 => 2 + 5 + 3 + 6 = 16
"""


def sum_digits(numero):
    suma = 0
    for n in numero:
        suma += int(n)

    return suma


numero = input("Escriba un numero: ")
print(sum_digits(numero))
