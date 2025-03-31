"""

A partir das informações contidas na tabela abaixo, elabore um algoritmo que leia a
massa em kg de um boxeador e mostre a qual categoria ele pertence. Caso ele não se
encaixe, informe “Categoria inferior a Super-médio”. Lembrando que 1 quilograma =
2,20462262 libras (approx. 1 kg)


"""

Peso = int(input("Digite seu peso: "))

PesoLibra = Peso * 2.2

if PesoLibra < 165:
    print("Categoria inelegível")

if PesoLibra >= 165 and PesoLibra <= 168:
    print("Super-medio")
if PesoLibra >= 169 and PesoLibra <= 175:
    print("Meio-Pesado")
if PesoLibra >= 176 and PesoLibra <= 200:
    print("Meio-Pesado")
if PesoLibra >= 200 and PesoLibra <= 201:
    print("Meio-Pesado")


