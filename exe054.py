from datetime import date
atual=date.today().year
# contador maior
totmaior=0 
# contador menor
totmenor=0
# considera maior idade com =>21
for c in range(1,8):
    nasc=int(input(f'A {c}° pessoa nasceu em: '))
    idade=atual-nasc
    print(f'voce tem {idade} anos')

    if idade >= 21: 
        # cotadores a baixo
        totmaior += 1
    else:
        totmenor += 1
        
print(f'Ao todo tivemos {totmaior} maior de idade ')
print(f'Ao todo tivemos {totmenor} menores de idade')