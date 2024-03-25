letra = input("Digite uma letra:")

vogais = "aeiouAEIOU"
consoantes = "bcdfghjklmnpqrstvwxyzç"

if letra in vogais:
    print("É uma vogal!")
elif letra in consoantes:
    print("É uma consoante!")
else:
    print("Você não digitou uma letra!")
