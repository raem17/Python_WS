"""
Si se desconoce el número de argumentos de clave-valor, 
se agrega ** antes del nombre del parámetro.

De esta forma, la función recibirá un diccionario de argumentos y 
podrá acceder a los elementos en consecuencia:
"""


def my_function(**persona):
    print("Su DNI es: " + persona["dni"])


my_function(dni="12345D", nom="Pepe", ape="Viyuela")
