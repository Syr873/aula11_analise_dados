# Bibliotecas
import random

n = random.randint(1, 10)
m = random.randint(1, 10)

# print(n, m)

# ------------------------------------------------------------

# Gerar numeros decimais
n_decimal = random.uniform(1, 10)
numero_decimal = round(n_decimal, 1) # Arredonda
# print(f'{n_decimal:.2f}') # Formata
# print(numero_decimal)

# ------------------------------------------------------------

# Gerar numeros aleatorios dentro de uma lista
lst_numeros = [random.randint(1, 10) for num in range(5)]
print(lst_numeros)