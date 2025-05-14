
# Plan -> 
matrix = []  # This is correct
# get the users input
userIndex = int(input("Digite o número de linhas da matrix: ")) # This is correct
userColunms = int(input("Digite o número de colunas da matrix: ")) # This is correct


# matrix = [userIndex][userColunms] 
# This does not create a matrix with the dimensions
# Instead it tries to access that index

matrix = [[0 for _ in range(userColunms)] for _ in range(userIndex)]




# FOR EACH AVAILABLE SPACE IN THE MATRIX:
for i in range(len(matrix)):
    for c in range(len(matrix[0])):
    # FILL THEM WITH 1
        matrix[i][c] = 1

for rows in matrix:
    while True:
        print(rows)


