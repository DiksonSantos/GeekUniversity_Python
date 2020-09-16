class Robo:

    def __init__(self, nome, bateria=100, habilidades=[]):
        self.__nome = nome
        self.__bateria = bateria
        self.__habilidade = habilidades

    @property
    def nome(self):
        return self.__nome

    @property
    def bateria(self):
        return self.__bateria

    @property
    def habilidades(self):
        return self.__habilidade

    def carregar(self):
        self.__bateria = 100

    def dizer_nome(self):
        if self.__bateria > 0:
            self.__bateria -= 1
            return f'Beep Bateria eu sou {self.__nome.upper()}'
        return 'Bateria Fraca. Por favor, recarregue e tente novamente'


    def aprender_habilidade(self, Nova_Habilidade, custo):
        if self.__bateria >= custo:
            self.__bateria -= custo
            self.__habilidade.append(Nova_Habilidade)
            return f"Eu aprendi {Nova_Habilidade.upper()} sou o Mega Man Agora"
        return "Baterua Insuficiente ainda."
