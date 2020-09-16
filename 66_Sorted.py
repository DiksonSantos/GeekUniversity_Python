'''
O Similar SORT()  só funciona em Listas. O SORTED()
  funciona em qualquer iteravel, INCLUINDO Tuplas, porém
  só da pra usar dentro do PRINT
  (Para ordenar os elementos da lista)
'''

lista = [6,2,4,3,9,1,8,5,7]
lista.sort()
print(lista)

#DICIONARIO E LISTA SOMENTE DENTRO DO PRINT:

dicionario = {6,2,4,3,9,1,5}
print(sorted(dicionario))


tupla = (6,2,4,3,9,1,5)
print(sorted(tupla))# ELE IMPRIMIRA\transformara em UMA LISTA

oUTRA_lISTA = [6,2,4,3,9,1,5,4,9,8]
print(sorted(oUTRA_lISTA))

#Usando parametros no SORTED

print(sorted(dicionario, reverse=True))

#Esse Eu Acabei de testar/Descobrir aqui
rev = list(reversed(lista))
#rev = list(reversed(dicionario))# NÃO FUNCIONA COM DICIONARIOS
print(rev)

Dicionario = {'chave':'Valor', 'Key':'Value', 'Sword':'Shield','Mother':'Daughter'}
print(sorted(Dicionario, key=len))

#Ordenar por quantidade de Musicas:

musicas = [
    {'titulo': 'Poly','tocou':3},
    {'titulo': 'StairwayToHeaven','tocou':4},
    {'titulo': 'EvenFLow','tocou':5},
    {'titulo': 'Alive','tocou':4},
    {'titulo': 'SimplyTheBest','tocou':6},
    {'titulo': 'The Best Around','tocou':7}
]

print(sorted(musicas, key=lambda musica: musica['tocou']))#Da Menos Para a Mais
print(sorted(musicas, key=lambda musica: musica['tocou'], reverse=True))#Da Mais para a Menos Tocada
