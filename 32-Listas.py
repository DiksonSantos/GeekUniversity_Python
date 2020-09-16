lista1 = [1,2,3,4,5,6,7,8,9]

lista2 = ["G", "o","w"," ","D","i","k","s","o","n"]

lista3 = [0,0,0,0,0,0,0,0,0,0]

lista4 = list(range(12))

#print(lista4)

lista5 = ["Gow Dikson"]

#Checar valores numa Lista:

letra = "Gow Dikson"
'''
if letra in lista5:
    print("Encontrei")
else:
    print("Nada aqui")
'''
lista3.insert(1,"A") # A na posição 1.    -> NÃO SUBSTITUI VALOR, MAS SIM REALOCA OS ANTERIORES.
lista3.insert(3,"B") #B na posição 3.
lista3.append([1,2,3,4]) #Adiciona varios itens, mas é na verdade um item\lista
lista3.extend([10,11,13,14]) #Deste modo SIM Coloca mais itens dando continuidade á Lista.
#print(lista3)

lista5.extend(" Santos")
#print(lista5)


LISTA6 = lista1 + lista2
#print(LISTA6)

'''
lista2.reverse()
print(lista2)
'''
#print(len(lista2)," Itens")

Removido = lista1.pop(-1) #Removi Ultimo Item da lista.
guardado = Removido  #Aqui Guardo o Ultimo Item Removido.
#print(guardado) #Mostrando o Ultimo Item Removido.
lista3.clear() #Lipei a lista
lista3.append(5) # Adicionei o 5
#print(lista3) #Mostrei a Lista.


#Continuar em 1H e 4Min
Meu_Nome = "Gow Dikson"
'''
#Separa pelos espaços. Cada Palavra se torna UM INDICE de uma lista.
Dic = Meu_Nome.split() #Não Funcionou com a 'lista5'  por exemplo.
print(Meu_Nome)  #Sem o metodo Split
print(Dic) #Com Split
'''
#
'''
#Converter LISTA Em String:
lista6 = ["Programação", "Em", "Python", "Excencial"]
#print(lista6)
curso = ' - '.join(lista6) #Separa os elementos de uma lista com o que estiver entre " "
print(curso)


#Continuar em 1H e 11Min
'''
#
'''
#Lista com N tipos de dados

lista6 = [1,2.34, True, "Gow","Dikson",[1,2,3] , 4545]
#teste = '$'.join(lista6) #join Só funciona com Listas STRINGs
print(type(lista6))
'''
#
'''
soma = 0
for listasss in lista4:
    print(listasss,end="-")
    soma+= listasss
print('\n',soma) #Somou todos os numeros da lista
'''
#
'''
carrinho = []
produto = 'Budega'
while produto != "S":
    print("Adiciona Mais Produtos")
    produto = str.upper(input("Nome Produto: "))
    if produto != "S":
        carrinho.append(produto)
for produto in carrinho:
    print(produto.title(),end="-")
'''
#

cores = ['azul', 'amarelo', 'branco', 'verde', 'anil']

#for cor in cores:
#    print(cor)
'''
indice = 0
while indice <len(cores): #Imprime o que estiver em Indice enquanto indice tiver menos elementos que cores
    print(cores[indice])
    indice+=1 #A cada impressão ou loop, indice ganha +1
'''
#CONTINUAR EM 1H E 36MIN

#
'''
for indice, cor in enumerate(cores): #CRIA CHAVE E VALOR PARA CADA ELEMENTO DA ISTA
    print(indice,cor) #SENDO 'INDICE' A POSIÇÃO DE CADA ELEMENTO DA LISTA
'''
'''
#Listas aceitam Itens repetidos.
LISTA = []
LISTA.append(42)
LISTA.append(42)

for i in LISTA:
    print(i)
'''
#
'''
#ENCONTRAR INDICE NUMA LISTA:
lista_num = [5,6,7,8,9,10,11,12,"Jaba", "Cavalos"]
print(lista_num.index("Cavalos")) #EM QUE POSIÇÃO ESTA "Cavalos" NESTA LISTA

#BUSCAR ITEM A PARTIR DE UM ITEM DA LISTA:
LISTA_nUMERI = [5,6,7,5,8,9,0]
print(LISTA_nUMERI.index(5,1)) #Indice do Numero 5 a Partir do primeiro Indice da Lista.
# Resultado sera 3, ou Terceira Posição ignorando o primeiro 5 que esta na posição 0
print(LISTA_nUMERI.index(9,5)) #Nove a partir da Pos 5, na qual 9 esta.
'''

'''
#SLICEs:
lista = [1,2,3,4,5,6,7,8,9,10,12]
print(lista[1:10:2]) #De UM a DEZ de DOIS em DOIS.
print(lista[0::2]) #Um até o final de 2 em 2.
print(lista[11::-1]) #Indice 11 até o fim, Ao contrário.
print(lista[::-1]) #Tbm Inverte
lista.reverse()
print(lista) #Bem Mais Simples.

print(sum(lista))
print(max(lista))
print(min(lista))
print(type(lista))
TUPLA = tuple(lista) #Converteu Lista Para tupla.
print(TUPLA)
'''
'''
#Desempacotamento de Lista.
listasss = [1,2,3,4] #A quantidade de variaveis tem que ser igual a quantidade de
#...valores da lista.
num1, num2, num3, num4 = listasss
print(num1,num2, num3, num4)
#print(num4)
'''

#Shallow Copy & Deep Copy:

#Deep Copy:
lista = [1,2,3]
#print(lista)

nova_lista = lista.copy()
print(nova_lista,"Nova Lista.copy")

lista.append(13)
print(lista,"Append")

#Shallow Copy
