dis=float(input('Digite em KM a distancia da sua viagjem: '))
diskm=dis*100
preç1=diskm*0.50
preç2=diskm*0.45
if dis <= 200:
    print(f' o preço da sua viagem é de {preç1}')
else:
    print(f'o preço de sua viajem é de {preç2}')