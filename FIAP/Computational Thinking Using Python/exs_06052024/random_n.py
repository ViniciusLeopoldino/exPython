#Escreva uma função que recebe como parametro um n inteiro positivo e retorna uma lista com n numeros aleatorios entre 1 e 1000

import random

def cria_vetor(quantidade):
    list = []
    for x in range(quantidade):
        list.append(random.randint(1, 1000))
    return list

lista = cria_vetor(100)
print(lista)