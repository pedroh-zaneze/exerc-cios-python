palavras = []

while True:
    palavra = input("Digite uma nova palavra (ENTER para concluir:)")
    if palavra == "":
        break
    palavra_comprimento = len(palavra)
    palavras.append(palavra_comprimento)

print("O comprimento de cada palavra digitada é:", palavras)