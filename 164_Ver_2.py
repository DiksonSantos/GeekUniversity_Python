
import random
from typing import List, Tuple, Dict

NAIPES = '♠ ♡ ♢ ♣'.split()
#https://www.alt-codes.net/suit-cards.php
CARTAS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

CARTA = Tuple[str, str]
BARALHO = List[CARTA]


def criar_Baralho(aleatorio: bool = False) -> BARALHO:
    """Cria Baralho com 52 Cartas"""
    Baralho: BARALHO = [(n, c) for c in CARTAS for n in NAIPES]
    if aleatorio:
        random.shuffle(Baralho)
    return Baralho

def distribuir_Cartas(Baralho: BARALHO) -> Tuple[BARALHO, BARALHO, BARALHO, BARALHO]:
    """Gerencia a Mão de Cartas de Acordo Com o Baralho Gerado"""
    return (Baralho[0::4], Baralho[1::4], Baralho[2::4], Baralho[3::4])


def jogo() -> None:
    """Inicia Um Jogo Par 4 Jogadores"""
    cartas: BARALHO = criar_Baralho(aleatorio=True)
    jogadores: List[str] = 'P1 P2 P3 P4'.split()
    # 'j' é Chave 'm' É valor -> Representando Jogadores e distr.. dentro de ZIP
    maos: Dict[str, BARALHO] = {j: m for j, m in zip(jogadores, distribuir_Cartas(cartas))}

    for jogador, cartas, in maos.items():
        carta: str = ' '.join(f"{j}{c}" for (j, c) in cartas)
        print(f"{jogador}: {carta}")

if __name__ == '__main__':
    jogo()
