""" Bucle while """

num = 1
while (num < 100):
    print(num)
    num *= 2

while True:
    cadena = input("=> ")

    if cadena.lower().strip() == "salir":
        break
