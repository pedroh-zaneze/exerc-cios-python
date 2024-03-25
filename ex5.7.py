alunos = dict()
while True:
    nome_aluno = input("Digite o nome do aluno (ENTER para concluir):")
    if nome_aluno:
        nota_aluno = float(input("Digite a nota do aluno:"))
        alunos = round(nota_aluno)
    else:
        break
    print(f"A nota do aluno é {alunos}")
