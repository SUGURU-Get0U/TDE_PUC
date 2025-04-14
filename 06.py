
#  Exercicio 06
"""
 Faça um programa que peça para "n" pessoas a sua idade,
 ao final o programa deverá verificar se a
 média de idade da turma varia entre 0 e 25,
 26 e 60 e maior que 60; e então, dizer se a turma é jovem,
 adulta ou idosa, conforme a média calculada
"""
from IPython.core.display_functions import display

qp = int(input("Digite a quantidade de pessoas: "))
idade = 0
sI = 0
Media = 1

for anos in range(0,qp):
    idade = int(input("Digite a idade das pessoas: "))
    sI += idade
    Media = sI / qp

if Media < 25:
    display("A turma eh jovem")

elif Media < 60:
    display("A turma eh adulta")

else:
    display("A turma eh idosa")