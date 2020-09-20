valor = '67.9'
#print(float(valor))

valor2 = '3'
#print(int(valor2))

valor3 = 23.98
#print(str(valor3))
#____________________________________________________________________________

def cumprimenta(um, dois,/):
    return f"{um}, {dois}"

#Não Permitido:
#cumprimenta(dois='Sobrenome', um='Nome')


#Permitido:
#print(cumprimenta('Dikson', 'Santos'))
'''
A / Faz com que todos os parametros sejam posicionais, ou seja: Você não pode 
nomea-los alterando a sequencia deles (dos parametros)
'''



#AGORA UMA FORMA DE OBRIGAR A NOMEAR OS PARAMETROS:

def cumprimenta2(*,sobrenome, nome):
    return f"{nome}, {sobrenome}"


#print(cumprimenta2(nome='Dikson', sobrenome='Santos'))

#Não Roda, Pois precisa que informem Quem é Quem nos argumentos:
#print(cumprimenta2('Dikson', 'Santos'))


#Misturando as Tecnicas:
def cumprimenta3(nome, /, mensagem='Ola', *, nada):
    return nome + mensagem + nada

x = cumprimenta3('Gow ', nada='')
j = cumprimenta3('Gow ', 'Dikson', nada='')
print(x)
print(j)

#FICA OBRIGATORIO INFORMAR QUEM VAI SER O ARGUMENTO 'nada' .

# /  -> Tudo antes da / Não Pode informar quem é quem.
# *  -> Fica obrigatorio informar quem é quem APOS o *   .
