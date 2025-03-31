# Faça um algoritmo que leia o ano de nascimento de uma pessoa e calcule a idade
# que completará em 2022
from robot.model import While

Ano = 2022

while True:
    try:
        AnoNasc = int(input('Digite o ano do seu nascimento por favor: '))
        if AnoNasc < 0:
            print('Insira um algarismo positivo por favor.')
            continue
        break
    except ValueError:
        print('Insira um número por favor.')

Idade = Ano - AnoNasc

if Idade < 0:
    print(' o ano correspondente nao existe')
else:
    print("Voce tem: ",Idade, "anos")