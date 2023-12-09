peso=float(input('Digite seu peso: '))
alta=float(input('Digite sau altura: '))
imc=peso/(alta**2) 
print(f'seu imc é: {imc:.1f}')

if imc < 18.5:
    print('Voce esta abaixo do peso ideal')
elif 18.5 <= imc < 25:
    print('Voce esta no peso ideal, Parabens!')
elif 25 <= imc < 30:
    print("Voce esta com sobrepeso ideal")
elif 30 <= imc < 40:
    print('voce esta com obesidade, cuidado!') 
elif imc < 40:
    print('voce esta com serios riscos de saude, procure ajuda!')
