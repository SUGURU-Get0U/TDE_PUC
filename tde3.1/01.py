
# Exercicio 1

"""

Ler do teclado uma quantidade de números inteiros a serem lidos e calcular:
a) a soma total entre eles
b) a soma dos que forem pares.
c) a soma dos que forem ímpares
d) a amplitude amostral considerando todos os números lidos (diferença entre o maior e o menor)

"""

amlpitude = []


Limite = int(input("Digite o limite dos números a serem contados: "))
contPAR = 0
contImpar = 0


contNum = 1

while contNum <= Limite:
    entDados = int(input("Digite um número: "))
    amlpitude.append(entDados)
    contNum += 1
    amlpitude = sorted(amlpitude)
    if entDados % 2 == 0:
        contPAR += entDados
    else:
        contImpar += entDados


print("A soma total dos números é: ", sum(amlpitude))
print("A soma dos Pares é: ", contPAR)
print("A soma dos Impares é: ", contImpar)
print("a amplitude amostral desta lista eh: ", amlpitude[-1] - amlpitude[0])






