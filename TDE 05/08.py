# exercicio sobre listas 08

'''
A Amplitude amostral é uma médida de dispersão, ela é calculada como a diferença entre o valor
máximo e o valor mínimo de uma amostra. Elabore um programa que leia um vetor de 10 posições
inteiras e então mostre o valor máximo, o valor mínimo e a amplitude amostral do conjunto
fornecido.

'''

# create a list 
mirror = []

# logic to ask for 10 numbers
for num in range(0,10):
    num = int(input("Enter a number: "))
    mirror.append(num)

# know who is the smallest and biggest number of the list
Sorted_List = sorted(mirror)

# calculate what was asked
AdoGoat = Sorted_List[9] - Sorted_List[0]

print(f"The maximum value is {Sorted_List[9]}")
print(f"The minimum value is {Sorted_List[0]}")
print(f"The sample range is {AdoGoat}")
