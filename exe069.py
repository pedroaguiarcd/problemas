homem=0
mulher20=0
mais18=0
while True:
    var1=int(input('Digite a idade: '))
    var2=str(input(' SEXO [M/F]:')).strip().lower()
    var3=str(input('Deseja cotinuar? [S/N]: ')).strip().lower()
    while var2 not in ['m', 'f']:
        print('Por favor, insira "M" para masculino ou "F" para feminino.')
        var2 = input('Sexo [M/F]: ').strip().lower()

    while var3 not in ['s', 'n']:
        print('Por favor, insira "S" para sim ou "N" para não.')
        var3 = input('Deseja continuar? [S/N]: ').strip().lower()


    if var1 >= 18:
        mais18+=1
    if var2 == 'm':
        homem+=1
    if var2 == 'f' and var1 < 20:
        mulher20+=1
    if var3 != 's':
        break
print(f'O total de homens é {homem}\n sao {mais18} pessoas maiores de 18 anos \n {mulher20} mulheres com menos de 20 anos')

# homem = 0
# mulher20 = 0
# mais18 = 0

# while True:
#     var1 = int(input('Digite a idade: '))
#     var2 = input('Sexo [M/F]: ').strip().lower()
#     var3 = input('Deseja continuar? [S/N]: ').strip().lower()

#     # Validação das respostas para sexo
#     while var2 not in ['m', 'f']:
#         print('Por favor, insira "M" para masculino ou "F" para feminino.')
#         var2 = input('Sexo [M/F]: ').strip().lower()

#     # Validação das respostas para continuar
#     while var3 not in ['s', 'n']:
#         print('Por favor, insira "S" para sim ou "N" para não.')
#         var3 = input('Deseja continuar? [S/N]: ').strip().lower()

#     if var1 >= 18:
#         mais18 += 1
#     if var2 == 'm':
#         homem += 1
#     if var2 == 'f' and var1 < 20:
#         mulher20 += 1

#     if var3 != 's':
#         break

# print(f'O total de pessoas é {mais18}')
# print(f'O total de homens é {homem}')
# print(f'O total de mulheres com menos de 20 anos é {mulher20}')