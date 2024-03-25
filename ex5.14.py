nome_aluno = ["Pedro", "Henrique", "Zaneze", "Coelho"]
nota_aluno = [10, 8, 9, 7]

lista_tuplas = list(zip(nome_aluno, nota_aluno))

lista_tuplas.sort(key=lambda x: x[1], reverse=True)

nomes_ordenados = [tupla[0] for tupla in lista_tuplas]
notas_ordenadas = [tupla[1] for tupla in lista_tuplas]

print("Lista de alunos em ordem decrescente de nota:")
for nome, nota in lista_tuplas:
    print(f"{nome}: {nota}")
    
