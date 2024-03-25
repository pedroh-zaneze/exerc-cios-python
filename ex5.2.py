frase = input("Digite uma frase:")
palavras = frase.split()
contem_a = filter(lambda p: p.find("a")>=0, palavras)
# outra maneira contem_a = filter(lambda p: "a" in p, palavras)
substituir = [p.replace("a", "o") for p in contem_a]
print(substituir)



