'''
dicion = {'chave':'valor', 'key':'value'}
for I, J in dicion.items():
    print(I, J)

for J in dicion.values():  #Só mostrou o que estava Depois dos :
    print(J, 'Conteudo')

for X in dicion.keys(): #Printou Só valores antes das :
    print(X, "CHAVE")

dicion['Mês'] = 'Fevereiro'
nova_info = {'Março': 'Realização'}
New_2 = {}
New_2['Ilave'] = 'Valor'
dicion.update(nova_info) #Inseriu
Junta = dicion,New_2 #Concatenou
print(dicion)
print(Junta)
dicion.update(New_2)
Maio = {'Maio': 'Ritch'}
Maio.update({'Maio': 'Glory'}) #Faz um Update na Chave\ Valor
dicion.update(Maio)
print(dicion, 'Final')
del dicion['chave'] #Só um por Linha
del dicion['key']
print(dicion)
'''

'''
D = dict(a=1, b=2, c=3)
#dict(a=1, b=2, c=3)
print(type(D))
#print(type(dict))
for I, J in D.items():
    print(I, J, end=', ')
print('\n',D.clear(), "Limpou!")

outro = {}.fromkeys('Cofre','Dinheiro') #Chave & Valor
print(outro, type(outro))

#Valor comum para todas as chaves:
User = {}.fromkeys(['Nome', 'Endereço', 'Origem'], 'Não_Sei_!')
print(User)

See = {}.fromkeys(range(1, 11), "New")
print(See, end=', ')
'''
Estudantes_Python = {'Maco', 'Pat', 'Helen', 'peter', 'July'}
Est_Java = {'Ferdinand', 'Gustafson', "Joe", "DyeAnna", 'July', 'Pat'}

#Alguns alunos estão nos Dois Grupos.

#Unicos = Est_Java.union(Estudantes_Python)
Unicos2 = Estudantes_Python | Est_Java
print(Unicos2)
