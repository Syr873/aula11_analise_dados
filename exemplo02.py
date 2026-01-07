# Bibliotecas
import os
import random


# Funçoes
def gerar_numeros(n1, n2, qtd):
    lst_num = [random.randint(n1, n2) for i in range(qtd)]
    return lst_num


# Programa
inicio = 1
final = 10
quantidade = 2
lst_numeros = gerar_numeros(inicio, final, quantidade)
print(lst_numeros)
print(lst_numeros[0])
print(lst_numeros[1])
