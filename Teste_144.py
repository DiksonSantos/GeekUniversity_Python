import unittest
from Atividade_144 import comer, dormir, eh_funny
#from Atividade_144 import comer, dormir, eh_funny        #Tambem funciona desta maneira.

#não coloquei a palavra inicial 'test' no começo, deu pau.
class ATividadesTeste(unittest.TestCase):


#Aqui Conta Como DOIS  DEFs/testes:
    def test_comer(self):
        self.assertEqual(
            comer('quiabo', True),
            'Estou comendo quiabo porque quero manter a forma.'
        )


    def test_fast_food(self):
        """Testando se ta iguarzinho"""
        self.assertEqual(
            comer(comida='pizza', saudavel=False),
            'Estou comendo pizza porque Só se vive uma vez'
        )

    def test_dormindo_pouco(self):
        """Testando testando 123"""
        self.assertEqual(
            dormir(4),
            'Continuo Cansado Apos dormir por apenas 4 horas'
        )

    def test_dormir_muito(self):
        """E ae, funciona ou não ... ?"""
        self.assertEqual(
            dormir(horas=10),
            f'Fico Mau Dormindo {10} Um tanto desses'
        )
# AULA 145 A PARTIR DAQUI:

    def test_funny(self):
        '''Engraçado'''
        #self.assertEqual(eh_funny('Pualinho_Gogo'), False)
        self.assertFalse(eh_funny('Paulinho_Gogo')) #Se Usar 'None' invés da String, tbm funciona.
        #Caso o que estiver nos primeiros parenteses seja Falso, É sxibida a mensagem "Deveria..."
        self.assertTrue(eh_funny('Jim Carey'), 'Deveria Ser Engraçado.')



if __name__ == '__main__':
    unittest.main()
