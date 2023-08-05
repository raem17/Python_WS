""" Operadores lógicos 2 """
# and,or not
# &&, ||, != (En Java)

sabeGit = True
sabeJava = True
sabePython = False
mensaje = ""

# if sabeGit and (sabeJava or sabePython):
#     mensaje = "Puedes trabajar."

# else:
#     mensaje = "No puedes trabajar."

# print(mensaje)

if not sabeGit and not sabeJava and not sabePython:
    mensaje = "No sabes nada."

elif not sabeGit and (sabeJava or sabePython):
    mensaje = "Por lo menos sabes programar."

elif sabeGit and sabeJava and sabePython:
    mensaje = "Sabes hacer todo."

elif sabeGit and (sabeJava or sabePython):
    mensaje = "Puedes trabajar."

else:
    mensaje = "Sólo sabes Git."

print(mensaje)
