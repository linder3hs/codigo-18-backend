"""
Escribe una función max_de_tres que reciba tres números
y devuelva el mayor de ellos.
"""


def max_de_tres(n1, n2, n3):
    return max(n1, n2, n3)


n1 = int(input("Ingrese el numero 1: "))
n2 = int(input("Ingrese el numero 2: "))
n3 = int(input("Ingrese el numero 3: "))

print(max_de_tres(n1, n2, n3))

numeros = input("Ingrese los numeros separados por ,: ")
"""
split: convierte un str a un list, basado en un operador

Ejemplo: 
"10-11-12".split("-")
["10", "11", "12"]

destructuracion
n1, n2, n3 = ["10", "11", "12"]
"""
print(numeros.split(","))
n1, n2, n3 = numeros.split(",")

print(max_de_tres(int(n1), int(n2), int(n3)))
