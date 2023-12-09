import random 
win=0
while True:
    var1=int(input('digite um numero: '))
    var2=input(('Digite [P/I]: ')).strip().lower()S
    var3=(random.randint(1,20))
    resultado = (var1 + var3) % 2 == 0

    if (var2 == 'p' and resultado) or (var3 == 'i'and not resultado):
        print(f'Parabens, voce ganhou! o numero do robo foi {var3}')
        win+=1
    else:
        print(f'voce perdeu! o numero do robo foi {var3}')
        break
print(f'O numero de vitorias do jogador foi de {win}')