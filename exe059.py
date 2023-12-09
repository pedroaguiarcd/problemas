from time import sleep
var=int(input('Escolha o primeiro numero: '))
var1=int(input('Escolha um segundo numero: '))
while True:
    print('[ 1 ] SOMAR')
    print('[ 2 ] MULTIPLICAR')
    print('[ 3 ] MAIOR')
    print('[ 4 ] NOVOS NUMEROS')
    print('[ 5 ] SAIR DO PROGRAMA')
    
    print(f'Os numeros Digitados foram {var} e {var1}')

    var3=int(input('Quais das opções desejas? '))

    if var3 == 1: 
        print(var+var1)
        sleep(1)
    elif var3 ==2:
        print(var*var1)
        sleep(1)
    elif var3 == 3:
        print(max(var,var1))
        sleep(1)
    elif var3 == 4:
        var=int(input('Digite um novo primeiro numero: '))
        var1=int(input('Digite um novo segundo numero: '))
        sleep(1)
    elif var3 == 5:
        print('finalizando programa...')
        break
    else:
        print('opção invalida!')

        