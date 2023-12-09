# mais1k=0
# total=0
# nomebarato=''
# barato = float('inf')
# while True:
#     nome=str(input('Digite o nome do produto: '))
#     preço=int(input('Preço: '))
#     total+=preço
#     cont=str(input('Quer continuar a compra?[S/N]: ')).strip().lower()
#     while cont not in ['s', 'n']:
#         print('resposta invalida!')
#         cont=str(input('Quer continuar a compra?[S/N]: ')).strip().lower()
#     if preço > 1000:
#         mais1k+=1
#     if preço < nomebarato:
#         nomebarato=nome
#         barato=preço

#     if cont != 's':
#         break
# print(f'Total: {total} \n produtos com mais de 1k: {mais1k} \n produto mais barato: {barato}')


mais1k = 0
total = 0
nomebarato = ''
barato = float('inf')

while True:
    nome = input('Digite o nome do produto: ')
    preco = float(input('Preço: '))
    total += preco
    cont = input('Quer continuar a compra? [S/N]: ').strip().lower()

    while cont not in ['s', 'n']:
        print('Resposta inválida!')
        cont = input('Quer continuar a compra? [S/N]: ').strip().lower()

    if preco > 1000:
        mais1k += 1

    if preco < barato:
        nomebarato = nome
        barato = preco

    if cont != 's':
        break

print(f'Total: R$ {total:.2f}')
print(f'Produtos com mais de 1k: {mais1k}')
print(f'Produto mais barato: {nomebarato}')

    
