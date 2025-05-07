# exercicios sobre lists

'''
Dizemos que um número natural é triangular se ele é produto de três números naturais consecutivos.
Exemplo: 120 é triangular, pois 4.5.6 = 120. Dado um inteiro não-negativo n, verificar se n é
triangular

'''

Number = int(input("Digite um numero: "))

i = 1
t = 0

while t < Number:
    t = i*(i+1)*(i+2)
    i += 1

if t == Number:
    print("%d eh triangular" %Number)

else:
    print("%d nao eh triangular" %Number)


