import datetime
"""
#print(dir(datetime))

#print(datetime.datetime.now())# 2020-03-23 02:43:18.144400

print(repr(datetime.datetime.now()))

#REPLACE P FAZER AJUSTES NO FORMATO:


Inicio = datetime.datetime.now()

#Substitui a hora atual por alguma prédefinida:
Inicio = Inicio.replace(hour=23, minute=30, second=00, microsecond=21)

print(Inicio)
"""
#                         (Ano, Mês, Dia, Hora)
evento = datetime.datetime(2020, 3, 24, 13)
#print(evento)

print('DD/MM/AA')
Birthday = input("Informe Data de Nascimento: ")

Nascimento = Birthday.split('/')

Nascimento = datetime.datetime(int(Nascimento[2]), int(Nascimento[1]), int(Nascimento[0]))

#Fazendo acesso para reposicionar:
print(Nascimento.day, Nascimento.month, Nascimento.year)





#print(type(Nascimento)) #Lista de Strings
