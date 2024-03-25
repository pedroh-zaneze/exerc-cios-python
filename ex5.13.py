lista_pares = [0, 2, 4, 6, 8]
lista_impares = [1, 3, 5, 7, 9]

soma_total = 0
total_elementos = len(lista_pares) + len(lista_impares)

for num in lista_pares + lista_impares:
    soma_total += num

media_total = soma_total / total_elementos

print("Média total dos elementos:", media_total)
