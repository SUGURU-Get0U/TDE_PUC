# exercicios sobre listas 04 e 05 

'''
Leia dois valores reais do teclado, calcular e imprimir na tela:
5. a) A soma destes valores b) O produto deles c) O quociente entre eles

'''

ValueKeeper = []

for cr7 in range(0,2):
    cr7 = float(input("Enter a value: "))
    ValueKeeper.append(cr7)
# sum of these values
ValueAdd = sum(ValueKeeper)

# Their multiplying result
Value_M_Result = ValueKeeper[0] * ValueKeeper[1]

# Their dividing result
Value_D_Result = ValueKeeper[0] / ValueKeeper[1]

print(f"the sum is {ValueAdd}")
print(f"The multiplying value is {Value_M_Result}")
print(f"The dividing value is {Value_D_Result}")
