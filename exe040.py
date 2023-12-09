nota=float(input('Digite a primeira nota do aluno: '))
nota2=float(input('Digite a primeira nota do aluno: '))
notatotal=nota+nota2
media=notatotal/2
recu=range(5.0,6.9)
if media < 5.0:
    print('aluno reprovado!')
elif 7.0 > media >= 5.0 :
    print('de recuperaçao! ')
elif media > 7:
    print('aluno aprovado!')
