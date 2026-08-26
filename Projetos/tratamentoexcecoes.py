# Pequeno código para exemplicar como funciona o tratamento de exceções em Python. 

try:
    numero = int(input("Digite um número: "))
    resultado = 10 / numero
except ZeroDivisionError:
    print("Erro: Não é possível dividir por zero.")
except ValueError:
    print("Erro: Você precisa digitar um número inteiro válido.")
except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")
else:
    print(f"Sucesso! O resultado é {resultado}")
finally:
    print("Fim do processo de cálculo.")