frase = input("Digite uma frase:")
palavras = frase.split()

posicao_cada_palavra = [frase.find(palavra) for palavra in palavras]
print(posicao_cada_palavra)

