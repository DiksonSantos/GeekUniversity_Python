#print(print.__doc__)

#print(__doc__)

def oi():
    '''Funcção que só diz Oi'''
    print("Oi")

print(oi.__doc__) #Apresenta a linha das apaspas ou a explicação da função.

#help(oi())

def maisUma(par1, par2):
    ''' #Digitei as 3 aspas e dei enter ele já monta uma estrutura para eu explicar o que tudo faz.

    :param parametro 1:
    :param par2:
    :return:
    '''
    prime = par1
    sec = par2
    junta = prime+sec
    return junta

fulano = maisUma('Eu Sou ', 'A Luz das Estrelas')
print(fulano)
