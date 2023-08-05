""" Hallar números duplicados """


def existe_num(duplicated_nums: list[int], number: int):
    """ docstring """
    existe = False

    for num in duplicated_nums:
        if num == number:
            existe = True

            break

    return existe


def find_duplicate_nums(numbers: list[int]):
    """ docstring """
    nums_repetidos = []

    for num_i in numbers:
        cont = 0

        for num_j in numbers:
            if num_i == num_j:
                cont += 1

        if cont > 1:
            if not existe_num(nums_repetidos, num_i):
                nums_repetidos.append(num_i)

    return nums_repetidos


nums = [6, 9, 1, 6, 8, 3, 9, 1, 1, 4, 5, 9, 3, 4, 5, 7, 11, 44, 22, 13, 8]
dupli_nums = find_duplicate_nums(nums)
dupli_nums.sort()

print(dupli_nums)
