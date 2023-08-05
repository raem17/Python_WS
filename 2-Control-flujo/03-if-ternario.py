""" If ternario """
edad = input("Introduce tu edad:\n=> ")
edad = int(edad)

# If tradicional
# if edad < 18:
#     print("Eres menor.")

# else:
#     print("Eres mayor de edad.")

# If ternario
mensaje = "Eres mayor de edad." if edad >= 18 else "Eres menor."

print(mensaje)
