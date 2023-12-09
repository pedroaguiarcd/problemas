he=int(input('Digite um numero: '))
tot=0
for c in range (1, he + 1):
    if he % c == 0:
        print('\033[32m',end='')
        tot+=1
    else:
        print('\033[33m',end='')
    print(f'{c}',end=" ")
print(f'o numero {he} foi divisivel {tot} vezes')
if tot == 2:
    print('é numero primo!')
else:
    print('nao é numero primo')
