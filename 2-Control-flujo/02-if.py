""" If """
nota = input("Introduce tu nota:\n=> ")

try:
    nota = int(nota)
except ValueError as _e:
    print('Error:', _e)

if nota < 5:
    print("Has suspendido.")

elif nota == 5 or nota == 6:
    print("Tienes un bien.")

elif nota == 7 or nota == 8:
    print("Tienes un notable.")

elif nota == 9:
    print("Tienes un sobresaliente.")

elif nota == 10:
    print("Tienes una calificación perfecta.")

else:
    print("Nota no válida.")
