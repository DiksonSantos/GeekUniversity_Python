'''
Decorators:

São funções
Envolvem outras funções e aprimoram seus comportamentos:
Decorators tem uma sintaxe propria.
'''

#Decorators como Funções (NÃO Recomendado):

def seja_Educado(func):
    def sendo(): #Isso não passa de uma função filha que usa o Argumento da Fun Mãe
        print('Foi Um Prazer Conhecer você')
        func() #Argumento da Função Mãe
        print('Tenha Um Otimo Dia')
    return sendo


def saudacao():
    print('Seja Bem Vindo')

#Testando:
teste = seja_Educado(saudacao) #Isto é uma Função Decorada
#teste()

#TESTE 2:

def odeio():
    print("Eu Te Odeio")

Raiva_Mole = seja_Educado(odeio)
#Raiva_Mole()


#DECORATOR COM SYNTAX SUGAR (Açucar Sintatico):

def seja_educado_mesmo(funcao):
    def sendo_mesmo():
        print('It Was a Prize To Meet You')
        funcao() #Isso aqui Executa a Função recebida como Parametro poe Esta Função Aqui
        print('Have an excelent Day')
    return sendo_mesmo


#@seja_educado_mesmo                    # O @ Juntou as Duas Funções:        #Isso Aqui é o Decorador.
def apresentando():
    print("My Name Is Suggar")

#Testando:  Com o @ ficaria Assim Apenas:
#apresentando()

#SEM O @ TERIAMOS QUE USAR DA MANEIRA A BAIXO:
y = seja_educado_mesmo(apresentando)
y()


@seja_Educado
def quero_dormir():
    print('I Want to Sleep')

#quero_dormir()
