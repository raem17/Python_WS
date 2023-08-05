# pylint: disable = invalid-name
""" Métodos de strings """

animal = "  loro P   pEpe  "

# Devuelve una copia de la cadena en mayúsculas
print(animal.upper())

# Devuelve una copia de la cadena en minúsculas
print(animal.lower())

# Devuelve una copia de la cadena con el primer carácter en mayúscula y el resto en minúscula
print(animal.capitalize())

# Devuelve una copia de la cadena con la primera letra de cada palabra en mayúscula y
# el resto en minúscula. Ej: Loro Pepe
print(animal.title())

# Devuelve una copia de la cadena con los espacios del principio y el final removidos.
# Es igual al .trim() de Java
# Tiene 2 variaciones: lstrip() y rstrip()
print(animal.strip())

# Devuelve la posición/índice de la cadena de caracteres especificada. Devuelve -1 en caso de error.
print(animal.find("P"))

# Reemplaza los caracteres especificados por los nuevos.
print(animal.replace("P", "usb"))

# Devuelve un booleano si encuentra la secuencia de caracteres especificados en el string especificado.
print("P" in animal)

# Devuelve un booleano si NO encuentra la secuencia de caracteres especificados en el string especificado.
print("P" not in animal)
