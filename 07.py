
# Exercicio 07

"""

Os números primos possuem várias aplicações dentro da Computação, por exemplo, na Criptografia.
Um número primo é aquele que é divisível apenas por um e por ele mesmo. Faça um programa que
peça um número inteiro e determine se ele é ou não um número primo

"""
from IPython.core.display_functions import display

num = int(input("Digite um numero: "))
lista = [1,2,3,4,5,6,7,8,9,10]


while num < 0:
    num = int(input("Digite um valor maior que zero: "))



lista.insert(0,num)

if num % lista[0] == 0 and num % lista[1] == 0 and num % lista[2] != 0\
        and num % lista[3] != 0:
    print("O numero eh primo")

else:
    print("O numero nao eh primo")




