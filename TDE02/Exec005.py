'''

Numa determinada papelaria a fotocópia custa R$0,25, caso sejam tiradas menos de 100
cópias. A partir de 100 cópias, o valor de cada fotocópia tirada cai para R$0,20. Elabore
um algoritmo que leia o número de cópias e mostre o valor a pagar pelo serviço.

'''


# Inserir o numero de copias
QuantCopias = int(input("Digite a quantidade de fotocopias: "))
ValorPg = 0

while QuantCopias <= 0:
    print("O valor nao pode ser calculado")
    QuantCopias = int(input("Digite a quantidade de fotocopias: "))

if QuantCopias > 100:
    ValorPg = QuantCopias * 0.2
    print(f"O valor total eh: {ValorPg}")

else:
    ValorPg = QuantCopias * 0.25
    print(f"O valor total eh: {ValorPg}")


