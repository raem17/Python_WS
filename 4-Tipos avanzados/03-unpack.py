nums = [10, 20, 30, 40, 50, 60]

# Mal
# primero = nums[0]
# segundo = nums[1]
# tercero = nums[2]

# Desempaquetar todos los elementos
# primero, segundo, tercero = nums
# print(primero, segundo, tercero)

# Desempaquetar el primer y último elemento
primero, *otros, ultimo = nums
print(primero, ultimo)
