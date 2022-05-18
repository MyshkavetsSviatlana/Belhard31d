# Написать функцию перевода десятичного числа в двоичное и обратно, без
# использования функции int.

def whole_decimal_to_binary(a):
    """Converts whole decimal number to binary. """
    if a == 0:
        return 0
    elif isinstance(a, int) or isinstance(a, float):
        sequence = []
        b = 1
        while a / b >= 1:
            sequence.append(a / b)
            b *= 2
        sequence_str = [str(i) for i in sequence]
        sequence_str_whole = [i[:i.find('.')] for i in sequence_str]
        result = ''
        for i in sequence_str_whole:
            if float(i) % 2 == 0:
                result += '0'
            else:
                result += '1'
        return result[::-1]
    else:
        print('Wrong type. Argument should be int or float.')


print(whole_decimal_to_binary(126))


def decimal_to_binary(a):
    """Converts whole or fractional decimal number to binary."""
    if a == 0:
        return 0
    elif isinstance(a, int):
        return whole_decimal_to_binary(a)
    elif isinstance(a, float):
        ind = str(a).find('.')
        d = float('0.' + str(a)[-ind:])
        sequence_float = ''
        while len(sequence_float) < 5:
            if d * 2 < 1:
                sequence_float += '0'
            else:
                sequence_float += '1'
            d = d * 2
        return whole_decimal_to_binary(a) + '.' + sequence_float


print(decimal_to_binary(1.1))


def whole_binary_to_decimal(a):
    """Converts binary numbers to decimal ones."""
    result = 0
    i = len(str(a)) - 1
    while i >= 0:
        for num in str(a):
            int_result = float(num) * (2 ** i)
            result += int_result
            i -= 1
    return result


# print(whole_binary_to_decimal(110010))


def binary_t0_decimal(a):
    if isinstance(a, float) or isinstance(a, str):
        ind = str(a).find('.')
        print(ind)
        d = '0.' + str(a)[:ind:-1]
        print(d)
    else:
        print(a)


print(binary_t0_decimal(11001110.0001110110))
