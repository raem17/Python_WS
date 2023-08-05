""" Bucle for """

num_buscado = 3

for num in range(5):
    print(num, num * "hola ")

    if num == num_buscado:
        print("Encontrado:", num)
        break
else:
    print("El número buscado no existe.")

# El "else" se va a ejecutar siempre que no se ejecute un "break"

print()

# Iterables
for char in "Dinamarca":
    print(char)
