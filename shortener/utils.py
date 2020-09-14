BASE62_MAPPING = '23456789abcdefghijkmnopqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ'
# some character removed for better readability (0,O,1,I,l)


def encode(decimal_number, base=57):
    remainder_stack = []

    if base <= 0 or base > 62:
        return 0  # return appropriate exception

    while decimal_number > 0:
        remainder = decimal_number % base
        remainder_stack.append(remainder)
        decimal_number = decimal_number // base

    mapped_string = []
    while remainder_stack:
        mapped_string.append(BASE62_MAPPING[remainder_stack.pop()])

    return ''.join(mapped_string)


def decode(value, base=57):
    if base <= 0 or base > 62:
        return 0  # return appropriate exception

    decimal_number = 0
    for index, char in enumerate(reversed(value)):
        number = BASE62_MAPPING.index(char)
        decimal_number += number * (base ** index)

    return decimal_number
