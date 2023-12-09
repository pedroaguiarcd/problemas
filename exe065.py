
# while True:
#     var1=int(input('Digite seu numero: '))
#     print('QUER CONTINUAR? [S/N]')
#     opç=str(input('Digite aqui se deseja ou nao continuar: ')).upper
#     if opç == 'S':
#         var1=int(input('Digite seu numero: '))
#         var2=(max(var1,var1))
#         var3=(min(var1,var1))
#         var1+=var1
#     if opç == 'N':
#         print('finalizando programa...')
#         break
#     else:
#         print('resposta invalida')

# print(f'A media dos numeros é {var1} e, o maior numero é {var2} e o menor {var3}')

contador = 0
soma = 0
maior = float('-inf')
menor = float('inf')

while True:
    var1 = int(input('Digite seu número: '))
    soma += var1
    contador += 1

    if var1 > maior:
        maior = var1

    if var1 < menor:
        menor = var1

    continuar = input('QUER CONTINUAR? [S/N]: ').strip().upper()

    if continuar == 'N':
        break

if contador > 0:
    media = soma / contador
else:
    media = 0

print('Finalizando programa...')
print(f'A média dos números é {media:.2f}')
print(f'O maior número é {maior}')
print(f'O menor número é {menor}')
