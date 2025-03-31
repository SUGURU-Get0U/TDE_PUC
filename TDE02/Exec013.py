"""
Numa determinada loja de eletrodomésticos, os produtos podem ser adquiridos da
seguinte forma:

Elabore um algoritmo que leia a opção do cliente e o preço de tabela do produto, mostrando
então o valor calculado conforme a condição escolhida.


"""

valor_Produto = int(input("Digite o valor do produto: "))

Valor_A_Vista = round(valor_Produto * 0.8, 2)
ValorParcela2x = round((valor_Produto * 4) / 2, 2)
ValorParcela3x = round((valor_Produto / 3))
ValorParcela4x = round((valor_Produto / 4) * 1.04, 1)

print(f"O valor com 8% de desconto e de: R$ {Valor_A_Vista:.1f}");
print(f"O valor do produto parcelado em 2x com 4% de desconto e de: R$ {ValorParcela2x:.2f}");
print(f"O valor com sem desconto parcelado em 3x R$ {ValorParcela3x:.2f}");
print(f"O valor com 4% de acréscimo e parcelado em 4x e de: R$ {ValorParcela4x:.2f}")