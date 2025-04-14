
# Exercicio 08

"""

Faça um programa que gera uma lista dos números primos existentes entre 1 e um número inteiro
informado pelo usuário

"""

# saber o limite de numeros

def encontrando_primos(limite):

    primos = []
    for num in range(2,limite + 1):
        primo = True
        for x in range(2, int(num**(1/2) + 1)):
            primo = False
            break
        if primo:
            primos.append(num)
    return primos

limite01 = int(input("Digite o limite: "))

numPrimo = encontrando_primos(limite01)

print(numPrimo)
