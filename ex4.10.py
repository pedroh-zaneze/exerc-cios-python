frase = input("Digite uma frase: ")
artigos = ["o", "a", "os", "as", "um", "uns", "uma", "umas"]
    
palavras = frase.split()
palavras_sem_artigos = [palavra for palavra in palavras if palavra.lower() not in artigos]
nova_frase = ' '.join(palavras_sem_artigos)
frase_sem_artigos = nova_frase 
print("Frase sem os artigos:", frase_sem_artigos)

