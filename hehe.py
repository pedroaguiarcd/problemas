a = input('Digite algo: ')
print(f'O tipo primitivo desse valor é {type(a)}')
print(f'Só tem espaços? {a.isspace()}')
print(f'É um número? {a.isnumeric()}')
print(f'É alfabético? {a.isalpha()}')
print(f'É alfanumérico? {a.isalnum()}')
print(f'Está em maiúsculas? {a.isupper()}')
print(f'Está em minúsculas? {a.islower()}')
print(f'Está capitalizado? {a.istitle()}')


n = str(input('Digite algo: '))
print(f'''
    É Alpha númerico? {n.isalnum()}
    É alpha? {n.isalpha()}
    É Minuscula? {n.islower()}
    É maiuscula? {n.isupper()}
    Está capitalizada? {n.istitle()}
    É Decimal? {n.isdecimal()}
    É numérica? {n.isnumeric()}
    É espaço? {n.isspace()}
    Tipo: {type(n)}
''')
