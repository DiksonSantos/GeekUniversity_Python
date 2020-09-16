#Funções com Parametros:

#Refatorando uma função:
'''
def quadrado_de_7(Numero):
    return  Numero * Numero


cacl = quadrado_de_7(2)
print(cacl)

print(quadrado_de_7(3))
'''
'''
def cantar_parabens(aniversariante):
    print('Parabéns Pra você \nMuitos anos de vida')
    print(f'Viva o {aniversariante}')

cantar_parabens("Dikson 34 de idade")
'''

'''
#Nomeando Parametros:

def nome_completo(string1, string2):
    return f'Seu nome Completo é {string1} { string2}'
print(nome_completo("Dikson",'Santos'))

#Argumentos nomeados ou KeyWord Arguments

print(nome_completo(string1='Gow', string2='Rodrigues'))
'''

def soma_impares(Numeros):
    total = 0
    for num in Numeros:
        if num % 2 != 0: #Se o numero é Impar
            total += num #total recebe o valor que ele já tem + o novo numero IMPAR da sequencia
    return total
#lista = [1,2,3,4,5,6,7,8,9,0]
#lista2 = [1,2,3,4,5,6,7] # Ou seja Só esta somando os elementos IMPARES
#print(soma_impares(lista))

dicionario = {1,2,3,4,5,6,7}
print(soma_impares(dicionario))

if __name__ == '__main__':
    lista = [1,2,3,4,5,6,7,8,9,0]
    tupla = (1,2,3,4,5,6,7,8,9,0)
