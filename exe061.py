p1 = int(input('Primeiro termo: '))
ra = int(input('Razão: '))

n = 1  # Inicializa o contador para o primeiro termo
while n <= 10:  # Este loop irá calcular os 10 primeiros termos
    termo = p1 + (n - 1) * ra
    print(f'Termo {n}: {termo}')
    n += 1  # Incrementa o contador para calcular o próximo termo
    