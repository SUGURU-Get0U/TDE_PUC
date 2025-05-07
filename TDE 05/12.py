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
User = []

# PC choice of numbers
Rchoice = rr.sample(range(1,61), 6)
Pc.append(Rchoice)

UguessCounter = 0
# User guessing
while UguessCounter != 6:
    try:
        Uguess = int(input("Enter a number between 1 and 60"))
        if Uguess < 0 or Uguess > 60:
            print("Invalid Output, please type in a number between 1 and 60")
        else:
            UguessCounter += 1
            continue
    except ValueError:
        print("Type in a number bro....")

# grab the pc choices and compare then with the user choices


        

