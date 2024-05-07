# Problema da troca de dinheiro, suponha que queremos trocar o valor de uma
# cedula x por moedas nos valores a e b. Sua tarefa neste exercıcio e ler os valores x,
# a e b e imprimir se e possıvel ou nao efetuar a troca. Na situacao que seja possıvel,
# imprima a quantidade de moedas de cada um dos valores necessarias para efetuar a
# troca.


# Lendo os valores de x, a e b
x = int(input("Digite o valor da cédula: "))
a = int(input("Digite o valor da primeira moeda: "))
b = int(input("Digite o valor da segunda moeda: "))

# Variáveis para armazenar a quantidade de moedas de cada valor
quantidade_a = 0
quantidade_b = 0

# Verificando se é possível efetuar a troca
possivel = False
i = 0
while i * a <= x:
    j = 0
    while i * a + j * b <= x:
        if i * a + j * b == x:
            possivel = True
            quantidade_a = i
            quantidade_b = j
            break
        j += 1
    if possivel:
        break
    i += 1

# Imprimindo o resultado
if possivel:
    print("É possível efetuar a troca.")
    print(f"Quantidade de moedas de {a}: {quantidade_a}")
    print(f"Quantidade de moedas de {b}: {quantidade_b}")
else:
    print("Não é possível efetuar a troca.")
