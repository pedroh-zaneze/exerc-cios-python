frase = input("Digite uma frase:")

palavras = frase.split()
quantidade_vezes_palavra = [frase.count(palavra) for palavra in palavras]
print(quantidade_vezes_palavra)
