import datetime
old=int(input('digite o ano em que voce nasceu: '))
atual = datetime.datetime.now().year
idade= atual - old

if idade > 18:
    print('Voce é maior de idade, portanto podera se alistar ate 45 anos!')
elif idade == 18 :
    print('é o momento ideal para se alistar!')    
elif idade < 18 :
    print('voce ainda nao completou 18 anos')   
