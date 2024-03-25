distancia_percorrida = float(input("Digite a distância percorrida pelo objeto em (m):"))
tempo_gasto = float(input("Digite o tempo gasto pelo objeto em (s):"))
aceleracao = float(input("Digite a aceleração em (m/s²):"))

velocidade_final = (0 + 2*aceleracao*distancia_percorrida) **0.5
velocidade_inicial = velocidade_final - (aceleracao * tempo_gasto)
print(f"A velocidade inicial do objeto é {velocidade_inicial} m/s², e a sua velocidade final é de {velocidade_final} m/s²")
