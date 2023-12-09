var1=str(input('Digite uma frase: ')).strip() .upper()
var2=var1.split()
var3=''.join(var2)
var4=''
for letras in range (len(var3) -1,-1,-1):
    var4+=var3[letras]
print(f' o inverso de {var4} é {var3}')
if var4 == var3:
    print('palindromo')
else:
    print('nao palindromo')
