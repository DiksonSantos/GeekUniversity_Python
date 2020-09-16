#Exemplos:

numeros = [1,2,3,4,5,6]

res = [numero * 10 for numero in numeros] #Rapaaazzz

#print(res) #Multiplica por 10 cada um dos itens da lista.


#res = [numero / 2 for numero in numeros]
#print(res)

def funcao(valor):
    return valor * valor

res_ = [funcao(numero) for numero in numeros]

#print(res_)


'''
#List comprehension VS Loop:

#Com Loops:
numeros = [1,2,3,4,5]

numeros_dobrados = [] #DOBRADOSSSS
for numero in numeros:  #ISSO AQUI TEM A VER COM A LISTA DALI DO COMEÇO
    numeros_dobrado = numero * 2 #DOBRADOOO
    numeros_dobrados.append(numeros_dobrado) #DOBRADOSSS -> RECEBE O DOBRADOOO
print(numeros_dobrados) #IMPRIME DOBRADOSSSS QUE RECEBEU DOBRADOOO

#AGORA NÃO MAIS LOOPS -> USAREMOS O LIST COMPREHENSION:
#Substituimos TODAS  as linhas de codigo a cima por apenas esta aqui -> Faz a mesma coisa.
print([numero * 2 for numero in numeros]) #Isso é um LOOP de uma linha Apenas.
'''

# 1
nome = 'Gow Dikson'
#print([letra.upper() for letra in nome]) #NÃO SE ESQUEÇA DOS [] DENTRO DO PRINT!

# 2
def Maiuscula(nome):  # , sobre='' Segundo argumento Não Obrigatorio
    #Substitui a Letra na pos 0 por ela mesma em Mauiscula.
    #nome_ = nome.replace(nome[0], nome[0].upper())
    nome_ = nome.replace(nome[0], nome[0].upper())
    #sob = sobre
    #sobre = sobre.replace(sobre[0], sobre[0].upper())
    return nome_ #, sob


Nome = 'dikson'
Sobrenome = 'santos'
FRIENDS = ['MARIA', 'KATIFUNDA', 'BONECO', 'PAULO CINTURA', 'RAIMUNDO']
amigos = ['anibal','spot' ]
friends = ['Camila', 'Vento_Ventania', 'Astronauta']
dicionario = {'Spartacus', 'Maximus', 'Leonidas'}

#print([FRIENDS[0].upper() for FR in FRIENDS])

#print([Maiuscula(amigo, dicionario) for amigo in amigos])

print([Maiuscula(friend) for friend in friends])
#print([Maiuscula(amigos, dicionario) for am in amigos for DC in dicionario])
#print([Maiuscula(Nome, Sobrenome) for N in Nome for SB in Sobrenome])
#print([Maiuscula(Nome, Sobrenome)])
#print([Maiuscula(dicionario) for DIC in dicionario])
#print([Maiuscula(amigos)])
#print(Maiuscula(Nome))
#print(Maiuscula(Nome, Sobrenome))

'''A FUNÇAO A CIMA NÃO FUNCIONA COM DICIONARIOS OU LISTAS, APENAS COM VARIAVEIS STR'''

# 3

#print([numero * 3 for numero in range(1,10)])

# 4
#print([bool(valor) for valor in [0, [], '', True, 1,3,14]])


# 5 :

#print([str(valor) for valor in [0, [], '', True, 10,31,15]])
