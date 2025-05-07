# Exercicios sobre listas 9

'''
Elabore um programa que leia um vetor de 10 posições inteiras. Depois, solicite para o usuário um
número que ele gostaria de pesquisar neste vetor, caso o número exista no vetor, mostre em qual(is)
posição(ões) ele foi encontrado e quantas ocorrências foram detectadas.

'''

Array10 = [10,20,30,40,50,60,70,80,90,100]

print(*Array10)

user = int(input("Enter a number to search inside the list above: "))

#flag
found = False

#logic
for search in range(len(Array10)):
    if Array10[search] == user:
        print("Your number was found at index:" , search)
        found = True
        break
    
if not found:
    print("Unable to find number")


