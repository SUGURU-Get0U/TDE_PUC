"""

O IMC (Índice de Massa Corporal) é calculado através da seguinte fórmula:
IMC = massa / altura2
Elabore um algoritmo que leia a massa (em quilogramas) e a altura (em metros) do usuário
e mostre o valor do IMC e se ele está na faixa considerada “normal” segundo o critério
apresentado na tabela da OMS (Organização Mundial de Saúde): 18,5 ≤ IMC< 25. Caso
não esteja, calcule a sua massa máxima considerada normal (usando IMC igual a 24,9).

"""

Comeco = input("Voce deseja comecar o calculo do imc? [s/n]: ")

while Comeco == int or float:
    print("EH uma pergunta de sim ou nao :(")
    Comeco = input("Voce deseja comecar o calculo do imc? [s/n]: ")


    while Comeco == 's':
        EnterMassa = float(input("Coloque seu peso para calculo do IMC: "))
        EnterAltura = float(input("Coloque sua altura para calculo do IMC: "))

        IMC = EnterMassa / (EnterAltura * EnterAltura)

        if IMC >= 18.5:
            if IMC < 25:
                print("Tudo dentro do normal pela OMS")

        else:
            IMC = 24.9
            MaxMASS = IMC / (EnterAltura * EnterAltura)
            print(f"A sua massa maxima eh: {MaxMASS: .2f}")

    Comeco = input("Voce deseja continuar? [s/n]: ")
print("OK!")