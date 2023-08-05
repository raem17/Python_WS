""" 
Si se desconoce el número de argumentos que recibirá una función,
se escribirá un * antes del nombre del parámetro.

De esta manera, la función recibirá una tupla de argumentos y 
podrá acceder a los elementos en consecuencia.
"""


def suma(*numeros):
    result = 0

    # For each en Java
    for num in numeros:
        result += num

    print(result)


def sumaCadenas(*cadenas):
    cadena_resul = ""

    for cadena in cadenas:
        cadena_resul += cadena + " "

    cadena_resul = cadena_resul.strip()

    print(cadena_resul)


suma(1, 2, 3)
suma(6, 1)

sumaCadenas("Hola", "mundo", "2023")
