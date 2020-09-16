import datetime
"""
#Com Now podemos especificar um FusoHorario, pois com o .now() vem o Fuso do Sistema Junto.
now = datetime.datetime.now()
print(now)
print(type(now))
print(repr(now))

#Com Today nos não conseguimos.
Hoje = datetime.datetime.today()
print(Hoje)

"""
"""
# Mudanças acontecendo as 00 Horas: -> Usando o método combine()
#                             Metodo Para Juntar Data\Horas - Juntou o Agora com + UM dia & datetime.time() Zerou o Relogia p/ Meia Noite.
manutenção = datetime.datetime.combine((datetime.datetime.now() + datetime.timedelta(days=1)), datetime.time())

print(manutenção)
print(repr(manutenção))
"""

"""
manutenção = datetime.datetime.combine((datetime.datetime.now() + datetime.timedelta(days=1)), datetime.time())
print(manutenção.weekday()) #Primeiro segindo dias etc... Segunda=1 , Terça=2 etc...
"""



Aniversario = input("Data De Aniversario: ")
Aniversario = Aniversario.split('/')
Aniversario = datetime.datetime(year=int(Aniversario[2]), month=int(Aniversario[1]), day=int(Aniversario[0]))

if Aniversario.weekday() == 0:
    print('Nasceu Na Segunda Feira')
elif Aniversario.weekday() == 1:
    print('Nasceu Na Terça Feira')
elif Aniversario.weekday() == 2:
    print('Nasceu Na Quarta Feira')
elif Aniversario.weekday() == 3:
    print('Nasceu Na Quinta Feira')
elif Aniversario.weekday() == 4:
    print('Nasceu Na Sexta Feira')
elif Aniversario.weekday() == 5:
    print('Nasceu No Sabado')
elif Aniversario.weekday() == 6:
    print('Nasceu No Domingo')


#FORMATANDO DATAS/HORAS COM strftime() (String Format Time)
# dd/mm/yyyy
"""
hoje = datetime.datetime.today()
print(hoje)

# %b  Maiusculo Ou Minusculo -> Da o nome do Mês.
Hoje_Formatado_PT_BR = hoje.strftime('%d/%m/%Y') # %y Minusculo = Dois Digitos. %Y Maiusculo = 4 Digitos

#print(Hoje_Formatado_PT_BR)

def formata_data(data):
    if data.month == 1:
        return f'{data.day} De Janeiro de {data.year}'
    elif data.month == 2:
        return f'{data.day} De Fevereiro de {data.year}'
    elif data.month == 3:
        return f'{data.day} De Março de {data.year}'

print(formata_data(hoje))
"""


# Este método precisa de Conexão com a internet para Funcionar, Ele traduz o Texto Usando a Web.
from textblob import TextBlob
"""
Esta Função Tem Apenas Duas Linhas Contra a Outra Anterior a esta, que tinha muitas,
 E Esta faz a mesma Coisa.

"""
"""
def formata_data(data):
    return f"{data.day} De {TextBlob(data.strftime('%B')).translate(to='pt-br')} de {data.year}"

hoje = datetime.datetime.today()
print(formata_data(hoje))
"""

"""
Enter = str(input("Data De Aniversário dd/mm/yyyy: "))
#X = Enter.split('/')
Birth = datetime.datetime.strptime(Enter, '%d/%m/%Y')
print(Birth.day,"/",Birth.month,"/",Birth.year, "Hora: ", Birth.now())
"""

"""
#MARCANDO O TEMPO DE EXECUÇÃO DO NOSSO CODIGO:
import timeit

#loop For:
tempo = timeit.timeit('"-".join(str(n) for n in range(100))', number=25000)
print(tempo)

#ListComprehension:
tempo = timeit.timeit('"-".join([str(n) for n in range(100)])', number=25000)
print(tempo)

#Map:
tempo = timeit.timeit('"-".join(map(str, range(100)))', number=25000)
print(tempo)
"""
"""
import timeit, functools


def teste(n):
    soma = 0
    for num in range(n * 200):
        soma = soma + num ** num + 4
    return soma


#Testando a performance desta Função -> Partial recebe o nome da Função + O parametro de entrada para ela.
print(timeit.timeit(functools.partial(teste, 2), number=10))
"""

