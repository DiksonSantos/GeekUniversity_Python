#Set Comprehension

lista = [1,2,3]

set = {1,2,3}

num = {num for num in range(0,9)}
#print(num)

numeros = {x**2 for x in range(10)}
#print(numeros)

#Convertendo Dicionario em Lista:
#No caso da variavel 'numeros' NÃO deu certo. Precisam haver chaaves e valores para se especificar  que se quer.
chave_valor = {'Chave':'Valor', 'Seg':'Segmento'}
Lista_num = list(chave_valor.values()) #Pode especificar .key  ,  .values , .items
#print(Lista_num)
#https://www.pythoncentral.io/convert-dictionary-values-list-python/

'''
vari = 0 in range(10)
for I in range(0,10):
    print(I,end=' ')
'''
numeros__ = [[x**2 for x in range(10)]]
#print(numeros__)

#Outra maneira mais dirta Economiza uma linha.
print([[x**2 for x in range(10)]])

#Pra fazer um Dicionario:
dicio = {x: x**2 for x in range(10)} #Apenas Especificque o 'x' como sendo a chave
print(dicio)


