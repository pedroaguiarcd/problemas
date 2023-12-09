cont=0
soma=0
while True:
    num=int(input('digite um numero [999 para parar]: '))
    if num == 999:
        print('finalizando programa...')
        break
    cont+=1
    soma+=num
print('programa finalizado')
print(f'A soma dos numeros: {soma} e a quantidade digitada foi: {cont}')
