'''
Iterador Customizado
'''

'''
#For Comun:
for n in range(0, 11):
    print(n)
'''
#ESTA CLASSE E SUAS FUNÇÕES É UMA RÉPLICA DO RANGE Comum:
class Contador:
    def __init__(self, menor, maior):
        self.menor = menor
        self.maior = maior

    #Função que transforma a função anterior em um Iteravel:
    def __iter__(self):
        return self
    #Para que o NEXT dos Print funcione, este trecho aqui é necessário:
    def __next__(self):
        if self.menor < self.maior:
            numero = self.menor
            self.menor = self.menor + 1
            return numero
        raise StopIteration

#Aqui a Função dentro da classe recebeu 2 Parametros:
con = Contador(1,6)

#Aqui Escolho qual imprimir ->Parametro um ou Dois:
#print(con.maior)

'''
it = iter(con)

print(next(con))
print(next(con))
'''

for N in Contador(1,20):
    print(N,end=',')

#Seria o Mesmo Que:
#for I in range(1, 20):
#    print(I)
