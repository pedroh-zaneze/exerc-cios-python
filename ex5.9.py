nomes = []

while True:
    nome = input("Digite um nome (ENTER para concluir):")
    if nome == "":
        break
    nome_maiusculo = nome.upper()
    nomes.append(nome_maiusculo)

print(f"Lista de nomes em caixa alta: {nomes}")

