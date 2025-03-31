"""
partir da idade informada de uma pessoa, elabore um algoritmo que informe a sua
classe eleitoral, sabendo que menores de 16 não votam (não votante), que o voto é
obrigatório para adultos entre 18 e 65 anos (eleitor obrigatório) e que o voto é opcional
para eleitores entre 16 e 18, ou maiores de 65 anos (eleitor facultativo)

"""


Idade = int(input("Digite sua idade: "))


if Idade < 16:
    print("nao votante")

elif Idade > 65 or Idade < 18:
    print("Nao facultativo")

else:
    print("Eleitor obrigatório")

