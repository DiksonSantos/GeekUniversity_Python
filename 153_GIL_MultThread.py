import time
from threading import Thread

CONT = 5000000


def contagem_reg(m):
    while m > 0:
        m -= 1

t1 = Thread(target=contagem_reg, args=(CONT//2,))
t2 = Thread(target=contagem_reg, args=(CONT//2,))

inicio = time.time()
t1.start()
t2.start()
t1.join()
t2.join()
fim = time.time()

print(f"Tempo em Segundos {fim - inicio}")#Tempo em Segundos 0.5333559513092041
