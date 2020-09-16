'''

Metadatas -> Dados de um arquivos, como tamanho e datas de criação e modificação.

Wraps ->

'''

'''
#ORIGINAL:
def ver_log(fun):
    def logar(*args, **kwargs):
        #aQUI TINHA A DOCUMENTAÇÃO TIVE QUE TIRAR
        print(f'Você esta Chamando{fun, __name__}')
        print(f'Aqui a documentação: {fun, __doc__}')
        return fun(*args, **kwargs)
    return logar


@ver_log
def soma(a,b):
    #aQUI Também
    return a+b

#print(help(soma))

'''

from functools import wraps

#SOLUÇÃO:
def ver_log(fun):
    @wraps(fun)
    def logar(*args, **kwargs):
        '''Eu sou uma função dentro de outra'''
        print(f'Você esta Chamando{fun, __name__}')
        print(f'Aqui a documentação: {fun, __doc__}')
        return fun(*args, **kwargs)
    return logar


@ver_log
def soma(a,b):
    '''Soma algo'''
    return a+b

#Isso aqui só funciona corretamente se eu remover: @ver_log De cima da Função Soma
print(help(soma)) # Ou se usar o @wraps na Função que NÃO queremos que a documentação apareça.

#print(soma.__doc__) #Soma algo
#print(soma.__name__) #soma
