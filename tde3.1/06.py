
# Exercicio 06

"""

Faça um programa que peça para n pessoas a sua idade,
ao final o programa deverá verificar se a
média de idade da turma varia entre 0 e 25,
 26 e 60 e maior que 60; e então, dizer se a turma é jovem,
adulta ou idosa, conforme a média calculada

"""
import random
from random import randrange

QuantPessoas = int(input("Digite o numero de pessoas: "))
soma = []

for idade in range(QuantPessoas):
    idade = randrange(15,70)
    print(idade, end= ' ')
    soma.append(idade)
    soma = sum(idade)
    media = soma / QuantPessoas

print(media)

if media < 25:
    print("sala full of calouros")

elif media < 60:
    print("sala adulta")

else:
    print("old people")

