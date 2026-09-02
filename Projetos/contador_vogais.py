
def count_and_reverse():

    text = input("Digite uma palavra ou frase: ").lower()

    vogais = "aeiou"
    count = 0
    reversed_text = ""

    for char in text:
        if char in vogais:
            count += 1

    for char in text:
        reversed_text = char + reversed_text

    return (f"Total de vogais: {count}\n"
            f"Texto invertido: {reversed_text}\n")

print(count_and_reverse())