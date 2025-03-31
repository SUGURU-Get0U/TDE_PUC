"""

14. Escreva um algoritmo que leia três números inteiros e mostre o valor do maior deles.


"""

numeros = []  # Lista para armazenar os números

for i in range(3):  # Pede 3 números ao usuário
    num = int(input("Digite um número: "))
    numeros.append(num)  # Adiciona o número à lista

maior = numeros[0]  # Assume que o primeiro número é o maior

for num in numeros:  # Itera pela lista de números
    if num > maior:  # Se encontrar um número maior, atualiza a variável 'maior'
        maior = num

print("O maior número é:", maior)