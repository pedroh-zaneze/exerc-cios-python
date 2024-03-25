while True:
    frase = input("Digite uma frase com 5 palavras: ")
    palavras = frase.split()
    if len(palavras) != 5:
        print("Você digitou uma frase com uma quantidade de palavras diferente de 5!")
    else:
        break

print("\nPalavras na frase:")
for palavra in palavras:
    print(palavra)

