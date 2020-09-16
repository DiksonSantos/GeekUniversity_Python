'''
Decorators Com Diferentes Assinaturas
'''

'''
def gritar(fun):
    def aumentar(nome):
        return fun(nome).upper()
    return aumentar

@gritar
def saudacao(nome):
    return f'Ola Eu Sou {nome}'

@gritar
def dar_ordem(main, keep_up):
    return f'Hello I Would Like to a {main}, and an {keep_up}'

#Testando:

#A função SAUDAÇÃO foi Absorvida pela Fun Gritar, sendo Assim esta fun saud.. recebe o tratamento da Gritar
#..Pois ela passa por dentro dela.
x = saudacao('Dikson')
#print(x)

#-> Se fosse fazer SEM o uso do decorador E com a função precisando de uma Informação
#..parametro Externo já ia dar Pau.

print(dar_ordem('Batata Assada', 'Molho Branco'))

#-> ESTE BLOCO INTENCIONALMENTE DEU PAU DEVIDO A DIFERENTE QUANTIDADE DE ARGUMENTOS ENTRE AS FUNÇÕES ENTRELAÇADAS.

'''

def gritar(fun):
    def aumentar(*args, **kwargs):
        return fun(*args, **kwargs).upper()
    return aumentar

@gritar
def saudacao(nome):
    return f'Ola Eu Sou {nome}'

@gritar
def dar_ordem(main, keep_up):
    return f'Hello I Would Like to a {main}, and an {keep_up}'


#print(saudacao("Happy Endings"))

#-> Funcionou graças ao *args  &  **kwargs
#print(dar_ordem('Batata', "Molho"))


def verifica_primeiro_argumento(valor):
    def interna(fun):
        def outra(*args, **kwargs):
            if args and args[0] != valor:
                return f'Valor Incorreto! Primeiro Argumento Precisa Ser {valor}'
            return fun(*args, **kwargs)
        return outra
    return interna


@verifica_primeiro_argumento('Pizza')
def favorite_meals(*args):
    print(args)

@verifica_primeiro_argumento(10) #Diz ou Ordena que o primeiro Argumento DEVE SER 10, e nenhum outro numero.
def soma_dez(n1, n2):
    return n1, n2

#TESTES:

#print(soma_dez(1,20)) # Valor Incorreto!

#print(favorite_meals("Pão")) # Valor Incorreto! Primeiro Argumento Precisa Ser Pizza

