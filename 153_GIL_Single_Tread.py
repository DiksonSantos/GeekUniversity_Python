import time
from threading import Thread

CONTADOR = 5000000
COn = 50

def contagem_regressiva(n):
    while n > 0:
        n -= 1


inicio = time.time() #Tempo atual ao iniciar a contagem Regressiva de 500000
contagem_regressiva(CONTADOR)
fim = time.time()# Tempo atual ao finalisar a COntagem regressiva

# Fim - Inicio = Tempo Decorrido/Durante a contagem regressiva.
print(f"Tempo em Segundos: {fim - inicio}")# Tempo em Segundos: 0.4945077896118164

