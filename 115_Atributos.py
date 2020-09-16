'''
Atributos -> São os estados de Um Objeto

Existem 3 Tipos de Atributos:
    Atrib de Instancia
    De classe
    Dinamico

Metodo Construtor -> Constroi Objetos (???)

'''
'''
class Lampadinhas:
    def __init__(self, voltagem, cor):
        self.__voltagem = voltagem
        self.__cor = cor
        self.__ligada = False

    @property
    def voltagem(self):
        return self.__voltagem

    @property
    def cor(self):
        return self.__cor

    @property
    def ligada(self):
        return self.__ligada

'''


# Classes com Atributos de instancia Publicos (Ou seja SEM o __ antes)
class Lampadas:

    def __init__(self, voltagem, cor):
        self.voltagem = voltagem
        self.cor = cor
        self.ligada = False


class ContaCorrente:

    def __init__(self, numero, limite, saldo):
        self.Numero = numero
        self.Limite = limite
        self.Saldo = saldo


class Produto:
    # Atributo de CLasse
    imposto = 1.05  # Ou 0,05% de Imposto.
    Contador = 0

    def __init__(self, nome, descricao, valor):
        self.id = Produto.Contador + 1  # Esta contando Cada Objeto que usar esta classe.
        self.Nome = nome
        self.Descricao = descricao
        self.Valor = (valor * Produto.imposto)
        # A cada vez/Linha que esta DEF desta classe é usada a Variavel da linha de baixo recebe 1.
        Produto.Contador = self.id  # Aqui ele confere o valor da variavel id, Se outro produto for criado ela valerá 2


class Usuario:

    def __init__(self, nome, email, senha):
        self.Nome = nome
        self.Email = email
        self.Senha = senha


# Classes de Atributos de instancia Privados (Ou seja COM o __ antes)
class Acesso:

    def __init__(self, email, senha):  # Pode ser SELF ou qualquer outra palavra no ninicio (Usei Proprio)
        self.__email = email  # Este atributo com __ quer dizer que é PRIVADO...Ou seja, só podem ser acessados por Um Objeto Criado FORA da função
        self.senha = senha

    def mostra_e_mail(self):
        return self.__email  # Tentei com o PRINT , mas ele cria uma ultima linha e mostra NONE

    def Printa_email(self):
        print(
            self.__email)  # Para não aparecer NONE no final, não printe La fora Use-> "user.Printa_email()" #Apenas Isto


# ATRIBUTOS DE INFANCIA:
# EX:    __ == Interno
user = Acesso('Gmail.com', '123456')
# print(user.email) #Não da pra usar
# print(user.senha) # Aqui Vai Tudo Bem. (SEM o __ )

USU = Usuario('Dikson', 'Gmail', 123)
# print(USU.Nome) #Aqui como Na Função esta sem o __ Ele aceita que seja usado Aqui fora.

# PARA CONSEGUIR ACESSO AOS ATRIBUTOS QUE TEM __

# print(user.mostra_e_mail()) #Assim ele acessa os dados privados por __
# user.Printa_email() #Apenas Isto

# Continua em 44:30Min:
# https://www.udemy.com/course/curso-de-programacao-em-python-do-basico-ao-avancado/learn/lecture/11893058?start=0#content

User1 = Acesso('Gow@Hotmail.com', 123)
User2 = Acesso('Santos@gmail', 564)

# User1.Printa_email()
# User2.Printa_email()


# ATRIBUTOS DE CLASSE:
# Pro1 = Produto("VideoGame", "Console", 30)
# Pro2 = Produto('Computador', 'DeskTop', 200)
# Produto3 = Produto('NoteBook', 'Portable', 2.300)

'''
Atributos são declarados diretamente na classe, OU fora do Construtor:

'''
# print("Preço Com Imposto: ",Pro1.Valor)
# print("Preço Com Imposto: ",Pro2.Valor)

# Fazendo acesso a um valor de um atributo de Classe:
# print(Produto.imposto)

# print(Pro1.id)# Aqui foram contados a criação de UM produto ou Objeto.
# print(Pro2.id) #Aqui Como foi criado Um segundo Item\Objeto, ele Conta\Marca 2
# print(Produto3.id)# 3 produtos Contados.


# ATRIBUTOS DINAMICOS:
# Atributo dinamico é exclusivo da instancia que o criou.

p1 = Produto('Computador', 'DeskTop', 2.000)
p2 = Produto('NoteBook', 'Portable', 2.300)

# Criando Um Atrib dinamico em tempo de execução. Ou Seja Só existe AQUI e Só Para p2
p2.peso = "5KGs"  # Exclusivo de p2.

# p1 Da Pau
# print(f'Produto: {p1.Nome}, Descrição: {p1.Descricao}, Valor {p1.Valor}, Peso {p1.peso}KG')

print(f'Produto: {p2.Nome}, Descrição: {p2.Descricao}, Valor {p2.Valor}, Peso {p2.peso}')

# DELETANDO o ATRIBUTOS:
print(p2.__dict__)  # Antes de fazer a Deleção
del p2.peso
# Pode deletar Atributos Que existem na Função TBM
del p2.Descricao
del p2.Nome

# As 3 linhas a baixo mostram todos os elementos de uma classe ou Objeto.
print(p1.__dict__)
# Apos fazer a deleção.
print(p2.__dict__)  # Restou apenas o Valor
# print(Produto.__dict__) #Mostra tudo da DEF.
