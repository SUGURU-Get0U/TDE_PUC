"""
Desenvolva um programa que leia uma matriz quadrada de números inteiros de dimensão (4×4), e
então coloque em um outro vetor de 4 posições o maior valor encontrado na coluna da matriz cujo
índice é o mesmo do vetor, ou seja, o maior valor da coluna zero da matriz na posição zero do vetor e
assim por diante. Mostre então a matriz, o vetor e a média aritmética do vetor.

"""
from random import choice as c
from random import randint      # 1,2,3 3,2,1   2,1,3 , 2,3,1  1,3,2 , 3,1,2 

#plan -> 

    # Create a matrix that is 4 by 4 dimensioned
        # create a matrix full of 0s
    # Create a array with 4 integers
myArray = [0,0,0,0]    # same as myArray = [0] * 4    
myMatrix = [[0 for _ in range(4)] for _ in range(4)]

    # fill the matrix with a random number
for i in range(len(myMatrix)): # lines
    for c in range(len(myMatrix[0])): #columns
        myMatrix[i][c] = randint(2,50) # fill all of the integers with random numbers
        
# Find the maximum value in each column and store it in myArray
for c in range(4):
    max_val = myMatrix[0][c] # starts with the first value as the biggest
    for i in range(4):
        if myMatrix[i][c] > max_val:
            max_val = myMatrix[i][c]
        myArray[c] = max_val
        

    # display the matrix

print("The matrix: ")

for rows in myMatrix:
    print(rows)

print("Array with the biggest numbers of each row: ")
print(*myArray, "|")

print("average sample")

a = sum(myArray) / len(myArray)
print(" the average sum is: ", a    )

    # Create a array with 4 integers

        # Insert in the array the numbers that have the same index as the one in the array,  or 
        # the biggest number in the column of the matrix that corresponds to its index 0.
    