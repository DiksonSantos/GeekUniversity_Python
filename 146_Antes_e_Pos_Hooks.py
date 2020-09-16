"""
Unittest:

hooks -> São testes em si. Ou seja, aexecução dos testes.

setup() -> é executado antes de cada metodo de teste, é util para criarmos instancias
de objetos e outros dados.

tearDown() -> é executado ao final de cada método de teste. É útil para excluir dados
ou fechar conexões com bancos de dados.
"""

import unittest

class ModuloTest(unittest.TestCase):

    def detUp(self):
        # Conf do SetUp
        pass

    def test_primeiro(self):
        # setup Vai rodar antes do test
        #TearDown() vai rodar após o teste.
        pass

    def test_segundo(self):
        # setup Vai rodar antes do test
        #TearDown() vai rodar após o teste.
        pass

    def tear_Down(self):
        # Configurações do tearDown()
        pass

    
