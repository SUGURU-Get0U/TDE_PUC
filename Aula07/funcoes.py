'''

Exercicios que necessitam de funções.

Funçõe nos permitem "quebrar" um problema complexo em sub-partes
mais simples

-> Permite reutilizar o código
    -> Ex: calcular o troco de 100 faturas diferentes

'''
from random import randint

# função para calcular o troco

def troco(vFatura, vPago):
    resto = vPago - vFatura
    return resto  

def getPreco():
    for i in range(1,100):
        precoPagar = randint(1,299)
        print(f"o valor a pagar é: {precoPagar}")
        meuDinheiro = randint(2,301)
        while meuDinheiro < precoPagar:
            meuDinheiro = randint(2,301)
        print(f"O valor a pagar é {precoPagar}, voce deu {meuDinheiro}, sobram {troco(precoPagar, meuDinheiro)} reais")
        

getPreco()
troco()   