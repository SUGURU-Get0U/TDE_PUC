# exercicio sobre listas 06

'''
Ler 4 números inteiros e calcular a soma dos que forem par

'''

# create a list that will keep the user inputs
Keys = []

# create our logic that recieves 4 for values than inserts them in the list
for potato in range(0,4):
    potato = int(input("Enter a value: "))
    Keys.append(potato)

# create a new list with only the even numbers
EvenNumbers = [i for i in Keys if i % 2 == 0]

# does the sum of the even numbers
Valorant = sum(EvenNumbers)

print("The sum of the even numbers are", Valorant)

#