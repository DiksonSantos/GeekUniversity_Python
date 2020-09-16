#Parecudo com Teoria Dos Conjuntos de Matemática.

#Bons para armazenar elementos mas sem se importar
# ...com a ordenação deles (Chaves valores e itens
#...duplicados são aceitos).


#Forma 1

#s = set({1,2,3,4,5,6,7,7,7,7})

#print(s) #Não Printou os numeros repetidos

#Forma 2
'''
s = {1,2,3,4,5,5}
print(s)
print(type(s))

Meu_Nome = "Dikson"
conv = set(Meu_Nome)
print(conv) #Tratou cada letra como um item\elemento diferente

if 'D' in Meu_Nome:
    print('Tem')
'''

'''
s = [1,2,3,4,5,6,7,7,7,7]

#Desta forma ele acaba imprimindo todas as virgulas tbm
#s = '1,2,3,4,5,6,7,7,7,7'

lista = list(s)
print(lista, len(lista),"Elementos Aqui"," Lista")

tupla = tuple(s)
print(tupla)

conjunto = set(s)
print(conjunto," Não imprime Itens Repetidos na String")

Dicionario = {}.fromkeys([1,2,3,4,5,6,7,7,7,7]," Dict")
print(Dicionario) #Cria Uma Chave chamada Dict
'''
'''
#USOS INTERESSANTES COM SETs :

cidades = ['Belo Horizonte', 'SP', 'Campo Grande', 'Cuiaba', 'Campo Grande', 'SP', 'Cuiaba']
print(len(cidades))

#Agora precisamos saber quantas cidades distintas temos na lista. Podemops usar o SET
print(len(set(cidades))) #Com o SET Não RE-Conta Valores já contados. = 4 Cidades

#SET -> Remove Duplicidades.

#print(set(cidades))# Não mostra Valores repetidos.
'''
'''
conjunto = {3,2,1,99,0,8,7} #Geram uma ordenação propria dele.
print(conjunto)
'''

#Adicionando Elementos a um Conjunto:
Con = {1,2,3}
Con.add(4) #Só aceita UM por Vez
Con.add(5) #Adiciona no final da fila.
Con.add(5) #Não adiciona Itens Repetidos !!  Mas tbm não da erro.
#print(Con)

Con.remove(5) #Remove o VALOR
#print(Con)
#Con.remove(67)# Da Erro
#Caso valor Não encontrado Da Erro

Con.discard(4)# Com o discard SE ele não encontrar o Item na lista, Não da Erro tbm.
#print(Con) #Discard é melhor.

#Copiando Um conjunto para Outro:

#Deep Copy
novo = Con.copy()
#print(novo)

#Shallow Copy:

new = Con
new.add(8)
#print(new)

#Podemos remover todos os itens de um COnjunto:

Con.clear()
#print(Con, 'Vazio')


#https://www.vivaolinux.com.br/topico/Python/diferenca-entre-print-e-return-no-python
#CONTINUA EM 47Min

#Metodos Matematicos de Conjuntos:

Estudantes_Python = {'Maco', 'Pat', 'Helen', 'peter', 'July'}
Est_Java = {'Ferdinand', 'Gustafson', "Joe", "DyeAnna", 'July', 'Pat'}

#Alguns alunos estão nos Dois Grupos.

Unicos = Est_Java.union(Estudantes_Python)
#print(Unicos) #-> Juntou as duas e Não repetiu Valores iguais das duas.


#FORMA 2:
#Utilizando o barrinha Pipe  |
Unicos2 = Estudantes_Python | Est_Java #Mesma coisa ->Une as duas listas e não imprime itens repetidos.
#print(Unicos2)
#Removemos as Duplicidades com esses dois métodos a cima.

#________________

#Conjunto de estudantes que estão em AMBOS os gupos.
Ambos = Est_Java.intersection(Estudantes_Python)
#print(Ambos) #Somente Os Nomes que estão em ambos os Grupos.

Abos_2 = Estudantes_Python & Est_Java
#print(Abos_2) #Mesma Resultado!
#UNIÃO & INTERCECÇÃO => TEORIA DOS CONJUNTOS USADA EM PYTHON
#___
#Estudantes que Estão SÓ Num Curso:
So_Python = Estudantes_Python.difference(Est_Java)
print(So_Python, "São Estudantes Somente de Python")

So_JAVA = Est_Java.difference(Estudantes_Python)
print(So_JAVA, "Estudam Só JAVA")
