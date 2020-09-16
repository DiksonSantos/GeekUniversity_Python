from multiprocessing import Pool
import time

CON = 5000000
CO = 50

def cont_reg(m):
    while m > 0:
        m -= 1


if __name__ == '__main__':
    pool = Pool(processes=2)
    inicio = time.time()
    R1 = pool.apply_async(cont_reg, [CO//2])
    R2 = pool.apply_async(cont_reg, [CO//2])
    pool.close()
    pool.join()
    fim = time.time()
    print(f"Tempo Decorrido {fim - inicio}") # Tempo Decorrido 0.09767413139343262

print("Este foi o Teste mais Rápido dos 3")
