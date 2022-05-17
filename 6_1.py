# Написать функцию перевода десятичного числа в двоичное и обратно, без
# использования функции int.

# def decimal_to_binary(a: int):
#     result = []
#     c = 1
#     while len(result) < 16:
#         b = (a / c) % 2
#         b = str(int(b))
#         result.append(b)
#         c *= 2
#     return print(''.join(result[::-1]))
#
#
# print(decimal_to_binary(126))

def decimal_to_binary(a):
    sequence = []
    b = 1
    while len(sequence) < 16:
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
    return print(result[::-1])


print(decimal_to_binary(126))






