'''

Tendo como dados de entrada a altura (h) e o sexo de uma pessoa (use 1 - masculino e 2 -
feminino) elabore um algoritmo que calcule o peso ideal (p) do usuário utilizando as
seguintes fórmulas:
a. para homens: p = (72,7 * h) - 58
b. para mulheres: p = (62,1 * h) - 44,7

'''

# Entrada com o sexo
Gender = int(input("Escolha o seu genero:  Digite 1 para masculino  e  2 para feminino: "))
altura = float(input("Agora digite sua altura: "))

if Gender == 1:
    pesoIdeal = (72.7 * altura) - 58
    pesoIdeal = round(pesoIdeal,1)
    print(f"Seu peso ideal eh {pesoIdeal: 1f}")

else:
    pesoIdeal = (62.1 * altura) - 44.7
    pesoIdeal = round(pesoIdeal,1)
    print(f"Seu peso ideal eh {pesoIdeal: 1f}")


