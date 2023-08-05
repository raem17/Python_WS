""" Calculadora """


def menu():
    """ Menú que calcula con dos números. """

    opc = 0
    while opc != 5:

        opc = input(
            "\nElige una opción:\n1. Sumar\n2. Restar\n3. Multiplicar\n4. Dividir\n5. Salir\n=> ")

        try:
            opc = int(opc)

        except ValueError as _e:
            print("Error:", _e)

        if opc == 1:
            num = input("Introduce el primer número: ")
            num2 = input("Introduce el segundo número: ")

            num = int(num)
            num2 = int(num2)

            print("Resultado:", (num + num2))

        elif opc == 2:
            num = input("Introduce el primer número: ")
            num2 = input("Introduce el segundo número: ")

            num = int(num)
            num2 = int(num2)

            print("Resultado:", (num - num2))

        elif opc == 3:
            num = input("Introduce el primer número: ")
            num2 = input("Introduce el segundo número: ")

            num = int(num)
            num2 = int(num2)

            print("Resultado:", (num * num2))

        elif opc == 4:
            num = input("Introduce el primer número: ")
            num2 = input("Introduce el segundo número: ")

            num = int(num)
            num2 = int(num2)

            print("Resultado:", (num / num2))

        elif opc == 5:
            print("Ha salido del menú.")
            break

        else:
            print("Opción incorrecta.")


menu()
