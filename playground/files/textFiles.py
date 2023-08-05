""" docstring """
# Leer archivo
with open("playground\\file.txt", "r", encoding="utf-8") as file:
    print(file.read())

# Escribir en archivo
with open("playground\\file.txt", "w", encoding="utf-8") as file:
    file.write("Bob\n\nEspaña")
