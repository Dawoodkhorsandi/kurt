BASE57_MAPPING = '23456789abcdefghijkmnopqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ'
# some character removed for better readability (0,O,1,I,l)


class BaseNotValidException(Exception):
    """Base number should be an integer between 0 and 57"""
    def __str__(self):
        if self.args:
            return f"Base  '{self.args[0]}'.  Base number should be an integer between 0 and 57."
        else:
            return "Base number should be an integer between 0 and 57."


def encode(decimal_number, base=57):
    """
    Get an integer(model ID) and turns it to base 57

    :param decimal_number: An integer (model ID)
    :param base: An integer between 0 and 57 to determine the base
    :return: Encoded string of decimal_number
    """
    remainder_stack = []

    if base <= 0 or base > 57:
        raise BaseNotValidException(base)

    while decimal_number > 0:
        remainder = decimal_number % base
        remainder_stack.append(remainder)
        decimal_number = decimal_number // base

    mapped_string = []
    while remainder_stack:
        mapped_string.append(BASE57_MAPPING[remainder_stack.pop()])

    return ''.join(mapped_string)


def decode(value, base=57):
    """
    By default gets a base 57 encoded string and convert it to base 10
    :param value: base encoded 57 string
    :param base: base number
    :return: a decimal number
    """
    if base <= 0 or base > 57:
        raise BaseNotValidException(base)

    decimal_number = 0
    for index, char in enumerate(reversed(value)):
        number = BASE57_MAPPING.index(char)
        decimal_number += number * (base ** index)

    return decimal_number
