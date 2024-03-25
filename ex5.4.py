lista = list(range(31))
divisiveis = list(filter(lambda x: x%3==0 or x%5==0, lista))
print(divisiveis)
