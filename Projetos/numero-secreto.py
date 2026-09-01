
import random

def guess_number():

    secret_number = 22
    attempts = 0

    while True:
        guess = int(input("Advinhe um número entre 1 e 100: "))
        attempts += 1

        if guess > secret_number:
            print("Muito alto! Tente um número menor.")

        elif guess < secret_number:
            print("Muito baixo! Tente um número maior.")

        else:
            print(f"Parabens, você acertou o número {secret_number} em {attempts} tentativas!")
            break

    return attempts

guess_number()
    
