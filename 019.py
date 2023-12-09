from math import radians, sin, cos, tan
an=float(input('digite o valor do angulo que deseja: '))
seno=sin (radians(an))
cosseno=cos(radians(an))
tangente=tan(radians(an))
print(f'o valor do seno é: {seno:.2f}')
print(f'o valor do cosseno é: {cosseno:.2f}')
print(f'o valor do tangente é: {tangente:.2f}')
