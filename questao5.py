# Escreva um programa que recebe uma String e imprime uma outra String com
# os caracteres invertidos. Obrigatoriamente, nesse exercıcio, use um comando de
# repeticao (while ou for)


# Lê uma string do usuário
string_original = input("Digite uma string: ")

# Inicializa uma string vazia para armazenar o resultado invertido
string_invertida = ""

# Inicializa um contador
i = 0

# Itera sobre os caracteres da string de trás para frente
while string_original[i:]:
    i += 1

# Itera sobre os caracteres da string de trás para frente
while i > 0:
    i -= 1
    # Adiciona o caractere na posição i à string invertida
    string_invertida += string_original[i]

# Imprime a string invertida
print("String invertida:", string_invertida)
