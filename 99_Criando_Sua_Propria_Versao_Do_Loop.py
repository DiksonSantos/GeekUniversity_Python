'''
Entendendo como o Loop funciona
criando minha propria versão do Loop
'''

#for num in [1,2,3,4]:
#    print(num)

'''
print('\n')

x = iter([1,2,3])
print(next(x))
print(next(x))
'''

def meu_for(iteravel):
    it = iter(iteravel)
    while True: #Para não parar até chegar no final da Lista
        try: #tente isto.
            print(next(it),end='') #Faça Isso
        except StopIteration: #Se chegar no final:
            break #Pare o processo.


lista = [1,2,3,4]

#fulano = meu_for(lista)
#print(fulano) #Cria um erro imprimindo NONE no final do processo.

#meu_for(lista) #Deu tudo certo.

meu_for('Dikson')
