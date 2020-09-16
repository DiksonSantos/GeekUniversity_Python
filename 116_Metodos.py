# Métodos São Funções -> Representam o Comportamento do Onjeto, Ou as ações que este pode realizar no Software\Sistema.

# Existem metodos de Instancia e Metodos de Classes.

'''
#Retirado da Classe Usuario:
def __correr__(self, metros):
        print(f'{self.__Nome} Esta correndo Metros {metros} Metros')


'''
'''
#ISSO TUDO AQUI ESTAVA A BAIXO DA CLASSE USUARIO:

Prod = Produto('VideoGame', 'Console', 2000)
#Imprime - Classe - instancia - Objeto - Porcentagem
print(Produto.desconto(Prod, 50))
print(int(Prod.desconto(10))) #Com Desconto de 10%
'''
'''
# User1 = Usuario('Dikson', 'Santos', 'Dikson_Santos@gmail', 456)
# User2 = Usuario('Gow', 'Santos', 'GowDikson@Hotmail.com', 987)
# print(User1.nome_completo(), '\n', User2.nome_completo())
# Continua em 30Min

nome = input("Informe Nome: ")
sobrenome = input("Informe Sobrenome: ")
email = input("E-mail: ")
senha = input("Digite a Senha: ")
confirma = input("COnfirmação de Senha: ")

if senha == confirma:
    user = Usuario(nome, sobrenome, email, senha)
else:
    print('Senha Incorreta')
    exit(1)
print("User Created With Success")

if user.checa_senha(senha):
    print('Access Allowed')
else:
    print("Access Denied")
print(f'Senha User Criptografada: {Usuario.mostra_senha(user)}')  # Acesso Correto FUNCIONA!

# CONTINUA EM 50 Min
'''

class Lampada:

    def __init__(self, Cor, Voltagem,
                 Luminosidade):  # __init__ é o Construtor -> Para Criarmos um Objeto precisamos de um Construtor.
        self.__cor = Cor
        self.__voltagem = Voltagem
        self.__luminosidade = Luminosidade
        self.__Ligada = False


class Cont_Corrent:
    Contador = 4999

    def __init__(self, numero, limite, saldo):
        self.__Numero = Cont_Corrent.Contador + 1
        self.__Limite = limite
        self.__Saldo = saldo
        Cont_Corrent.Contador = self.__Numero


class Produto:
    Cont = 0

    def __init__(self, nome, describe, valor):
        self.__Nome = nome
        self.__id = Produto.Cont + 1
        self.__Describe = describe
        self.__Valor = valor
        Produto.Cont = self.__id

    def desconto(self, porcentagem):
        '''Da o valor do produto com Desconto'''
        return (self.__Valor * (100 - porcentagem)) / 100


from passlib.hash import django_pbkdf2_sha256 as CRIP


class Usuario:

    contador = 0

    @classmethod
    def conta_usuarios(cls): # cls -> Este parametro é a propria classe Usuario
        '''Função que imprime UMA linha de UMA função de dentro de qualquer lugar da classe Usuario'''
        print(f'Temos {cls.contador} Usuario(s) no sistema')


    @staticmethod
    def definicao():
        return "UFHGDS"


    def __init__(self, nome, sobrenome, email, key):
        self.__id = Usuario.contador = 1
        self.__Nome = nome
        self.__Sobrenome = sobrenome
        self.__Email = email
        self.__Key = CRIP.hash(key, rounds=200000, salt_size=16)
        Usuario.contador = self.__id

    @classmethod
    def ver(cls):
        ''''''
        print('Teste')
        print(cls.mostra_senha(Usu))



    def mostra_senha(self):
        return self.__Key

    def __correr__(self, metros):
        print(f'{self.__Nome} Esta correndo Metros {metros} Metros')

    def nome_completo(self):
        return f'{self.__Nome} {self.__Sobrenome}'

    def checa_senha(self, senha):
        if CRIP.verify(senha, self.__Key):
            return True
        return False

    def gera_Usuario(self):
        return self.__Email.split("@")[1] #Retorna só o que vem depois de @ no E-mail\argumento do Usuario\Objeto.


Usu = Usuario('Gow', 'Dikson', 'Dikson@gmail.com', "1234")
#Classe.Metodo()
#Usuario.conta_usuarios() #Forma correta

print(Usu.gera_Usuario())

#Objeto.Metodo()
#Usu.conta_usuarios() #Possivel, Mas não recomendado.

#Usu.ver() #Imprime a frase 'Teste' E A senha Criptografada.

#METODO ESTATICO:
'''
print(Usuario.contador)

print(Usuario.definicao())

Usu = Usuario("Dik", "Sant", "@", '123')

print(Usu.contador)

print(Usu.definicao())

Usu.gera_Usuario()
'''
