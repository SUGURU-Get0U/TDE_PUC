'''

implemente um programa que permita multiplicar uma matriz de ordem (3×3) de números inteiros
fornecida pelo usuário por um número também fornecido pelo usuário.
Lembrete: para multiplicar uma matriz Am×n por um escalar k, basta multiplicar cada entrada aij
de A por k. Assim, a matriz resultante B será também da ordem (m×n) e bij = k * aij


'''

# Matriz vazia
m = [[0 for _ in range(3)]for _ in range(3)]
# Resultado
B = []

for lines in range(len(m)):
    for col in range(len(m[0])):
        while True:
            try:
                n = int(input("num: "))
                m[lines][col] = n
                break
            except ValueError:
                print("Erro")

print("A matriz original é: ")
for rows in m:
    print(m)

mms = int(input("num multiplicador: "))

print("A matriz multiplicada é: ")
for linhas in range(3):
    for col in range(3):
        m[linhas][col] = n * mms

print(m)






