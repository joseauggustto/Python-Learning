import json

filename = "userName.json"
name = ""

# Procura um arquivo de histórico
try:
    with open(filename, "r", encoding="utf-8") as r:
        # Carrega o nome do usuário do arquivo de histórico
        name = json.load(r)
except IOError:
    print("Primeiro login")

# Se o usuário foi encontrado no arquivo de histórico, dar as boas-vindas de volta
if name != "":
    print(f"Bem-vindo de volta, {name}!")
else:
    # Se o arquivo de histórico não existir, pedir o nome ao usuário
    name = input("Olá! Qual é o seu nome? ")
    print(f"Olá, {name}!")

    # Salva o nome do usuário no arquivo de histórico
    try:
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(name, f)
    except IOError:
        print("Ocorreu um problema ao gravar no arquivo de histórico.")