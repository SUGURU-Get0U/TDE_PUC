
# Exercicio 06

"""

Imprima uma tabela de conversão de polegadas para centímetros, cuja escala vai de
1 a 20 polegadas (approx. 51 cm). A conversão entre estas duas unidades é dada por: polegada =
centímetro × 2,54

"""

n = 0
inches = 0


while n < 20:
    n += 1
    inches = n * 2.54
    print(abs(inches))

print("Done") # Nao aproxima os valores