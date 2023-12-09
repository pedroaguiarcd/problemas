var1=int(input('escreva um numero inteiro: '))
var2=int(input('escreva um numero inteiro: '))

if var1 > var2:
    print(f'o primeiro valor é maior')
elif var2 > var1:
    print(f'o segundo valor é maior')
else:
    print(f'nao existe valor maior, {var1} e {var2} sao iguais')