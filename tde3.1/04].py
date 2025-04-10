
# Exercicio 4

"""

Faça um programa que peça dois números,
 base e expoente, calcule e mostre o primeiro número
elevado ao segundo número. Não utilize a função de potência da linguagem

"""

Num1 = int(input("Digite a base: "))
Num2 = int(input("Digite o expoente:  "))

potencia = 1

for i in range(Num2):
    potencia = Num1 * potencia

print("o valor eh : %d" %potencia)