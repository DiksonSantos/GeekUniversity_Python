
def soma_impares(Numeros):
    total = 0
    for num in Numeros:
        if num % 2 != 0: #Se o numero é Impar
            total += num #total recebe o valor que ele já tem + o novo numero IMPAR da sequencia
    return total
#lista = [1,2,3,4,5,6,7,8,9,0]
#lista2 = [1,2,3,4,5,6,7] # Ou seja Só esta somando os elementos IMPARES
#print(soma_impares(lista))

#dicionario = {1,2,3,4,5,6,7}
#print(soma_impares(dicionario))

if __name__ == '__main__':
    lista = [1,2,3,4,5,6,7,8,9,0]
    tupla = (1,2,3,4,5,6,7,8,9,0)
'''
else:
    print('O Modulo Funções Com Parametros Paython Foi Importado')
'''



