cont=0
n=0
while True:
    var1=int(input('Digite um numero [999 para parar o programa...]'))
    if var1 == 999:
        break
    cont+=1
    n+=var1
print(f' A soma entre os {cont} numeros é {n}')