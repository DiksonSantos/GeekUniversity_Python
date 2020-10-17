
#Função que retorna valor inteiro:

def dobro(valor: int) -> int:
    return valor * 2

#Gera um erro no mypy nome_arquivo.py
#x = dobro("Gow")
#print(x)


from typing import Literal

#                              Retorna    Este      ou   Este Valor
def pegar_status(usuario: str) -> Literal['conectado', 'desconectado']:
    pass

