#Named Tuples:
'''
tupla = (Num:1,N:2,Number:3)

print(tupla[1])
'''
from collections import  namedtuple



#tupla = namedtuple(Num:1,N:2,Number:3)
#Forma 1
cachorro = namedtuple('Cão', 'Idade Race Name')

#Forma2

cachorro2 = namedtuple("cachorro", "Nome, raca, peso")

#Forma3
Cachorrao = namedtuple('Cao', ['Idade', 'race', 'name'])


#How to use:

ray = Cachorrao(Idade=2, race='Pastor', name='Xray')
print(ray)
print(ray[1]) #O numero é o indice
print(ray.name) #Assim é mais facil 
