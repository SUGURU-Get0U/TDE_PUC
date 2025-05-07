# Exercicio sobre listas 10

'''
esenvolva um programa que leia 10 números inteiros e armazene-os em um vetor chamado vLido.
Depois, crie dois outros vetores: vPares, contendo somente os números pares de vLido, e vImpares
contendo somente os números ímpares de vLido. Os vetores vPares e vLido não deverão conter
zeros. Mostre então os três vetores.

'''
vLido = []

# recieve 10 numbers
for yamal in range(0,10):
    yamal = int(input("Enter a value: "))
    vLido.append(yamal)

# list comprehension to add the even numbers different from 0 to a separate list
vEven = [p for p in vLido if p % 2 == 0 and p != 0]

# list comprehension that adds the odd numbers different from 0 to a separate list
vOdd = [o for o in vLido if o % 2 != 0 and o != 0]

# Displaying both lists
print(f"This is the list with the even numbers different from 0 {vEven}")
print("--------------------------------------------------------------------")
print(f"This is the list with the odd numbers different from 0 {vOdd}")