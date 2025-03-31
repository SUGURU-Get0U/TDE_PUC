"""

Elabore um algoritmo que, dada a idade de um nadador, mostre a sua classificação
segundo uma das seguintes categorias:
• 5 até 7 anos: Infantil A;
• 8 até 10 anos: Infantil B;
• 11 até 13 anos: Juvenil A;
• 14 até 17 anos: Juvenil B;
• Maiores de 18 anos: Adulto


"""

IdadeNadador = int(input("Digite sua idade: "))

if IdadeNadador >= 5 and IdadeNadador <= 7:
    print("Você faz parte do Infantil A")
elif IdadeNadador >= 8 and IdadeNadador <= 10:
    print("Você faz parte do Infantil B")
elif IdadeNadador >= 11 and IdadeNadador <= 13:
    print("Você faz parte do Juvenil A")
elif IdadeNadador >= 14 and IdadeNadador <= 17:
    print("Você faz parte do Juvenil B")
else:
    print("Você faz parte do grupo Adulto")
