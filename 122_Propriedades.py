"""
class Conta:

    contador = 0

    def __init__(self, titular, saldo, limite):
        self.__Numero = Conta.contador
        self.__Titular = titular
        self.__Saldo = saldo
        self.__Limite = limite
        Conta.contador += 1

    def extrato(self):
        return f'Saldo de {self.__Saldo} do Cliente {self.__Titular}'

    def depositar(self, valor):
        self.__Saldo += valor

    def sacar(self, valor):
        self.__Saldo -= valor

    def transfere(self, valor, destino):
        self.__Saldo -= valor
        self.__Saldo += valor
        destino.__Saldo += valor

    def get_numero(self):
        return self.__Numero

    def get_titular(self):
        return self.__Titular

    def set_titular(self, titular):
        self.__Titular = titular

    def get_saldo(self):
        return self.__Saldo

    def get_limite(self):
        return self.__Limite

    def set_limite(self, limite):
        self.__Limite = limite


Conta1 = Conta("Dikson", 80.000, 5.000)
Conta2 = Conta("Samantha_Puta", 20.000, 3.000)

print(Conta1.extrato())
print(Conta2.extrato())

#Conta.transfere(Conta1)

#Na linha a baixo esta uma possibilidade de acessar elementos Privados __ da Classe:
#... Porém é errado.
#Saldos = Conta1._Conta__Saldo + Conta2._Conta__Saldo    # Ponto UM Dunder & DOIS Dunder
#print(Saldos)


#AGORA USANDO O MÉTODO Oficial -> 'GET' :
Nova_Soma = Conta1.get_saldo() + Conta2.get_saldo()
print('Soma dos Dois Saldos Juntos (Duas contas): ',Nova_Soma)

Conta1.transfere(80, Conta2)

#print(Conta2.__dict__ )



Conta2.set_titular("Luciene") #Alterou o Nome da dona da conta.
#print(print(Conta2.__dict__ ))

print('Novo Saldo', Conta2.get_saldo())
print('Novo Saldo COnta1: ', Conta1.get_saldo())

"""

"""
class Conta:

    contador = 0

    def __init__(self, titular, saldo, limite):
        self.__Numero = Conta.contador
        self.__Titular = titular
        self.__Saldo = saldo
        self.__Limite = limite
        Conta.contador += 1

    def extrato(self):
        return f'Saldo de {self.__Saldo} do Cliente {self.__Titular}'

    def depositar(self, valor):
        self.__Saldo += valor

    def sacar(self, valor):
        self.__Saldo -= valor

    def transfere(self, valor, destino):
        self.__Saldo -= valor
        destino.__Saldo += valor

    def get_numero(self):
        return self.__Numero

    def get_titular(self):
        return self.__Titular

    def set_titular(self, titular):
        self.__Titular = titular

    def get_saldo(self):
        return self.__Saldo

    def get_limite(self):
        return self.__Limite

    def set_limite(self, limite):
        self.__Limite = limite


Conta1 = Conta("Dikson", 80.000, 5.000)
Conta2 = Conta("Samantha_Puta", 20.000, 3.000)
print('Saldo Cont1:', Conta1.get_saldo())
print('Saldo Cont2:', Conta2.get_saldo())
Conta2.set_titular("Luciene")

Conta1.transfere(80, Conta2)
print('Novo Saldo Cont1: ', Conta1.get_saldo())
print("Novo Saldo Cont2: ", Conta2.get_saldo())
"""


class Conta:

    contador = 0

    def __init__(self, titular, saldo, limite):
        self.__Numero = Conta.contador
        self.__Titular = titular
        self.__Saldo = saldo
        self.__Limite = limite
        Conta.contador += 1

    @property
    def valor_total(self):
        return self.__Saldo + self.__Limite


    @property
    def numero(self):
        return self.__Numero

    @property
    def titular(self):
        return self.__Titular

    @property
    def saldo(self):
        return self.__Saldo

    @property #ISSO AQUI É UM 'GETTER'
    def limite(self):
        return self.__Limite

    @limite.setter #ISSO AQUI É UM 'SETTER'
    def limite(self, novo_limite):
        self.__Limite = novo_limite

    def extrato(self):
        return f'Saldo de {self.__Saldo} do Cliente {self.__Titular}'

    def depositar(self, valor):
        self.__Saldo += valor

    def sacar(self, valor):
        self.__Saldo -= valor

    def transfere(self, valor, destino):
        self.__Saldo -= valor
        destino.__Saldo += valor



Conta1 = Conta("Dikson", 80.000, 5.000)
Conta2 = Conta("Samantha_Puta", 20.000, 3.000)

print("Ct1 Saldo: ", Conta1.saldo)
print("Ct2 Saldo: ", Conta2.saldo)


Conta1.transfere(75, Conta2)
print('Novo Saldo C1: ', Conta1.saldo)
print('Novo Saldo C2: ', Conta2.saldo)
print("Ct1 Limite:", Conta1.limite)
Conta1.limite += 30.000  #  += ele adiciona -> 30+5   |  = -> 30 Só = ele sobreescreve
print("Ct1 Novo Limite: ", Conta1.limite)

# Repare que NÃO  tem () no final de total. Isto é uma propriedade e não uma função
print(f"Valor total Conta1 = Saldo{Conta1.saldo} Limite{Conta1.limite} = ", Conta1.valor_total)

print(f"Valor total Conta2 = conta Saldo{Conta2.saldo} Limite{Conta2.limite}= ", Conta2.valor_total)
