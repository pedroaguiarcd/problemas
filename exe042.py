print('-='*20)
print('VENDO RETOS')
print('-='*20)


a=float(input('digite aqui o comprimento da primeira reta:  '))
b=float(input('digite aqui o comprimento da segunda reta: '))
c=float(input('digite aqui o comprimento da segunda reta: '))
if a == b == c:
    print(f'A soma dos numeros formam um triangulo equilatero')
elif a == b or c==b:
    print(f'A soma dos numeros formam um triangulo isosceles')
elif a != b != c != a:
    print(f'A soma dos numeros formam um triangulo escaleno')
else:
    print('nao pode formar um triangulo')



