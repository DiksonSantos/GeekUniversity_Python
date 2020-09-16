'''
A CADA VEZ QUE O CODIGO É EXECUTADO ELE DESAPARECE.
'''
Lista0 = ['a','b','c']
lista = [1,2,3]


'''
ZIPA = zip(Lista0, lista) #Poderia inclir mais de Duas listas tbm , "lista02".
print(list(ZIPA),'Lista') # [('a', 1), ('b', 2), ('c', 3)] -> Une elementos de Indices Iguais.

ZIPA = zip(Lista0, lista)
print(tuple(ZIPA),"Tupla")

ZIPA = zip(Lista0, lista)
print(dict(ZIPA), 'DICIONARIO')

ZIPA = zip(Lista0, lista)
print(set(ZIPA),"SET ?") #Dicionario com Tuplas (???)

ZIPA = zip(Lista0, lista)
print(type(ZIPA),"Tipo") #Class 'zip'
'''

tupla = (1,2,3)
lista0 = [0,0,0]
lista_ = [4,5,6]
Alunos = ['Maria', 'João', 'Betina']
Dicionario = {'Alpha':'Uno','Beta':'Twice','Gama':'Arvore'}
Dicionario2 = {'Alpha':0,'Beta':11,'Gama':22}


#Como estamos usando uma func MAX na tupla e na lista, só vai ser mostrado o maior valor entre eles dois.
#         Alunos       Tupla    lista_
final = {dado[0]: max(dado[1], dado[2]) for dado in zip(Alunos,tupla,lista_)}
print(final) #Só a Tpla e a Lista Interagem



#Mesma coisa, Mas Com MAP:

final2 = zip(Alunos, map(lambda nota: max(nota), zip(lista0,lista)))
print(list(final2)) #Pode Ser List OU DICT
