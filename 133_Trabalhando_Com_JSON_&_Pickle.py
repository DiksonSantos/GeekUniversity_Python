"""
JSON -> Java Script Object Notation

API -> São metodos de comunicação entre os serviços oferecidos por
 empresas

"""
"""
import json
#Converteu a Lista que possui um Dict Para JSON
ret = json.dumps(['produto', {'Play-4': ('2TB', 'Novo', '220V', 2340)}])
print(ret)
"""

"""
#import json
import jsonpickle

class Gato:

    def __init__(self, nome, raca):
        self.__Nome = nome
        self.__Raca = raca

    @property
    def nome(self):
        return self.__Nome

    @property
    def Raca(self):
        return self.__Raca


#Transformando Um Objeto Python num arquivo JSON:
Felix = Gato('Felix', 'Egipcio')
ret = jsonpickle.encode(Felix)
print(ret)
"""




'''
print("Não Convert. P/ JSON: ", Felix.__dict__)
ret = json.dumps(Felix.__dict__)
print("Convertido Para JSON: ", ret)
'''

"""
Existe Uma forma de Integrar JSON com o Pickle:
Precisa Instalar:
Vá ao terminal daqui do Pycharm mesmo e digite:

pip install jsonpickle 

Só isso.

"""


#REFATORANDO O CODIGO:
import jsonpickle

class Gato:

    def __init__(self, nome, raca):
        self.__Nome = nome
        self.__Raca = raca

    @property
    def Nome(self): #É desta linha (.Nome) que usamos para ver as informações contidas em .__Nome
        return self.__Nome

    @property
    def Raca(self):
        return self.__Raca

"""
#-> Transformando/Escrevendo Um Objeto Python em um (num) JSON:
#Objeto Felix:
Felix_Objeto = Gato('Felix', 'Egipcio')

#Cria o Felix.json , Objeto_Arquivo
with open('Felix.json', 'w') as Arquivo:
    #Codificar o Objeto Felix em JSON_Pickle
    Resp = jsonpickle.encode(Felix_Objeto)
    #E Finalmente o Arquivo 'Felix.json' recebe o conteudo do Objeto Felix
    Arquivo.write(Resp)
"""
with open('Felix.json', 'r') as Arquivo:
    Contents = Arquivo.read()
    #Decodifica com Decode:
    Ler = jsonpickle.decode(Contents)
    print(Ler)
    print(type(Ler))
    print(Ler.nome)
    print(Ler.Raca)
