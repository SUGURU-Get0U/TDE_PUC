# Exercicio about lists

'''
Escreva um programa que leia um vetor de números inteiros de 10 posições, aceitando apenas
valores positivos. Modifique então o vetor de forma que, tenhamos primeiro todos os números pares,
depois, os números impares. Mostre o vetor antes de depois da modificação

'''
# create a single list
Array = []

# Recieve 10 values
    # Variable the checks if the number is positive
while len(Array) < 10:  # Loop until 10 positive numbers are collected
    try:
        user_input = input("Enter a positive number: ")
        number = int(user_input)
        if number > 0:
            Array.append(number)
        else:
            print("Invalid value, please enter a positive number.")
    except ValueError:
        print("Invalid input. Please enter a whole number.")

# insert the even numbers at index 0
even_numbers = [e for e in Array if e % 2 == 0]
# insert the odd numbers at index -1
odd_numbers = [odd for odd in Array if odd % 2 != 0]

# Display the list
newList = even_numbers + odd_numbers
print(newList)


