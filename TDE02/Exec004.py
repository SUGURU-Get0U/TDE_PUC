'''

Um produtor de abóboras deve verificar a classificação dos seus produtos para posterior
empacotamento e venda. Um dos seus clientes compra apenas abóboras médias (aquelas que
possuem o diâmetro (d) no intervalo 15 cm ≤ d < 20 cm). Elabore um algoritmo que leia o
diâmetro de uma abóbora e mostre se ela é do tipo médio ou não. Caso ela não se encaixe
na classificação, informe “produto fora das medidas”


'''

print("Bem-vindo ao super medidor de aboboras!")

Diametro_Abobora = int(input("Digite o diametro da sua abobora <3 :  "))

if Diametro_Abobora >= 15:
    if Diametro_Abobora < 20:
        print("Sua abobora eh boa para venda!!")

else:
    print("Abobora fora das medidas")


