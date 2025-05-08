# Exercicio sobre listas 12

'''
Construa um programa que sugira uma aposta de Mega-Sena ou seja, um algoritmo que gera e mostra
um conjunto de 6 números aleatórios entre [1, 60] sem repetição. Em seguida, obtenha a aposta do
usuário (sem repetição) e indique quantos acertos ele teve

'''

# import 
import random as rr

# List that will keep the values.

Pc = []
User  = []

# PC choice of numbers
Pc = rr.sample(range(1, 61), 6)
print(f"PC's numbers: {Pc}")

# User guessing
while len(User) < 6:
    try:
        Uguess = int(input("Enter a number between 1 and 60: "))
        if Uguess < 1 or Uguess > 60:
            print("Invalid Output, please type in a number between 1 and 60")
        elif Uguess in User:
            print("You already guessed that number. Try again.")
        else:
            User.append(Uguess)
    except ValueError:
        print("Type in a valid number.")

# Count the number of correct guesses
correct_guesses = set(Pc) & set(User)  # Intersection of both sets
num_acertos = len(correct_guesses)

# Output results
print(f"Your numbers: {User }")
print(f"Correct guesses: {correct_guesses}")
print(f"You got {num_acertos} correct!")










