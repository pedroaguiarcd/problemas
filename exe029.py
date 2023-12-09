import random
velocidade=random.randint(80,300)
velopermetida=80
valor=float((velocidade*7))
if velocidade >= velopermetida:
    print(f'Sua velocidade {velocidade}')
    print(f'voce excedeu o limite de velocidade! O valor de sua multa é de {valor}')
else:
    print(f'Sua velocidade {velocidade}')
    print('Sua velocidade esta dentro no limite permetido!')