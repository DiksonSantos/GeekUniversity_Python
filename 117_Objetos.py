'''
Objetos São Instancias da Classe

'''

class Lampadas:

    def __init__(self, cor, voltagem, luminosidade):
        self.__Cor = cor
        self.__Volt = voltagem
        self.__Luminosidade = luminosidade
        self.__Ligada = False

    def checa_lampada(self):
        return self.__Ligada

    def liga_desliga(self):
        if self.__Ligada:
            self.__Ligada = False
        else:
            self.__Ligada = True


class COntCorrent:

    contador = 4999

    def __init__(self, limite, saldo):
        self.__Numero = COntCorrent.contador + 1
        self.__Limite = limite
        self.__Saldo = saldo
        COntCorrent.contador = self.__Numero


class Usuario:

    def __init__(self, nome, sobrenome, email, senha):
        self.__Nome = nome
        self.__Sobrenome = sobrenome
        self.__Email = email
        self.__Senha = senha

    def MostraTudo(self):
        '''Se Não tiver esta Função ele só mostra o Endereço de Memoria'''
        return self.__Nome, self.__Sobrenome, self.__Email, self.__Senha


#Instancias OU Objetos
lampiao = Lampadas('Branca', 11, 60)
#False OU Desligada
print(f'A lampada Esta Ligada? {lampiao.checa_lampada()}')

lampiao.liga_desliga() #ESTE MÉTODO LIGA A LAMPADA:
print(f'A lampada Esta Ligada? {lampiao.checa_lampada()}') #TRUE.

cc1 = COntCorrent(500, 2000)

Usu = Usuario('Gow', 'Rodrigues', 'Gow@email.com', 90897)
print(Usu.MostraTudo())

Nome = 'Dikson'
Sobre_Nome = 'Santos'
E_mail = 'Dikson@hotmail.com'
Keys = 12345

Usu1 = Usuario(nome=Nome, sobrenome=Sobre_Nome, email=E_mail, senha=Keys)
print(Usu1.MostraTudo())

#Usu1 = Usuario(Nome, Sobre_Nome, E_mail, Keys)
#print(Usu1.MostraTudo())
