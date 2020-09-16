"""
Delta é a diferença entre uma data inicial Menos a Data Final:

03-04-2020 á 04-05-2020   -> Delta = 31 Dias

"""

"""
import datetime

data_hoje = datetime.datetime.now()

Birthday = datetime.datetime(2021, 3, 24, 00)

Res = data_hoje - Birthday

print(Res*-1) # 365 days, 20:38:56.004360     -> Hoje é 23-03-2020   03:20H Matina.
print(Res.days*-1, " Dias Restantes")

print(type(Res)) # Tipo TimeDelta
"""

import datetime

Data_Compra = datetime.datetime.now()

Regra_Boleto = datetime.timedelta(days=3)

print(Regra_Boleto)

Vencimento = Data_Compra + Regra_Boleto

print("Data Do Vencimento: ", Vencimento.day, "/", Vencimento.month, "/", Vencimento.year)
