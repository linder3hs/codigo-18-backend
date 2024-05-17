# Escriba un programa que retorne la suma de 2 numeros
numero_1 = input("Ingrese el numero 1: ")
numero_2 = input("Ingrese el numero 2: ")

# type(variable) permite ver el tipo de dato
print(type(numero_1), type(numero_2))

"""
 Nos dimos cuenta que toda información
 que venga de input, será un 'str'(string)
"""

"""
Si queremos convertir un str a int usamos la funcion int(variable)
Si queremos convertir un str a float usamos la funcion float(variable)
"""
try:
    suma = float(numero_1) + float(numero_2)
    print(suma)
except Exception as e:
    print(e)
