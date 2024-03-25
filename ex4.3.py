import math

angulo = float(input("Digite o valor do ângulo em graus:"))
angulo_radianos = math.radians(angulo)

seno = math.asin(angulo_radianos)
cosseno = math.acos(angulo_radianos)
tangente = math.atan(angulo_radianos)

print(f"O valor do seno é {seno}")
print(f"O valor do cosseno é {cosseno}")
print(f"O valor do tangente é {tangente}")