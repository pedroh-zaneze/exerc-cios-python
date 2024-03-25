peso = float(input("Digite o seu peso em Kg:"))
altura = float(input("Digite a sua altura em m:"))

imc = peso / (altura * altura)
print(f"O seu indíce de massa corporal IMC é de {imc:.2f}")
