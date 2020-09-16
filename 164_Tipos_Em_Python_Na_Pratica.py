"""
#Declarando Os Tipos de Variaveis:

nomes: list = ["Gow", "Dikson"]

TUPLA: tuple = (3, 5, 7)

Valores: set = {3, 5, 5}

Options: dict = {"Air": True, "Blue_Bean": False, "Truth": False}

print(nomes, "\n", TUPLA, "\n", Valores, "\n", Options)
"""

"""
#A CIMA ESPECIFICAMOS OS TIPOS DE VARIAVEIS, AGORA PODEMOS TAMBÉM DEFINIR QUE TIPO DE
#..ITENS ESTARÃO DENTRO DESSAS VARIAVEIS:

from typing import Dict, List, Tuple, Set

nomes:  List[str] = ['Gow', 'Dikson']

versions: Tuple[int, int, int] = (2, 3, 4)

Options: Dict[str, bool] = {'ar': True, 'Banco_De_Ouro': True}


print(nomes, "\n", versions, "\n", Options)
print(__annotations__) #Mostra Todas as informações no que diz respeito aos tipos de Itens e os Tipos de Suas Variaveis.
"""

import random

NAIPES = '♠ ♡ ♢ ♣'.split()
# https://www.alt-codes.net/suit-cards.php
CARTAS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()


def criar_Baralho(aleatorio=False):
    """Cria Baralho com 52 Cartas"""
    Baralho = [(n, c) for c in CARTAS for n in NAIPES]
    if aleatorio:
        random.shuffle(Baralho)
    return Baralho


#print(criar_Baralho())

"""
Baralho = [(n, c) for c in CARTAS for n in NAIPES]
print(Baralho)
#EX: Combina todos os Simbolos com 2, deposi todos 3 com todos, e assim por diante.

X = list(zip(NAIPES, CARTAS))
print(X)
#Aqui ele Combina o primeiro Simbol com o Primeiro Numero, Segundo Simbolo c/ Segundo Numero Etc.. 
#..Quando acaba os Simbolos ele Para de combinar. ->[('♠', '2'), ('♡', '3'), ('♢', '4'), ('♣', '5')]
"""

def distribuir_Cartas(Baralho):
    """Gerencia a Mão de Cartas de Acordo Com o Baralho Gerado"""
    return (Baralho[0::4], Baralho[1::4], Baralho[2::4], Baralho[3::4])

#baralho = criar_Baralho()
#print(distribuir_Cartas(baralho))

def jogo():
    """Inicia Um Jogo Par 4 Jogadores"""
    cartas = criar_Baralho(aleatorio=True)
    jogadores = 'P1 P2 P3 P4'.split()
    # 'j' é Chave 'm' É valor -> Representando Jogadores e distr.. dentro de ZIP
    maos = {j: m for j, m in zip(jogadores, distribuir_Cartas(cartas))}

    for jogador, cartas, in maos.items():
        carta = ' '.join(f"{j}{c}" for (j, c) in cartas)
        print(f"{jogador}: {carta}")

if __name__ == '__main__':
    jogo()
