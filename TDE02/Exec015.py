"""

Escreva um algoritmo que leia três números inteiros e mostre-os em ordem decrescente.


"""

# Passo 1: Ler os três números inteiros
numeros = []
for i in range(3):
  num = int(input(f"Digite o {i+1}º número: "))
  numeros.append(num)

# Passo 2: Ordenar os números em ordem decrescente usando sorted()
numeros_ordenados = sorted(numeros, reverse=True) # SORTED ORGANIZA OS ELEMENTOS EM ORDEM CRESCENTE, REVERSE TRUE INVERTE A ORDEM

# Passo 3: Mostrar os números em ordem decrescente
print("Números em ordem decrescente:", numeros_ordenados)


