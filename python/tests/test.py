import time
import psutil
import loop
import recursion
# inicio teste de velocidade de execução
tempoInicial = time.time()
loop.fatorial(555)
tempoFinal = time.time()
print(f"tempo de execução código em LOOP {(tempoFinal-tempoInicial)} segundos")
print(psutil.virtual_memory()[2])
#fim

#inicio teste de velocidade de execução
tempoInicial = time.time()
recursion.fatorial(555)
tempoFinal = time.time()
print(f"tempo de execução código em Recursao {(tempoFinal-tempoInicial)} segundos")
print(psutil.virtual_memory()[2])
#fim