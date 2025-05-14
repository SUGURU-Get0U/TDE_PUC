# matrizes

m = [[1,2,3],
     [3,4,5],
     [9,8,7]]

column = len(m[0]) # saber o número de colunas

# para acessar os elementos de uma matriz
    # var [linha] [coluna] = atribuir elemento
    #     ------  ||||||||

# soma?

n = [[2,3,4],[1,5,4],[234,3,23]]

# mostrar todos os elementos da matriz 

for linhas in range(len(m)):
    for colunas in range(len(m[0])):
        print(m[linhas][colunas], end=" ")

    print('')


multiple = [(2,3,"banana"),
            ["baiacu",True,32],
            (n,34,2)]

for linhas in range(len(m)):
    for colunas in range(len(m[0])):
        print(multiple[linhas][colunas], end=" ")
print('')


print('linha diagonal')
for linhas in range(len(m)):
    for colunas in range(len(m[0])):
        if linhas == colunas:
            print(multiple[linhas][colunas], end=" ")
print('')

print('Triangulo Superior -- Coluna > linha')
for linhas in range(len(m)):
    for colunas in range(len(m[0])):
        if linhas < colunas:
            print(multiple[linhas][colunas], end=" ")
print('')

print('Triangulo Inferior -- Coluna < linha')
for linhas in range(len(m)):
    for colunas in range(len(m[0])):
        if linhas > colunas:
            print(multiple[linhas][colunas], end=" ")
print('')