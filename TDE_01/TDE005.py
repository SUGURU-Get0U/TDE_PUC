#  Faça um algoritmo que calcule o consumo médio de um automóvel (medido em
#  km/l), solicitando como entrada a distância total percorrida (KM) e o volume de
#  combustível consumido para percorre-la (litros)

DistanciaPercorrida = float(input("Digite a distancia a ser percorrida: "))
GasolinaConsumida = int(input("Digite a quantidade de combustivel consumido: "))

AverageUse = DistanciaPercorrida // GasolinaConsumida

print(f"O consumo medio eh de: {AverageUse:.2} Km/l")