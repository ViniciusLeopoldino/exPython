#  Dados um numero inteiro n e uma sequencia de n numeros reais, escreva
# um algoritmo que calcula a somatoria de numeros que sao maiores que 50 e conta
# quantos numeros sao menores do que 100


# Lendo o número inteiro n
n = int(input("Digite o número de elementos na sequência: "))

# Inicializando a soma e o contador
soma_maiores_que_50 = 0
contador_menores_que_100 = 0

# Iterando sobre a sequência de n números reais
i = 0
while i < n:
    numero = float(input(f"Digite o {i+1}º número da sequência: "))

    # Verificando se o número é maior que 50
    if numero > 50:
        soma_maiores_que_50 += numero

    # Verificando se o número é menor que 100
    if numero < 100:
        contador_menores_que_100 += 1
    
    i += 1

# Exibindo a soma dos números maiores que 50
print(f"A soma dos números maiores que 50 é: {soma_maiores_que_50:.0f}")

# Exibindo a quantidade de números menores que 100
print(f"A quantidade de números menores que 100 é: {contador_menores_que_100:.0f}")
