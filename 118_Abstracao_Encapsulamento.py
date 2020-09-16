
'''
class Conta:

    contador = 400

    def __init__(self, titular, saldo, limite):
        self.Numero = Conta.contador
        self.Titular = titular
        self.Saldo = saldo
        self.Limite = limite
        Conta.contador += 1

    def extrato(self):
        print(f"Seu saldo é de {self.Saldo:.3f}R$.\nTitular: {self.Titular}\n"
            f"Com Limite de {self.Limite:.3f}R$")

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        self.Saldo = valor

Cont1 = Conta('Dikson', 40.000, 5.000)
print(Cont1.Titular)
print(Cont1.Saldo)
print(Cont1.Limite)
print(Cont1.Numero)
print(Cont1.extrato())
'''

"""
Quando Não Usamos o __ nos atributos da classe, Isso permite que eles
não apenas sejam lidos como também alterados Como no exemplo a Baixo:



Cont1.Numero = 500
Cont1.Titular = 'Little Wonder'
Cont1.Saldo = 25

print(Cont1.__dict__)
"""

#Re-Fatorando a Classe Toda:
#Ou, tornando todos os Atributos Privados:
class Conta:

    contador = 400

    def __init__(self, titular, saldo, limite):
        self.__Numero = Conta.contador
        self.__Titular = titular
        self.__Saldo = saldo
        self.__Limite = limite
        Conta.contador += 1

    def extrato(self):
        print(f"Seu saldo é de {self.__Saldo:.3f}R$.\nTitular: {self.__Titular}\n"
            f"Com Limite de {self.__Limite:.3f}R$")

    def depositar(self, valor):
        if valor > 0:
            self.__Saldo += valor
        else:
            print("Valor tem que ser Positivo")

    def sacar(self, valor):
        if valor > 0:
            if self.__Saldo >= valor:
                self.__Saldo -= valor
            else:
                print('Saldo Insuficiente')
        else:
            print("Valor (Saque) Não Pode ser Negativo!")

    def transferir(self, valor, conta_destino):
        """Retira Valor Da Conta de Origem"""
        self.__Saldo -= valor
        self.__Saldo -= 1 #TAXA DE TRANSFERENCIA (Cobrada de quem Realizou a Transferencia)

        """Insere Valor Na Conta Destino"""
        conta_destino.__Saldo += valor


'''
Desta forma o modo de leitura Já não pode mais ser usado 
como fiz antes ali em cima.
'''
Cont1 = Conta('Dikson', 80, 5)
#print(Cont1.__dict__)

Conta2 = Conta('Luciene', 0, 3)

Cont1.transferir(10, Conta2)

Cont1.extrato()
Conta2.extrato()















#print(Cont1._Conta__Titular)

#Porem foi possivel fazer a Mudança de Nome acessando o Atributo desta forma Aqui
#O professor esta meio contraditorio:

#Cont1._Conta__Titular = 'Anger'
#print(Cont1._Conta__Titular)

#Cont1.depositar(5.000) #Depositado 3.000R$ aos 40 Mil que la já estavam.
#print(Cont1.__dict__)

#Cont1.sacar(40.000)
#print(f"Saldo Atual: {Cont1._Conta__Saldo}") #Deduziu o Saldo. = 38 Mil.

#print('\n \n')

'''
#TRANSFERENCIA ENTRE CONTAS:   -> METODO BURRO

Valor_TR = 2.100

Conta2.sacar(Valor_TR)
print('\n')
Cont1.depositar(Valor_TR)

Cont1.extrato()
print("_______")
Conta2.extrato()
'''
