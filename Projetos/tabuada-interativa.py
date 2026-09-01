
def tabuada(numero):
    
    while True:
        
        numero = int(input("Digite um número inteiro entre 1 e 10: "))

        if 1 <= numero <= 10:
            break
        else:
            print("Valor inválido, tente novamente.")  

    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")

    return numero  

tabuada(0) 