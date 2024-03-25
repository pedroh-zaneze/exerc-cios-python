numero = input("Digite um número: ")

eh_numero_real = True
ponto_decimal = False

for caractere in numero:
    if not caractere.isdigit():
        if caractere == '.' and not ponto_decimal:
            ponto_decimal = True
        else:
            eh_numero_real = False
            break

if eh_numero_real:
    print("É um número real!")
else:
    print("Não é um número real!")
