def fatiar_frase(frase):
    substrings = [] 
    i = 0
    while i < len(frase):
        substring = frase[i:i+6] 
        substrings.append(substring.strip())  
        i += 6  
    return substrings

frase = input("Digite uma frase: ")

for substring in fatiar_frase(frase):
    print(substring)
