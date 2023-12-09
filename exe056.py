somaidade=0
maioridade=0
maioridadehomem=0
nomevelho=''
totmulher=0
for p in range (1,5):
    nome=str(input('Nome: ')).strip()
    idade=int(input('Idade: '))
    sexo=str(input('[M/F]: ')).strip().upper()
    somaidade+=idade
    if p == 1 and sexo =='M':
        maioridade=idade
        nomevelho=nome
    if sexo == 'M' and idade > maioridadehomem:
        maioridadehomem=idade
        nomevelho=nome
    if sexo == 'F' and idade < 20:
        totmulher+=1
mediaidade=somaidade/4
print(f'a media de idade é {mediaidade}')
print(f'o homem mais velho tem {maioridadehomem} anos e se chama {nomevelho}')
print(f'a quantidade de mulheres com menos de 20 anos é {totmulher}')