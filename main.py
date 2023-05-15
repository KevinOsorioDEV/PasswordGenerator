import random
import secrets
import string
from colorama import Fore, Style


def choiceChar(Alphabet: str, numberChar):
    letters = []
    for i in range(numberChar):
        letters.append(secrets.choice(Alphabet))
    return letters


def passworGenerator(length: int = 5):
    print(Fore.YELLOW +
          ("Este generador crea contraseñas de 12 caracteres de longitud."))

    vowels = "aeiou"
    numbers = "123456789"
    characters = "._-@#!/%&?¡"
    password = []

    try:
        if length >= 4:
            password = choiceChar(string.ascii_letters,
                                  length) + choiceChar(vowels, 1) + choiceChar(characters, 3) + choiceChar(numbers, 3)

            random.shuffle(password)

            password_string = "".join(password)

            print(Fore.GREEN +
                  f"Tu nueva contraseña es: {password_string}".center(60))
        else:
            print(Fore.BLUE + "Para una contraseña segura deber ser mayor la longitud.")

    except Exception as a:
        print(Fore.RED + f"Ingresa un número, por favor. {a}")

    print(Style.RESET_ALL)


if __name__ == "__main__":
    passworGenerator()
