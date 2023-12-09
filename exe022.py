#  ESSE PRIMEIRO FOI FEITO POR MIM, SEM AJUDA! O SEGUNDO FOI AS CORREÇOES FEITAS PELO CHATGPT, ELE ESTA SENDO MEU PROFESSOR!

# nome=(input('Digite seu nome inteiro: '))
# v1=nome.upper()
# v2=nome.lower()
# v3=len(''.join(nome))
# v4=nome.split()
# vq=len(v4) 
#print(f'''Nome com todas as letras maiusculas: {v1}\n
    #Nome com todas as letras minusculas: {v2}\n
    #Total de letras sem o espaço:{v3}\n
     #quantas letras tem o primeiro nome:{vq}
 #''')

nome = input('Digite seu nome inteiro: ')
v1 = nome.upper()
v2 = nome.lower()
v3 = len(nome.replace(" ", ""))  # Remove espaços e conta as letras
v4 = nome.split()
vq = len(v4[0])  # Conta as letras no primeiro nome

print(f'''Nome com todas as letras maiúsculas: {v1}
Nome com todas as letras minúsculas: {v2}
Total de letras sem os espaços: {v3}
Quantas letras tem o primeiro nome: {vq}
''')

# CORREÇOES FEITAS POR ELE(ACHEI BOM ANOTAR)

# Neste código, eu fiz as seguintes correções:

# Usei nome.replace(" ", "") para remover os espaços em branco da string e, em seguida, usei len() para contar as letras. Isso corrige o cálculo do total de letras sem espaços.
# Usei v4[0] para obter o primeiro nome da lista gerada por split(). Isso permite contar as letras no primeiro nome corretamente.
# Agora, o código deve funcionar conforme o esperado.