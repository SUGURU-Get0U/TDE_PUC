'''

Elabore um programa que preencha uma matriz quadrada (4x4) de números inteiros,
sorteados dentro
do intervalo 100 a 999, garantindo que não haverá nenhuma repetição
 (os 16 números devem ser
únicos).
Encontre então o valor do menor elemento da linha em que se encontra o maior elemento da
matriz. Mostre a matriz e os dois valores encontrados.

'''
from random import randint

matrizQuadrada = [[0 for line in range(4)] for column in range(4)]
# matriz preenchida com 0s
valoresUtilizados = []
vetorAux = [] # vetor auxiliar
maiorNum = 0 # 8
linhaMaior = 0 # 0

for l in range(len(matrizQuadrada)):
    for c in range(len(matrizQuadrada[0])):
        dataA = randint(100,999)
        while dataA in valoresUtilizados:
            dataA = randint(100,999) #8
        valoresUtilizados.append(dataA) #8
        matrizQuadrada[l][c] = dataA #8
        if dataA > maiorNum: #16 > #8
            maiorNum = dataA # 16
            linhaMaior = l # 1

for rows in matrizQuadrada:
    print(*rows)

# Menor número
vetorAux = matrizQuadrada[linhaMaior]
menorNum = vetorAux[0]
for nums in vetorAux:
    if menorNum > nums:
        menorNum = nums




print(f"O menor número da linha do maior número é: {menorNum}")
print(f"O maior valor desta matriz é: {maiorNum}")







