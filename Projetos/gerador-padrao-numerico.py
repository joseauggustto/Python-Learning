#here we go again

def number_pattern(n):


    if not isinstance(n, int):
        return "Argument must be an integer value."

    elif n < 1:
        return "Argument must be an integer greater than 0."


    resultado = []

    for i in range(1, n + 1):
        resultado.append(str(i))   #essa bagunça pode ser escrita assim --> return " ".join(str(i) for i in range(1, n + 1))

    finalli = " ".join(resultado)

    return finalli    


print(number_pattern(5))

