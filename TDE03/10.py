
# Exercicio 10

"""

Uma empresa de câmbio permite a compra de dólares, libras e euros. Elabore um
algoritmo que leia o código da moeda que o cliente quer comprar e qual o montante
que ele quer adquirir nessa moeda. Mostre então quanto ele deverá pagar em reais
para concretizar a operação. Além da cotação, a empresa cobra uma comissão de 5%
(quando o valor for menor que R$ 1.000), ou de 3% (quando maior ou igual a
R$1.000). Considere o câmbio do dia.


"""

dinerito = [6, 6.5, 7]




amount = int(input("Digite o montante em reais: "))

for i in zip(range(1,4), ['dolárzao da massa', 'euro cr7', 'libra da rainha'], strict=True):
    print(i)

x = int(input("digite o numero equivalente a moeda que voce quer comprar: "))
if x == 1:
    dinerito = amount * 6
    print("O valor em dolares eh: ",dinerito)

elif x == 2:
    dinerito = amount * 6.5
    print("O valor em euro eh: ", dinerito)

else:
    dinerito = amount * 7
    print("O valor em libras eh: ", dinerito)

if dinerito >= 1000:
    print("O valor final com a comissão de 3% é: ", dinerito * 1.03)

else:
    print("O valor final com a comissão de 5% é: ", dinerito * 1.05)

