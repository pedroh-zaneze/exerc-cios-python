frase = input("Digite uma frase: ")

palavras = frase.split()
palavras_sem_espaco = [palavra.strip() for palavra in palavras if palavra.strip()]

frase_nova = " ".join(palavras_sem_espaco)

print(frase_nova)
