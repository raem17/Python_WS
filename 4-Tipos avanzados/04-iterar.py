paises = ["España", "Francia", "Alemania", "EEUU", "Japón"]

# Imprimir tuplas de índices y elementos
for pais in enumerate(paises):
    print(pais)

print()
# Imprimir índices
for pais in enumerate(paises):
    print(pais[0])

print()
# Imprimir elementos
for pais in enumerate(paises):
    print(pais[1])

print()
# Imprimir índices y elementos
for indice, pais in enumerate(paises):
    print(indice, pais)
