
# Exercicio 9

"""

Imprima os números múltiplos de 3 entre li (limite inicial) e lf (limite final). Os
valores inteiros de li e lf devem ser informados pelo usuário e não pertencem ao
intervalo, ou seja, intervalo aberto

"""

li = int(input("Digite o limite inicial: "))
lf = int(input("Digite o limite final: "))

for X in range(li + 1, lf):
    print(X)