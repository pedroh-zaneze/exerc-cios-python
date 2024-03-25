def par (numero):
    if numero % 2 == 0:
        return True
    else:
        return False
    
numero = float(input("Digite um número:"))
if par(numero):
    print("O número digitado é par!")
else:
    print("O número digitado é ímpar!")