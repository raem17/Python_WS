# pylint: disable = invalid-name
""" Strings """

nombre = "Alfredo"
descripcion = """
Esto es una simple
descripcion de prueba.
"""

# print(nombre, descripcion)

# Len: Función que devuelve el número de items que forman la cadena. Resultado: 7
print(len(nombre))

# Devolver al índice indicado de una cadena. Resultado: A
print(nombre[0])

# Devolver el rango de índices indicado de una cadena. Resultado: Alf
print(nombre[0:3])

# Devolver el conjunto de índices desde la posición indicada de una cadena. Resultado: do
print(nombre[5:])

# Devolver el conjunto de índices hasta la posición indicada de una cadena. Resultado: Alf
print(nombre[:3])
