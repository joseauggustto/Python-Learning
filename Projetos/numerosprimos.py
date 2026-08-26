#Desafio do canvas AWS

def primos():

    lista = []  # Cria uma lista vazia para armazenar os números primos encontrados

    for num in range(2, 251):           # Um range de numeros de 1 até 250
        eh_primo = True                 # Estou assumindo que todos são primos, até que se prove o contrário
        for divisor in range(2, num):   # Verifica se o número é divisível por algum número entre 2 e ele mesmo
            if num % divisor == 0:      # Se o resto da divisão for 0, já era, não é primo
                eh_primo = False        # Provei o contrário, não é primo
                break                   # pediu pra para, parou. Vamos para o próximo número do range inicial
        if eh_primo:                    # Se for primo, imprima está porra
            print(f"Esse {num} é primo.")
            lista.append(num)

    return lista # Retorna a lista de números primos encontrados  

resultado = primos()   # xama a função pra ela rodar 

with open("primos.txt", "w", encoding="utf-8") as arquivo:
    for num in resultado:
        arquivo.write(f"{num}\n")