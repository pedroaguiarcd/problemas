soma=0
cont=0
print('DIGITE 6 VALORES INTEIROS')
for c in range (1,7):
    num=int(input(f'digite o {c} valor: '))
    if c % 2 == 0:
        cont+=1
        soma+=num
print(f'A soma de todos os numeros é {soma} os numeros pares validos foram {cont}')
