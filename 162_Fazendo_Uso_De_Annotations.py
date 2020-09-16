"""
Aula 162 Annotation:
Annotations são as str depois dos argumentos de entrada das funções.

Formas de Uso:
#Correta:
texto: str

#Incorreta:
texto:str

texto : str

#PARA O TRUE (CORRETO):
alinhamento: bool = True)
__
Forma INCORRETAS Do Return (Depois dos argumentos):
)->str
) ->str
#Correto:
) -> str
"""

import math
                #Parametro Tipo Floar -> Saida Float
def circunferencia(raio: float) -> float:
    return 2 * math.pi * raio


#print(circunferencia.__annotations__)#{'raio': <class 'float'>, 'return': <class 'float'>}

# nome: str = "Gow Dikson"
# peso: float = 85.4
# Prontidao: bool = True
#
# #Tras informações sobre as variaveis globais do Programa:
# print(__annotations__) # {'nome': <class 'str'>, 'peso': <class 'float'>, 'Prontidao': <class 'bool'>}
#______________________


class Pessoa:
                                                          #O Uso do None Não é obrigatorio.
    def __init__(self, nome: str, idade: int, peso: float) -> None:
        self.__Nome = nome
        self.__Idade = idade
        self.__Peso = peso


    def andar(self) -> str:
        return f"{self.__Nome} I walking"

    @property
    def mostra_tudo(self):
        return f"Nome= {self.__Nome}, Idade= {self.__Idade}, Peso= {self.__Peso}"


People = Pessoa(nome="Dikson", idade=34, peso=85)

#print(People.andar())
print(People.mostra_tudo)
print(People.__dict__)

#O Objeto neste caso "People" , Não tem __annotations__  , mas um métpdp dele SIM Ex:
print("Annotation= ", People.andar.__annotations__)
#print("Annotation= ", People.mostra_tudo.__annotations__)  Aqui Deu ruim.
print(People.__init__.__annotations__)
