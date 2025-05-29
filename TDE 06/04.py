from random import randint

def preencher_matriz():
    return [[randint(10, 99) for _ in range(5)] for _ in range(5)]

def mostrar_matriz(matriz):
    for linha in matriz:
        print(*linha)

def exec_1(matriz):
    print("Exec 1: Coluna [2] e Linha [2]:")
    print("Coluna [2]:", [matriz[i][2] for i in range(5)])
    print("Linha [2]:", matriz[2])
    soma = sum(matriz[i][2] for i in range(5)) + sum(matriz[2]) - matriz[2][2]
    print("Soma:", soma)

def exec_2(matriz):
    print("Exec 2: Primeira e Última Linha e Coluna:")
    primeira_linha = matriz[0]
    ultima_linha = matriz[-1]
    primeira_coluna = [linha[0] for linha in matriz]
    ultima_coluna = [linha[-1] for linha in matriz]
    
    print("Primeira Linha:", primeira_linha)
    print("Última Linha:", ultima_linha)
    print("Primeira Coluna:", primeira_coluna)
    print("Última Coluna:", ultima_coluna)
    
    soma = sum(primeira_linha) + sum(ultima_linha) + sum(primeira_coluna) + sum(ultima_coluna)
    soma -= matriz[0][0] + matriz[0][4] + matriz[4][0] + matriz[4][4]
    print("Soma:", soma)

def exec_b(matriz):
    print("\nMatriz original:")
    mostrar_matriz(matriz)

    print("\nExibindo valores nas posições incrementadas:")
    linha = 0
    coluna = 1

    while linha < len(matriz) and coluna < len(matriz[0]):
        # Exibe o valor em [linha][coluna] e [coluna][linha]
        print(f"matriz[{linha}][{coluna}] = {matriz[linha][coluna]}")
        print(f"matriz[{coluna}][{linha}] = {matriz[coluna][linha]}")
        print("---")
        
        # Incrementa os índices para próxima iteração
        linha += 1
        coluna += 1

def exec_4(matriz):
    print("Exec 4: Elementos em posições com índices pares:")
    elementos = []
    for i in range(0, 5, 2):
        for j in range(0, 5, 2):
            elementos.append(matriz[i][j])
            print(f"[{i}][{j}]: {matriz[i][j]}")
    print("Soma:", sum(elementos))

def calcular_soma_total(matriz):
    return sum(sum(linha) for linha in matriz)

# Programa principal
matriz5x5 = preencher_matriz()
print("Matriz Gerada:")
mostrar_matriz(matriz5x5)
print()

exec_1(matriz5x5)
print()
exec_2(matriz5x5)
print()
exec_b(matriz5x5)
print()
exec_4(matriz5x5)
print()

print("Soma total da matriz:", calcular_soma_total(matriz5x5))
