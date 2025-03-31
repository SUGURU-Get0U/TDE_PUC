# Faça um algoritmo que recebe o valor de um produto e calcule os seguintes valores:
# (1) a vista com 5% de desconto; (2) o valor da parcela em 2x; (3) o valor da parcela
# em 3x com acréscimo de 5%

valorProduto = int(input("Digite o valor do produto: "))

ValorDesconto = round(valorProduto * 0.95, 2)
ValorParcela2x = round(valorProduto / 2, 2)
ValorParcela3x = round((valorProduto / 2) * 1.05, 1)

print(f"O valor com 5% de desconto e de: R$ {ValorDesconto:.1f}")
print(f"O valor do produto parcelado em 2x e de: R$ {ValorParcela2x:.2f}")
print(f"O valor com um acréscimo de 5%, parcelado em 2x eh de: R$ {ValorParcela3x:.2f}")


