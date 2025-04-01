
# Exercicio 07

"""

Considerando que 1 milha (1,61 km) vale exatamente 1.609,344 metros, imprima uma tabela
de conversão de metros (m) para milhas (mi.), de 20 km até 160 km, a cada 10
quilómetros

"""
# 1km == 1000m
N = 20000
Mile = 0

while N < 160000:
    N += 10000
    Mile = N * 1.61
    print(round(Mile,2))

print("Done")