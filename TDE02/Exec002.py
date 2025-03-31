## A partir do ano de nascimento informado pelo usuário, elabore um algoritmo que informe
## a idade que completará (ou já completou) em 2023. Verifique se ele já pode fazer a carteira
## de motorista ou não, informando a sua situação.


BirthYear = int(input("enter your birth year: "))

year = 2023

age23 = BirthYear - year

if age23 + 2 == 18:
    print("Youre older than 18. You can get a drivers licence")

else:
    print("Youre too young. You cant get a drivers licence")