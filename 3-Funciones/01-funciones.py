""" Funciones """


def print_string(nombre: str, apellidos="Smith"):
    # (nombre, cont, apellidos) = Parámetros
    # Se pueden declarar parámetros opcionales,
    # estos van a tener un valor predefinido a menos que se reciba un argumento

    print(f"Hola {nombre} {apellidos}")


# ("Peter") = Argumento
print_string("Peter")  # El apellido será Smith
print_string("Peter", "Parker")  # El apellido será Parker
