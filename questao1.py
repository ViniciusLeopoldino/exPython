# 1. (2.0) Escreva um programa que le um numero inteiro n positivo, e uma sequencia
# de n numeros inteiros, calcula e imprime quantos segmentos de numeros iguais
# consecutivos compoem essa sequencia. 


# Solicita ao usuário que insira o número de elementos na sequência e converte para inteiro
n = int(input("Digite o número de elementos na sequência: "))

# Solicita ao usuário que insira a sequência de números separados por espaço, e os divide em uma lista
sequencia = input("Digite a sequência de números separados por espaço: ").split()

# Verifica se o número de elementos na sequência é zero
if n == 0:
    # Se for zero, imprime que o número de segmentos de números iguais consecutivos é zero
    print("O número de segmentos de números iguais consecutivos é: 0")
else:
    # Se não for zero, inicializa a variável 'segmentos' com 1, pois há pelo menos um segmento
    segmentos = 1
    # Inicializa a variável 'anterior' com o primeiro elemento da sequência
    anterior = sequencia[0]
    # Itera sobre os elementos da sequência, começando do segundo elemento
    for elemento in sequencia[1:]:
        # Verifica se o elemento atual é diferente do elemento anterior
        if elemento != anterior:
            # Se for diferente, incrementa o número de segmentos e atualiza o elemento anterior
            segmentos += 1
            anterior = elemento

    # Imprime o número de segmentos de números iguais consecutivos
    print("O número de segmentos de números iguais consecutivos é:", segmentos)
