
# Exercicio 8

"""

Num determinado estacionamento a primeira hora custa R$ 8,00, que é o valor mínimo
praticado. Após uma hora o valor é fracionado, R$1,50 a cada 15 minutos. Elabore um
algoritmo que leia um número inteiro correspondente a quantidade de minutos usados no
estacionamento e mostre a mensagem “Valor mínimo, R$8,00” ou “Valor fracionado, R$
x”, no qual x será o valor a pagar calculado pelo algoritmo.

"""

# Entrada eh == quantidade de minutos
# const == valor minimo
# 15 * 4 = 60 ou 1 hora

ValorMinimo = 8
contador = 0

QuantMin = int(input("Digite por quantas horas pretende usar o estacionamento: "))

while QuantMin < 0:
    print("Voce nao pode ficar horas negativas")
    QuantMin = int(input("Digite por quantas horas pretende usar o estacionamento: "))


contador += QuantMin * 4
ValorPagar = ValorMinimo + contador * 1.5

print("O preco do estacionamento eh: ", ValorPagar)

