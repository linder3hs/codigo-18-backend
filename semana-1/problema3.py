"""
Escribe un programa que calcule el área de un círculo dado su radio 

(Área = π * radio^2). 

Pide el radio al usuario.
"""
import math

try:
    radio = float(input("Ingrese el radio: "))
    area = math.pi * radio ** 2

    print(f"El area del circulo es: {area}")
except Exception as e:
    print(f"Error: {e}")
