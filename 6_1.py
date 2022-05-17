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

# def decimal_to_binary(a):
#     if a == 0:
#         return 0
#     else:
#         sequence = []
#         b = 1
#         while a/b >= 1:
#             sequence.append(a/b)
#             b *= 2
#         sequence_str = [str(i) for i in sequence]
#         sequence_str_whole = [i[:i.find('.')] for i in sequence_str]
#         result = ''
#         for i in sequence_str_whole:
#             if float(i) % 2 == 0:
#                 result += '0'
#             else:
#                 result += '1'
#         return result[::-1]
#
#
# print(decimal_to_binary(2))

def decimal_to_binary(a):
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


print(decimal_to_binary(3.3))






