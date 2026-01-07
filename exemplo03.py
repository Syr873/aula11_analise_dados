# Bibliotecas
import os
import random


# Funçoes
def gerar_numeros(n1, n2, qtd):
    lst_num = [random.randint(n1, n2) for i in range(qtd)]
    return lst_num

def soma(lst_soma):
    valor = 0
    for i in lst_soma:
        valor += i
    return valor

def subtracao(lst_sub):
    sub = lst_sub[0]
    for i  in lst_sub[1:]:
        sub -= i
    return sub

def multiplicaçao(lst_multi):
    mult = 1
    for i in lst_multi:
        mult *= i
    return mult

def divisao(lst_divi):
    divi = lst_divi[0]
    for i in lst_divi[1:]:
        divi /= i
    return divi


# Programa
inicio = int(input('Informe o inicio: '))
fim = int(input('Informe o fim: '))
quantidade = int(input('Informe a quantidade: '))

lst_numeros = gerar_numeros(inicio, fim, quantidade)
soma_total = soma(lst_numeros)
subtracao_total = subtracao(lst_numeros)
multi_total = multiplicaçao(lst_numeros)
divi_total = divisao(lst_numeros)

os.system('cls')
print(lst_numeros)
print(soma_total)
print(subtracao_total)
print(multi_total)
print(divi_total)
