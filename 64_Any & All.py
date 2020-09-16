'''
Any & All

all() Retorna True e False
Ele apenas verifica -> Se todos os elementos forem True, mas se UM for False
ele retorna False ... Muito simples.
'''

#print(all([0,1,2,3,4])) #Apenas o ZERO é False, então o resultado sera False

Lista_True = [1,2,3,4]
#print(all(Lista_True)) #Aqui da True


Letra = ['Django', 'Diamente', 'Dinamite', 'Dinamo', 'Denmark', 'Deny','Tart']

#verifica = all([Letra[0] == 'D' for Letras in Letra])
#print(verifica)

#print(all([L[0] == 'D' for L in Letra]))

'''
for L in Letra:
    if L[0] == 'D':
        print('SIM')
    else:
        print('NÃO')
'''




# ANY Retorna true se Qualquer Elemento do iteravel for Verdadeiro

print(any(Lista_True))# Se Algum elemento na lista True for verdadeiro, ele retorna True

numeros = [0,1,3,5] #No caso aqui todos tem resto de divisão DIFERENTE de 0

#Se algum numero na lista numero tiver resto de divisão = 0 então True
compreencao = [any([num for num in numeros if num % 2 == 0])]
print(compreencao) #Resultado = False

