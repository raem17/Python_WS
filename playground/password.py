""" Programa en Python que genera contraseñas seguras de forma aleatoria. """
import string
import random


def menu():
    """ Imprime por pantalla el menú de opciones. """
    print(f"\n{'*' * 100}")
    print("""Elija una opción para generar una contraseña segura:\n
1. Generar una contraseña de 25 caracteres formada por 5 minúsculas, 5 mayúsculas, 8 números y 7 símbolos.
2. Generar una contraseña personalizada. Debe estar formada por al menos 5 caracteres.
3. Salir del programa.

Consejo: Para generar una contraseña segura de forma rápida se recomienda escoger la 1ª opción.""")
    print(f"{'*' * 100}")


def generar_pw_25():
    """ Devuelve una contraseña de 25 caracteres formada por 5 minúsculas, 
    5 mayúsculas, 8 números y 7 símbolos. """

    lower_letters = string.ascii_lowercase
    upper_letters = string.ascii_uppercase
    numbers = string.digits
    symbols = "!@#$%^&*.()"

    pw_list = random.sample(lower_letters, 5) + random.sample(upper_letters, 5) + \
        random.sample(numbers, 8) + random.sample(symbols, 7)

    random.shuffle(pw_list)

    pw_string = ''.join(pw_list)

    return pw_string


def generar_pw_custom(n_ll: int, n_ul: int, n_nums: int, n_sym: int):
    """ Devuelve una contraseña formada por (n_ll) letras minúsculas, (n_ul) letras mayúsculas, 
    (n_nums) números y (n_sym) símbolos. """

    lower_letters = string.ascii_lowercase
    upper_letters = string.ascii_uppercase
    numbers = string.digits
    symbols = "!@#$%^&*.()"

    pw_list = random.sample(lower_letters, n_ll) + random.sample(upper_letters, n_ul) + \
        random.sample(numbers, n_nums) + random.sample(symbols, n_sym)

    random.shuffle(pw_list)

    pw_string = ''.join(pw_list)

    return pw_string


# Main

opc = -1
while opc != 3:
    menu()
    opc = int(input("\n=> ").strip())

    if opc == 1:
        print(f"\nContraseña generada: {generar_pw_25()}")

    elif opc == 2:
        ll = int(
            input("¿Cuántas letras minúsculas desea tener? Máx: 26.\n=> ").strip())

        ul = int(
            input("¿Cuántas letras mayúsculas desea tener? Máx: 26.\n=> ").strip())

        nums = int(input("¿Cuántos números desea tener? Máx: 10.\n=> ").strip())

        sym = int(input("¿Cuántas símbolos desea tener? Máx: 11.\n=> ").strip())

        total = ll + ul + nums + sym

        if total > 4:
            if ll <= 26 and ul <= 26 and nums <= 10 and sym <= 21:
                print(
                    f"\nContraseña generada: {generar_pw_custom(ll, ul, nums, sym)}")

            else:
                print("\n¡Ha introducido un número excesivo de minúsculas, mayúsculas, números o símbolos!. Se le devolverá al menú principal.")

        else:
            print("\n¡La contraseña debe estar formada por al menos 5 caracteres!. Se le devolverá al menú principal.")

    elif opc == 3:
        print("\nHa salido del programa.")

    else:
        print("\nAVISO: ¡Introduzca una opción válida!")
