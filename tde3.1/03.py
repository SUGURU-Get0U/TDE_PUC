
#Exercicio 3

"""

Supondo que a população de um país A seja da ordem de 80.000 habitantes com uma taxa anual de
crescimento de 3% e que a população de B seja 200.000 habitantes com uma taxa de crescimento de
1.5%. Faça um programa que calcule e escreva o número de anos necessários para que a população
do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento

"""
from statsmodels.sandbox.regression.try_ols_anova import anova_str

Pais_A = 80
Pais_B = 200

cont = 0
crescimentoA = Pais_A * 0.03
crescimentoB = 0.015

while Pais_A <= Pais_B:
    Pais_A = Pais_A + crescimentoA
    cont += 1
    print(cont, " | ", round(Pais_A,2))

print("levará %d"%cont, "anos para o Pais A igualar B")