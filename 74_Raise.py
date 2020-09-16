'''
Levantando os proprios erros com Raise:

OBS: Nã é uma função, mas sim uma palavra reservada.

'''

#raise ValueError('Valor Incorreto')

def colorir(texto, cor):
    colours = ('Azul','Cinza','Verde Claro','Branco')
    if type(texto) is not str:
        raise TypeError('Texto Precisa Ser String')
    if type(cor) is not str:
        raise TypeError('Cor Precisa Ser String')
    if cor not in colours:
        raise ValueError(f'A cor Precisa Ser Uma Entre {colours}')
    print(f'O texto {texto} será impresso na cor {cor}')

x = colorir('String', 'Preto')


