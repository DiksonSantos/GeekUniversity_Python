import math


def circunferencia(raio):
    # type: (float) -> float
    return 2 * math.pi * raio

#W = circunferencia(8)
#print(f"Float, Mas Com 2 num depois da Virg: {W:.2f}")
#print("Original Float: ", W)
#print(round(circunferencia(8)))
#print(int(circunferencia(8)))


"""
Se passar um argumento que NÃO seja float. Mesmo que Não tenhamos colocado o trecho:]
(float) -> float nos argumentos de entrada, e que estes sejam apenas um #Comentário,
o mypy ainda sim consegue funcionar para testar o código.
EX:
"""


#print(circunferencia("String"))
""" O que acontece é:
Argument 1 to "circunferencia" has incompatible type "str"; expected "float"
Found 1 error in 1 file (checked 1 source file)

Se colocar do jeito tradicional (Ou seja: ao lado dos argumentos de entrada
e ainda usar também o #Comentário. Da pau. Vai dizer que esta duplicado.
"""


def cabecalho(texto, alig=True):
    # type: (str, bool) -> str   #Sequencia correspondente aos argumentos.
    if alig:
        return 'Alpha'
    else:
        return 'Bravo'

#X = cabecalho(texto=34, alig=000) #Usando o comando mypy+NomeDoArquivo ele aponta 2 problemas.
#print(X)


#ESTA É A FORMA MAIS ZUADA E BAGUNÇADA, SEGUNDO TBM O PROFESSOR, EU CONCORDO. (NÃO RECOMENDADO).
def cab2(
        texto,  # type: str
        alinhamento=True  # type: bool
):  # type: (...) -> str
    if alinhamento:
        return "Alpha"
    else:
        return "Bravo"

#cab2(texto=34, alinhamento='Dikson') # Ele ascende Indicando Problema
cab2(texto='34', alinhamento=True) #No Problem !


Nome = "Geremias" # type: str
