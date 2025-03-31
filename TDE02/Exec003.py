'''

Elabore um algoritmo que leia um número inteiro e mostre a sua raiz quadrada (informe
“Valor inválido” para números negativos).

'''

import math

print("bem vindo ao calculador de raiz quadrada 3000")

Numero = int(input("Digite o numero: "))

while Numero <= 0:
    print("Valor invalido, o numero colocado tem que ser maior que zero")
    Numero = int(input("Digite o numero: "))


retorno = math.sqrt(Numero)
print(f"A raiz quadrada eh: {retorno} ")



