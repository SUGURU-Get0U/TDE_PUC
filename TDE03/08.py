
# Exercicio 08

"""

Elabore um algoritmo que leia um conjunto de 10 números inteiros. Mostre então
qual o valor da soma e da média aritmética do conjunto.

"""

c1 = 0
n = 0
s = 0
av = 0



while c1 < 10:
    n = int(input("Enter a number: "))
    c1 += 1
    s += n
    av = s / c1
    print("The sum is,", s, " and the arithmetic mean is, ", av)


"""


c1 = []

for i in range(1,10):
    num = int(input("Enter a number: "))
    c1.append(num)

# faz a soma dos algarismos na lista
soma = sum(c1)

# faz a média, LEN da a quantidade de números
media = soma/ len(c1)

print("a soma dos numeros eh: ", soma)
print("a media dos numeros eh: ",media)

"""


