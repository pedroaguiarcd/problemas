valor=float(input('Digite o valor da casa: '))
salario=float(input('Digite o salario do comprador: '))
anos=int(input('em quantos anos ele vai pagar: '))
prestaçao=valor/(anos*12)
sar=salario*30/100


if prestaçao <= sar:
    print(f'\033[1;32mparabens! voce possui condiçoes de comprar a casa!\033[m')
else:
    print(f'\033[1;31minfelizmente voce nao tem condiçoes de comprar a casa\033[m')    



