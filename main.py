import time
import random
import secrets
import string


def choiceChar(Alphabet: str, numberChar):
    letters = []
    for i in range(numberChar):
        letters.append(secrets.choice(Alphabet))
    return letters


def passworGenerator(length: int = 4):
    print("Este generador crea contraseña de 8 caracteres de longitud.")

    vowels = "aeiou"
    numbers = "123456789"
    characters = "._-@#!/%&?¡"
    password = []

    try:
        if length >= 4:
            password = choiceChar(string.ascii_letters,
                                  length) + choiceChar(vowels, 3) + choiceChar(characters, 3) + choiceChar(numbers, 3)

            random.shuffle(password)

            password_string = "".join(password)

            print(f"Tu nueva contraseña es: {password_string}")
        else:
            print("Para una contraseña segura deber ser mayor la longitud.")

    except Exception as a:
        print(f"Ingresa un número, por favor. {a}")


if __name__ == "__main__":
    passworGenerator()
