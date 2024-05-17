"""
Escribe una función contar_palabras que reciba una cadena 
y devuelva el número de palabras que contiene.

hola como estas
3
"""


def contar_palabras(palabras):
    return len(palabras.split(" "))


# hola como estas?
palabras = input("Ingrese algunas palabras: ")
print(contar_palabras(palabras))
