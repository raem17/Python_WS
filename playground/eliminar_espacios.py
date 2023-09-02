""" docstring """


def eliminar_espacios(cadena: str):
    """ docstring """
    cadena = cadena.strip()
    cadena_limpia = ""

    for i, char in enumerate(cadena):
        if char != " ":
            cadena_limpia += char

        elif cadena[i+1] != " ":
            cadena_limpia += char

    return cadena_limpia


sucia = "       hola         mundo       2023            "
limpia = eliminar_espacios(sucia)

print(f"[{limpia}]")
