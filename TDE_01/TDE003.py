# Faça um algoritmo que receba o salário de um profissional e calcule quantos salário
# mínimos ele recebe


MonthlyWage = float(input("Digite o seu salario: "))

minimumWage = 1.518

Taxes =  MonthlyWage / minimumWage
Taxes = round(Taxes, 1)

print('voce ganha: ', Taxes, 'salarios minimos por mes')

