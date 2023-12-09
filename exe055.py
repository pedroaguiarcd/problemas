# ESSE DE BAIXO FOI FEITO SOLO, APENAS POR MIM!
peso1=float(input('1° Peso: '))
peso2=float(input('2° Peso: '))
peso3=float(input('3° Peso: ' ))
peso4=float(input('4° Peso: '))
peso5=float(input('5° Peso: '))
maior=max(peso1,peso2,peso3,peso4,peso5)
menor=min(peso1,peso2,peso3,peso4,peso5)
peso=float(input(f'Peso da {c} pessoa: kg'))
menor=min(peso)
maior=max(peso)
print(f'maior peso {maior}kg')
print(f'menor peso {menor}kg')

# O DE BAIXO PEGUEI DOS COMENTARIOS!!!!!
pesos = [float(input(f'Peso da {a}º pessoa: ')) for a in range(1, 6)]
print(f'O maior peso foi de {max(pesos)}Kg\nfO menor foi de {min(pesos)}Kg!')

# ESSE É O CODIGO DO GUANABARA, OU SEJA O 1° EU FIZ, O 2° FOI DOS COMENTARIOS E 3° É DO GUANABARA
maior=0
menor=0
for p in range(1,6):
    peso=float(input(f'Peso da {p}° pessoa: '))
    if p == 1:
        maior=peso
        menor=peso
    else:
        if peso > maior:
            maior=peso
        if peso < menor:
            menor = peso
print(f'O maior peso lido foi de {maior}Kg')
print(f'O menor peso lido foi de {menor}Kg')