import math

def calcular_fatorial(numero: int):
    return math.factorial(numero)

numero = int(input("Digite um número inteiro:"))
print(calcular_fatorial(numero))