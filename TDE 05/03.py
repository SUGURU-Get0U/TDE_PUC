# Exercicios sobre lista 03

'''
Leia três números do teclado e 
verificar se o primeiro é maior que a soma dos outros dois

'''
KeepNumber = []

for num in range (0,3):
    num = int(input("Type in a value: "))
    KeepNumber.append(num)

if KeepNumber[2] == KeepNumber[0] + KeepNumber[1]:
    print("Aot is peak")

else:
    print("The index [2] is not a result of the sum of indexes [0] and [1].")
