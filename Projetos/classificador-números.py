# Função pricipal que classifica os números em pares e ímpares. 

def classificar_numeros(numeros):
    pares = []
    impares = []

    for numero in numeros:
        if numero % 2 == 0:
            pares.append(numero)
        else:
            impares.append(numero)

    return (
        f"Numeros pares: {pares}\n"
        f"Numeros impares: {impares}\n"
        )

# Coleta de dados: 

entrada = input("Digite uma sequência de números inteiros separados por espaço: ").split()

# Converte a entrada em uma lista de inteiros

lista_numeros = [int(num) for num in entrada]

print(classificar_numeros(lista_numeros))