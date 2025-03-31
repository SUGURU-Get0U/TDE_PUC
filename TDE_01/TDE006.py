#  Faça um algoritmo que calcule a quantidade de latas de tintas necessárias para pintar
#  um tanque cilindro, em que são fornecidas a sua altura e raio, sabendo que:
#   a. A lata de tinta custa R$50,00
#   b. Cada lata contém 5 litros
#   c. Cada litro de tinta pinta 3 metros quadrados
#   d. Entrada do programa: altura e raio do cilindro
#   e. Saída: valor em reais e quantidade de latas


ShapeHeight = int(input("Digite a altura do cilindro: "))
ShapeRadius = int(input("Digite o raio do cilindro: "))

LatArea = 2 * 3 * ShapeHeight * ShapeRadius
BaseArea = 3 * ShapeRadius ^ 2

ShapeTotalArea = LatArea + 2 * BaseArea

BucketAmount = ShapeTotalArea // 15

TotalValue = BucketAmount * 50

print("O valor total a ser pago eh de: R$",TotalValue)
print("A quantidade de latas utilizadas foi de:", BucketAmount )
