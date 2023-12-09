from time import sleep
cor=(''' ESCOLHA AS CORES DOS FOGOS: 
[ 1 ] vermelho
[ 2 ] verde
[ 3 ] amarelo
''')
esc=int(input('ESCOLHA UMA COR PARA OS FOGOS!'))
if esc == 1:
    print('voce escolheu \033[1;31m vermelho! \033[m')
elif esc == 2:
    print('voce escolheu \033[1;34m verde! \033[m')
else:
    print('voce escolheu \033[1;33m amarelo! \033[m')

print('A CONTAGEM JA VAI COMEÇAR!')

for c in range (10,0,-1):
    print(c)
    sleep(1)


print('BOOOOMMMM!!!')
