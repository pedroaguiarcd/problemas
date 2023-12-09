var='M,F'
while var == 'M,F':
    sexo=str(input('digite seu sexo [M/F]:  ')).upper()
    if sexo == 'F':
        print('seu sexo é feminino')
        break
    elif sexo == 'M':
        print('seu sexo é masculino')
        break
    elif sexo != 'M' and 'F':
        print('resposta invalida. tente novamente')
print('FIM')