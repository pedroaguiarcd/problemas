import random
na=random.randint (0,10)
while na:
    aposta=float(input('adicione a quantia que deseja apostar: '))
    ad=int(input('Digite um numero, jogador: '))
    print(f'o numero escolhido pelo jogador foi: {ad}')
    print(f'o numero pensado pelo computador foi...?')
    if ad == na:
        print('Parabens! voce acertou!')
        print(f'+{aposta} de saldo')


    else:
        print('Que pena... Voce perdeu!')
        print(f'-{aposta} de saldo')

