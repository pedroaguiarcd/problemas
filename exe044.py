preço=float(input('Digite o preço total das compras: '))
print('FORMAS DE PAGAMENTO:')
opçoes=print('''
[ 1 ] á vista dinheiro/cheque
[ 2 ] á vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
var2=int(input('qual opçao o senhor desaja?: '))
if var2 == 1:
    total=preço-(preço*10/100)
    print(f'o valor total da sua compra com desconto de 10% é{total}')
elif var2 == 2:
    total = preço-(preço*5/100)
    print(f'o valor total da sua compra com desconto de 20% é:{total}')
elif var2 == 3:
    total= preço/2
    print(f'o valor total da sua compra com parcela de 2x é: {total}')
elif var2 == 4:
    total=preço+(preço*20/100)
    total2=int(input('Digite em quantas parcelas: '))
    preço2=total/total2
    print(f'o valor total da sua compra com parcelas de {total2}x é {preço2} e o juros total é {total}')
else:
    print('\033[031m opçao invalida de pagamento!\033[m')
