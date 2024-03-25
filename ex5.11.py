numeros = []

while True:
    numero = input("Digite um número (ENTER para concluir): ")
    if numero == "":
        break
    numero = int(numero)
    if numero % 2 == 0:  
        numeros.append(numero)

print("Lista de números pares:", numeros)
