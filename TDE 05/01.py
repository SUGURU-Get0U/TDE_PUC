# Exercícios sobre listas:

'''
Construa a tabela de multiplicação de 1 a 10.
 (Ex: 1x1 = 1, 1x2=2, 10x10 =100)

'''

num = [1,2,3,4,5,6,7,8,9,10] # lista com os números
multiplicador = 1 # number that will increase troughout the code

while multiplicador < 11:
# plan -> make a loop that multiplies our m variable by all the integers in our list
    for numbers in num:
        print(f"{multiplicador} X {numbers} ==", multiplicador * numbers)
        print(f"Tabuada do {multiplicador}")
    # it will finish when the multiplicator reaches 10
    multiplicador += 1
print(" It's Gojover :( ")
    
    


    


        