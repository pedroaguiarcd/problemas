nome=input('digite seu nome: ')
var1=nome.split()
var2=var1[0]
var3=var1[-1]
print(f'{nome} tem como primeiro nome: {var2}\n e como ultimo: {var3}')





# O uso de -1 para acessar o último elemento de uma lista em Python é uma convenção comum. Em Python, as listas são indexadas a partir de 0, ou seja, o primeiro elemento tem índice 0, o segundo elemento tem índice 1, e assim por diante.

# Usar -1 como índice em uma lista permite acessar o último elemento sem a necessidade de saber o comprimento da lista com antecedência. Isso é conveniente, especialmente quando você está lidando com listas de tamanho variável.

# Por exemplo, se você tem uma lista com 5 elementos, lista[4] acessaria o último elemento. Se a lista tivesse 10 elementos, lista[9] acessaria o último elemento. Usando -1, você pode acessar o último elemento, independentemente do tamanho da lista, tornando o código mais flexível e geral.

# Aqui está um exemplo que ilustra isso:
# minha_lista = [10, 20, 30, 40, 50]

# ultimo_elemento = minha_lista[-1]  # Acessa o último elemento, que é 50

# print(ultimo_elemento)
# No exemplo acima, não precisamos saber o tamanho da lista com antecedência; apenas usamos -1 para acessar o último elemento.




