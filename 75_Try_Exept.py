'''
entrada = input("Digite Algo: ")

LT = []

try:
    LT.append(entrada)
except:
    print('Apenas Valores INT')
'''

'''
#Trata Qualquer Erro:
try:
    Erroouu()
except:
    print("Deu Pau")
'''

'''
#Para erros especificos:
try:
    Erroouu()
except NameError:
    print("Deu Pau")

#Aqui ele deu uma explicação do que aconteceu de errado.
try:
    len(3)
except TypeError as ERRADO:
    print(f'A aplicação gerou um Bug do tipo {ERRADO}')
'''

'''
#Tratando Varios Erros de Uma vez:
try:
    #Aqui poderia haver um codigo com vários tipos de erros diferentes.
    #len(2) #Type Erro
    errado()#Name Erro
except TypeError as Erro_Digitac:
    print(f'Erro-> {Erro_Digitac}')
except NameError as Nome_Errado:
    print(f'Erro do Tipo{Nome_Errado}')
'''

def pega_valor(Dikt, KEY):
    try:
        return Dikt[KEY]
    except KeyError:
        return 'Deu Pau geral merrmão :0 CHAVE NÃO EXISTE'
    except TypeError:
        return 'Este Dicionario Não Existe -_-'
    except:
        '''Para erros desconhecidos ou Nçao especificados a cima
        Usa-se isto generico aqui.'''
        return None



dicio = {'Nome':"Valor_Do_Dict"}

print(pega_valor(dicio,'Non Existe'))

print(pega_valor(9,'Non Existe'))
