'''
Iterador
Retorna Um Dado Por Vez
Faz Uso da Função NEXT()


Iteravel
Objeto que retorna um ITERADOR
'''

#Exemplos de Iteraveis:
nome = 'Dikson'
lista = [1,2,3,4]

#Convertendo as variaveis para Objetos Iteraveis:
itera = iter(nome)
itera_2 = iter(lista)

#Imprimindo Eles:
print(next(itera))# D
print(next(itera))# I
print(next(itera))# K
print(next(itera))# S
print(next(itera))# O
print(next(itera))# N

print('\n')

print(next(itera_2))# -> 1
print(next(itera_2))# -> 2

#Para esxolher Os Itens a Serem imprimidos:

'''
OU SEJA : É UMA FORMA BURRA DE FAZER O QUE O LAÇO 'FOR' JÁ FAZ A MUITO TEMPO.
'''
