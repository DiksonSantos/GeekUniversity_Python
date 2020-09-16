import unittest

from Robo_146 import Robo


class Robo_Testes(unittest.TestCase):

    def setUp(self):
        """Tudo o que estiver no setUp tem prioridade de ser executado antes
        de todos os outros trechos de código."""
        self.megaman = Robo('Mega Man', bateria=50)#Podemos fazer acesso a este objeto a partir de todas as DEFs a baixo.
        print("SetUp sendo executado...")

    def test_carregar(self):
        self.megaman.carregar()
        self.assertEqual(self.megaman.bateria, 100) #O DEF Carrega do arquivo principal tem que ser = 100 tbm.


    def test_dizer_nome(self):
        megaman = Robo('Mega Man', bateria=50)
        self.assertEqual(self.megaman.dizer_nome(), 'Beep Bateria eu sou MEGA MAN')
        #self.assertEqual(megaman.bateria, 49, 'A Bateria Deveria estar em 49%')

    def tearDown(self):
        """Tudo o que estiver nos testes tipo tearDown será execurado no final
        dos testes todos."""
        print("tearDown() sendo Executado...")

if __name__ == '__main__':
    unittest.main()
