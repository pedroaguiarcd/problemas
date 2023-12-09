import random
s4=input('nome do pimeiro aluno a apresentar: ')
s3=input('nome do segundo aluno a apresentar: ')
s2=input('nome do terceiro aluno a apresentar: ')
s1=input('nome do quarto aluno a apresentar: ')
alunos=[s1,s2,s3,s4]
random.shuffle(alunos)


print(f'ordem de apresentaçao de 1 a quatro será:\n {alunos}')