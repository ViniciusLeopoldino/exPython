#  Uma fabrica pretende aumentar o preco de seus produtos, porem precisa saber
# qual sera o maior aumento em R$ e qual o maior aumento em percentual. Sua
# tarefa e escrever um algoritmo que le a quantidade n de produtos que a empresa
# deseja aumentar, para cada produto o usuario devera informar dois numeros reais
# para cada produto, o primeiro eh o preco atual e o segundo eh o preco reajustado. Seu
# algoritmo devera mostrar o maior aumento percentual e o maior aumento em reais
# (R$) entre os n produtos. Observe que o maior aumento percentual pode nao ser,
# necessariamente, o maior aumento em reais. Por exemplo, um produto passou de
# 0,50 para 1,00 que gerou um aumento percentual de 100% porem o aumento em R$
# foi de 0,50. Ja um outro produto passou de 20,00 para 22,00 um aumento percentual
# de 10% mas aumentou R$ 2,00.


# Inicializando as variáveis para armazenar o maior aumento em reais e o maior aumento percentual
maior_aumento_reais = 0
maior_aumento_percentual = 0

# Lendo a quantidade de produtos
n = int(input("Digite a quantidade de produtos: "))

# Inicializando um contador para os produtos
contador = 1

# Iterando sobre cada produto
while contador <= n:
    # Lendo o preço atual e o preço reajustado do produto
    preco_atual = float(input(f"Digite o preço atual do produto {contador}: "))
    preco_reajustado = float(input(f"Digite o preço reajustado do produto {contador}: "))

    # Calculando o aumento em reais
    aumento_reais = preco_reajustado - preco_atual

    # Calculando o aumento percentual
    aumento_percentual = (aumento_reais / preco_atual) * 100

    # Verificando se este aumento é o maior em reais
    if aumento_reais > maior_aumento_reais:
        maior_aumento_reais = aumento_reais

    # Verificando se este aumento é o maior em percentual
    if aumento_percentual > maior_aumento_percentual:
        maior_aumento_percentual = aumento_percentual

    contador += 1

# Exibindo o maior aumento em reais e o maior aumento percentual
print(f"O maior aumento em reais é de R$ {maior_aumento_reais:.2f}")
print(f"O maior aumento percentual é de {maior_aumento_percentual:.2f}%")
