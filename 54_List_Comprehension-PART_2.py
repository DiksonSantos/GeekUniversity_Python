#Podemos adicionar estruturas adicionais logicas ás nossas List Comprehension

#Exemplos:

# 1

num = [1,2,3,4,5,6,7]

#Usa um laço FOR na Lista num -> se ekemento de num ...
pares = [numero for numero in num if numero % 2 == 0] #Isso aqui poderia ir diereto dentro de um Print tbm.
#print(pares)

impares = [numero for numero in num if numero % 2 != 0] # != 0   OU ==1
#print(impares)

#PODEria USAR O IF NOT em quaquer uma destas duas a cima. Assim como nas logo a baixo:

#impares = [numero for numero in num if numero % 2 == 1]
#print(impares)

pares_ = [numero for numero in num if numero %2]

impares_ =[numero for numero in num if not numero %2]
#print(pares_)
#print('\n', impares_)
#Esplicação  -> % de 2 é 1, e 1 em Python é True

# 2

#Eleento *2 -> Se os elementos tiverem resto 0 (Ou seja for PAR) -> Caso contrário /2 cada elemento.
#Ou seja se for IMPAR Mult por 2 | se for PAR Divida por 2
res = [numero * 2 if numero % 2 == 1 else numero / 2 for numero in num]
print(res)

#print(num * 2) #aPENAS dUPLICA A SEQUENCIA
