numeros = []

while True:
    entrada = input("Digite um número (ENTER para concluir): ")
    if entrada == "":
        break
    numero = int(entrada)
    numeros.append(numero)

quadrados = list(map(lambda x: x**2, numeros))

print("Lista com os quadrados de cada número:", quadrados)
