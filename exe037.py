var1=int(input('Digite um numero inteiro: '))
print('''ESCOLHA UMA DAS BASES PARA A COVERSÃO:
    [ 1 ] converter para binario
    [ 2 ] converter para octal 
    [ 3 ] coverter para hexadecimal''')
opçao=int(input('sua opçao foi: '))
if opçao == 1:
    print(f'o numero {var1} para binario é {bin(var1)[2:]}')
elif opçao == 2:
    print(f'o numero {var1} para octal é {oct(var1)[2:]}')
elif opçao == 3:
    print(f' o numero {var1} para hexadecimal é {hex(var1)[2:]}')
elif opçao != 3 and 1 and 2:
    print('resposta invalida')