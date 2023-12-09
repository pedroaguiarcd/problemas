print('-='*20)
print('VENDO RETOS')
print('-='*20)


a=float(input('digite aqui o comprimento da primeira reta:  '))
b=float(input('digite aqui o comprimento da segunda reta: '))
c=float(input('digite aqui o comprimento da segunda reta: '))
if a+b>c and c+b>a and a+c>b:
    print(f'A soma dos numeros formam um triangulo')
else:
    print(f'A soma dos numeros nao formam um triangulo')


