""" docstring """


def eliminar_espacios(cadena: str):
    """ docstring   d"""
    cadena = cadena.strip()
    cadena_limpia = ""

    for i, char in enumerate(cadena):
        if char != " ":
            cadena_limpia += char

        elif cadena[i+1] != " ":
            cadena_limpia += char

    return cadena_limpia


sucio = "       hola         mundo       2023            "
limpio = eliminar_espacios(sucio)

print(limpio, ".")
