"""
class Clientes:
    def __init__(self, nome, sobrenome, cpf, renda):
        self.__Nome = nome
        self.__Sobrenome = sobrenome
        self.__CPF = cpf
        self.__Renda = renda

    def nome_completo(self):
        return f'{self.__Nome}, {self.__Sobrenome}'




class  Funcionario:
    def __init__(self, nome, sobrenome, cpf, matricula):
        self.__Nome = nome
        self.__Sobrenome = sobrenome
        self.__CPF = cpf
        self.Matricula = matricula

    def nome_completo(self):
        return f'{self.__Nome}, {self.__Sobrenome}'


Cliente1 = Clientes('Dronelles', 'Del Valle', 346, 5.000)
Fun = Funcionario('Abenildo', 'Botelho', 6666, 1965)

print(Cliente1.nome_completo())
print(Fun.nome_completo())
"""


"""
class Pessoa:

    def __init__(self, nome, sobrenome, cpf):
        self.__Nome = nome
        self.__Sobrenome = sobrenome
        self.__CPF = cpf

    def nome_completo(self):
        return f'{self.__Nome}, {self.__Sobrenome}'


class Clientes(Pessoa):
    #Cliente Herda os Outros Atributos da Classe 'Pessoa' 
    def __init__(self, nome, sobrenome, cpf, renda):
        super().__init__(nome, sobrenome, cpf)#SUPER É A CLASSE 'PESSOA', E NELA TEMOS ESTES 3 ATRIBUTOS.
        self.__Renda = renda


class Funcionario(Pessoa): #Funcionario Herda de Pessoa
    def __init__(self, nome, sobrenome, cpf, matricula):
        Pessoa.__init__(self, nome, sobrenome, cpf) # Aqui troquei o INIT por pessoa, mas da no mesmo.
        self.Matricula = matricula



Cliente1 = Clientes('Dronelles', 'Del Valle', 346, 5.000)
Fun = Funcionario('Abenildo', 'Botelho', 6666, 1965)


#print(Cliente1.nome_completo())
#print(Fun.nome_completo())


print(Cliente1.__dict__)
print(Fun.__dict__)

"""
class Pessoa:

    def __init__(self, nome, sobrenome, cpf):
        self.__Nome = nome
        self.__Sobrenome = sobrenome
        self.__CPF = cpf

    def nome_completo(self):
        return f'{self.__Nome}, {self.__Sobrenome}'


class Clientes(Pessoa):
    """Cliente Herda os Outros Atributos da Classe 'Pessoa' """
    def __init__(self, nome, sobrenome, cpf, renda):
        super().__init__(nome, sobrenome, cpf)#SUPER É A CLASSE 'PESSOA', E NELA TEMOS ESTES 3 ATRIBUTOS.
        self.__Renda = renda


class Funcionario(Pessoa): #Funcionario Herda de Pessoa
    def __init__(self, nome, sobrenome, cpf, matricula):
        Pessoa.__init__(self, nome, sobrenome, cpf) # Aqui troquei o INIT por pessoa, mas da no mesmo.
        self.__Matricula = matricula

    def nome_completo(self):
        print(self._Pessoa__CPF) #Self PONTO + UM Dunder + 2 Dunders + Atrib
        return f'Identificação Funcionario: {self.__Matricula} Nome: {self._Pessoa__Nome}'



Cliente1 = Clientes('Dronelles', 'Del Valle', 346, 5.000)
Fun = Funcionario('Abenildo', 'Botelho', 6666, 8965)

print(Cliente1.nome_completo()) #Metodo 'Nome-Completo' Original
print(Fun.nome_completo()) #Metodo Nome_Completo Re-escrito.



