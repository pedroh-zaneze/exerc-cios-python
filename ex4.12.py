frase = input("Digite uma frase: ")
palavras = frase.split() 

terminam_o = 0
terminam_a = 0

for palavra in palavras:
    if palavra.endswith('o'):
        terminam_o += 1
    if palavra.endswith('a'):
        terminam_a += 1

print(f"A quantidade de palavras que terminam com 'o' é {terminam_o}, e as que terminam com 'a' é {terminam_a}")
