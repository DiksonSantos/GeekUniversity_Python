#Função em python
def func(x):
    return 3 * x + 1


#print(func(4),' Função')


#Expressão lambda
calc = lambda x: 3 * x + 1

#print(calc(4),' Lambda')


#Expreeões LAMBAS podem ter multilas entradas tbm:

nome_completo = lambda nome, sobrenome: nome.strip().title() + ' ' + sobrenome.strip().title()

#print(nome_completo(' gow', ' dikson'),nome_completo(' RODRIGUES doS', ' SANTos'))
#print(nome_completo(' RODRIGUES', ' SANTos'))

'''
nomes = 'gow dikson'
nomes.lstrip()
#print(nomes)

amar = lambda: 'How not to love Python?'
print(amar())

umha = lambda x:3 * x + 1
print(umha(6))

duas = lambda x, y: (x*y) ** 0.5
print(duas(5,7))

tres = lambda x,y,z: 3 / (1/x+1/y+1/z)
print(tres(3,6,9))
'''

#Outro exemplo:

autores = ['Paulinho Gogo', 'Matheus ceará', 'Ludmila Layer Landstomr', 'Xiquinho Micharia', 'Pedrinho Tonelada',
           'Zé da Cachirolla', 'Fagundes chifrão Rauff', 'Macalé oliveira', 'João Mimero','SR Izac']

#Ordena por ordem alfabetica os Sobrenomes
autores.sort(key=lambda sobrenome: sobrenome.split(' ')[-1].lower())

#print(autores)

'''
#Teste:
nome = 'gow dikson rodrigues dos santos'

print(nome.title().split(' ')[0:3]) #O separador TEM QUE TER um espaço em branco

print(nome.title().split(' ')[-1])# Trouxe só o 'santos'
'''

# Função quadratica:
#f(x) = a * x ** 2 + b * x + c

def fun_quad(a,b,c):
    '''Retorna a Função F(x) = a.x**2 + b *x + c'''
    return lambda x: a * x **2 + b * x + c

# Teste com valores de A B C Respectivamente
teste = fun_quad(2, 3, -5)

#Aqui temos que passar o valor de X da Função Neste caso F(0)  Ou F de Zero:
print(teste(0))

#F de 1:
print(teste(1))

#F(2):
print(teste(2))
print('\n')
#Informando todos os valores Numa Unica Linha:
print(fun_quad(3,0,1)(2)) #A B C  e o valor de X



#É até mais facil que os DEFs ...
soma = lambda Soma, Elemento: Soma + Elemento

testando = soma(2,2)
print(testando)

print(soma(4,4)) #Numa unica linha.
