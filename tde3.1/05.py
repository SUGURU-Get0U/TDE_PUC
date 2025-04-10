
# Exercicio 5

"""

Faça um programa que calcule o fatorial
 de um número inteiro fornecido pelo usuário. Ex.: 5! = 5 x 4
x 3 x 2 x 1 = 120

"""

n = int(input("Digite o numero: "))

i = 1

cont = 1

while cont <= n:
    i = i * cont
    cont += 1

print(i)