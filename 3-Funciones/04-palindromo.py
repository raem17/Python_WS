def es_palindromo(cadena: str):
    cadena = cadena.strip().lower().replace(" ", "")
    cadena_reversed = ""

    for char in cadena:
        cadena_reversed = char + cadena_reversed

    return cadena == cadena_reversed


print(es_palindromo("Amo la paloma"))
print(es_palindromo("Hola mundo"))
