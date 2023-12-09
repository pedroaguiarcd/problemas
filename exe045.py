import random
print('PEDRA!')
print('PAPEL!')
print('TESOURA!')
eu=input('Escolha do Jogador: ')
jogo=['pedra','papel','tesoura']
pc=random.choice(jogo)
print(f'Escolha do Bot: {pc}')
if eu == pc:
    print('empate!')
elif eu == 'pedra' and pc == 'papel':
    print('Pc Ganhou!')
elif eu == 'pedra' and pc == 'tesoura':
    print('Jogador ganhou!')
elif eu == 'papel' and pc == 'tesoura':
    print('Pc ganhou!')
elif eu == 'papel' and pc== 'pedra':
    print('Jogador ganhou!')
elif eu == 'tesoura' and pc == 'papel':
    print('Jogador Ganhou!')
elif eu == 'tesoura' and pc == 'pedra':
    print('Pc Ganhou!')
else:
    print('resposta invalida!')
