#Exemplos

numeros = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6}

#Ou-> Guarda a chave e eleva o valor ao Quadrado:
quadrado = {chave : valor ** 2 for chave, valor in numeros.items()}

#print(quadrado)#Cada valor das chaves Foi elevado a 2(Quadrado)

'''
#Este aqui eu que 'inventei' -> Ele acopla a palabra ' Chave' Ás chaves do Dicionario:
quadrado2 = {chave : valor +' Chave' for valor, chave in numeros.items()}
print(quadrado2)
'''

'''
Lista_Numeeros = {1,2,3,4,5}

#Aqui ele Disse pro Python repetir -> valor & valor OU
LQuad = {valor: valor ** 2 for valor in Lista_Numeeros }
print(LQuad)# Ele Enumera as Chaves(Devido ao FOR) e eleva a 2 Os Valores.
#print(10**2)
'''

'''
chaves = 'abcde'
valores = [1,2,3,4,5]

#Usou a Var 'chaves' como Chave , e a Var 'valores' como os Valores do Dicionario 'mix'
mix = {chaves[I] : valores[I] for I in range(0, len(chaves))}
print(mix)
'''

#Exemplo com logica condicional:

numeros = [12,3,4,5]

#Sendo 'num' o elemento a ser percorrido na lista 'numeros'
#...num recebeu o codigo de Par ou Impar nos Parenteses
#... e logo aopos um FOR para especificar quem é quem no processo.
res = {num:('Par' if num % 2 != 1 else "Impar") for num in numeros}
print(res)
