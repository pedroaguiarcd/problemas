var1=float(input('Digite o seu salario aqui: '))
if var1 <= 1250:
    hehe=('salario esta disponivel para aumento de 15%')
    novo=var1+(var1*15/100)
    
else:
    hehe=('seu salario esta disponivel para aumento de 10%')
    novo=var1+(var1*10/100)
    
print(f'{hehe} e ele sera de: {novo:.2f}')