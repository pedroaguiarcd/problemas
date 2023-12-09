import random
alunos=input('digite os nomes dos alunos: ').split()
# a1=input('digite o nome do aluno: ')
# a2=input('digite o nome do aluno: ')
# a3=input('digite o nome do aluno: ')
# a4=input('digite o nome do aluno: ')
# lista=[alunos]
sorteio=random.choice(alunos)
print(f'o aluno(a) escolhido para apagar o quadro foi: {sorteio}')

