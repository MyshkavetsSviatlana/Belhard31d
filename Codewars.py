# 1
# In this kata you are required to, given a string, replace every letter with its position in the alphabet.
# If anything in the text isn't a letter, ignore it and don't return it.


# def alphabet_position(text: str) -> str:
#     """Replaces every letter with its position in the alphabet. Ignores any symbol that isn't a letter."""
#     letters = (
#         'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
#         'w', 'x', 'y', 'z')
#     numbers = [str(num) + ' ' for num in range(1, 27)]
#     letters_numbers = dict(zip(letters, numbers))
#     result_list = ''
#     for symbol in text.lower().replace(' ', ''):
#         if symbol.isalpha():
#             result_list += letters_numbers[symbol]
#         else:
#             continue
#     return result_list.rstrip()
#
#
# text = "The sunset sets at twelve o' clock."
# print(alphabet_position(text))


# 2
# Count the number of Duplicates
# Write a function that will return the count of distinct case-insensitive alphabetic characters and numeric
# digits that # occur more than once in the input string. The input string can be assumed to contain only
# alphabets (both uppercase and lowercase) and numeric digits.

text = 'AaaBb111234'
result1 = {key: text.lower().count(key) for key in text.lower() if text.lower().count(key) > 1}
print(len(result1))


def duplicate_count(text):
    result = {}
    for symbol in text:
        if text.lower().count(symbol) > 1:
            if symbol in result:
                result[symbol] += 1
            else:
                result[symbol] = 1
    return len(result.keys())


print(duplicate_count(text))


# 3
def how_much_i_love_you(nb_petals):
    dict_frase = {1: 'I love you',
                  2: 'a little',
                  3: 'a lot',
                  4: 'passionately',
                  5: 'madly',
                  6: "not at all"}
    if nb_petals < 7:
        return dict_frase[nb_petals]
    elif nb_petals % 6 == 0:
        return dict_frase[6]
    else:
        return dict_frase[nb_petals % 6]


print(how_much_i_love_you(444))

# 4 Given a list of notes (represented as strings) and an interval, output a list of transposed notes
# in sharp notation.
# Input notes may be represented both in flat and sharp notations (more on that below).


song = ['Db', 'F#', 'A', 'G', 'F#', 'F#', 'E', 'F#', 'D', 'G']

from itertools import repeat


def transpose(song, interval):
    sharp_notation = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#'] * 2
    flat_notation = ['A', 'Bb', 'B', 'C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab'] * 2
    song_transposed = []
    for index, note in enumerate(song):
        if note in sharp_notation:
            new_note = sharp_notation[sharp_notation.index(note) + interval]
            song_transposed.append(new_note)
        else:
            new_note = sharp_notation[flat_notation.index(note) + interval]
            song_transposed.append(new_note)
    return song_transposed


print(transpose(song, -12))

# 5 Write a function that accepts str string and key number and returns an array of integers
# representing encoded str.

from string import ascii_lowercase
from itertools import cycle
import numpy as np


def encode(message, key):
    cipher = dict(zip(tuple(ascii_lowercase), range(1, 27)))
    result = [cipher[symbol] for symbol in message]
    result_changed = []
    count = 1
    for i in cycle(str(key)):
        if count > len(result):
            break
        result_changed.append(i)
        count += 1
    result_changed = [int(i) for i in result_changed]
    return list(np.array(result) + np.array(result_changed))


message = 'masterpiece'
key = 1939
print(encode(message, key))
