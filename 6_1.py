# Написать функцию перевода десятичного числа в двоичное и обратно, без
# использования функции int.

def decimal_to_binary(a):
    """Converts decimal numbers to binary ones."""
    if a == 0:
        return 0
    elif isinstance(a, int):
        sequence = []
        b = 1
        while a/b >= 1:
            sequence.append(a/b)
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
    elif isinstance(a, float):
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
        ind = str(a).find('.')
        d = float('0.' + str(a)[-ind:])
        sequence_float = ''
        while len(sequence_float) < 5:
            if d * 2 < 1:
                sequence_float += '0'
            else:
                sequence_float += '1'
            d = d * 2
        return result[::-1] + '.' + sequence_float


print(decimal_to_binary(3))


def binary_to_decimal(a):
    """Converts binary numbers to decimal ones."""
    result = 0
    i = len(str(a)) - 1
    while i >= 0:
        for num in str(a):
            int_result = int(num) * (2 ** i)
            result += int_result
            i -= 1
    return result


print(binary_to_decimal(11))
