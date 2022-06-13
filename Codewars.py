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

# text = 'AaaBb111234'
# result1 = {key: text.lower().count(key) for key in text.lower() if text.lower().count(key) > 1}
# print(len(result1))
#
#
# def duplicate_count(text):
#     result = {}
#     for symbol in text:
#         if text.lower().count(symbol) > 1:
#             if symbol in result:
#                 result[symbol] += 1
#             else:
#                 result[symbol] = 1
#     return len(result.keys())
#
#
# print(duplicate_count(text))
#
#
# # 3
# def how_much_i_love_you(nb_petals):
#     dict_frase = {1: 'I love you',
#                   2: 'a little',
#                   3: 'a lot',
#                   4: 'passionately',
#                   5: 'madly',
#                   6: "not at all"}
#     if nb_petals < 7:
#         return dict_frase[nb_petals]
#     elif nb_petals % 6 == 0:
#         return dict_frase[6]
#     else:
#         return dict_frase[nb_petals % 6]
#
#
# print(how_much_i_love_you(444))
#
# 4 Given a list of notes (represented as strings) and an interval, output a list of transposed notes
# in sharp notation.
# Input notes may be represented both in flat and sharp notations (more on that below).


# song = ['Db', 'F#', 'A', 'G', 'F#', 'F#', 'E', 'F#', 'D', 'G']

# from itertools import repeat


# def transpose(song, interval):
#     sharp_notation = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#'] * 2
#     flat_notation = ['A', 'Bb', 'B', 'C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab'] * 2
#     song_transposed = []
#     for index, note in enumerate(song):
#         if note in sharp_notation:
#             new_note = sharp_notation[sharp_notation.index(note) + interval]
#             song_transposed.append(new_note)
#         else:
#             new_note = sharp_notation[flat_notation.index(note) + interval]
#             song_transposed.append(new_note)
#     return song_transposed
#
#
# print(transpose(song, -12))

# 5 Write a function that accepts str string and key number and returns an array of integers
# representing encoded str.
#
# from string import ascii_lowercase
# from itertools import cycle
# import numpy as np
#

# def encode(message, key):
#     cipher = dict(zip(tuple(ascii_lowercase), range(1, 27)))
#     result = [cipher[symbol] for symbol in message]
#     result_changed = []
#     count = 1
#     for i in cycle(str(key)):
#         if count > len(result):
#             break
#         result_changed.append(i)
#         count += 1
#     result_changed = [int(i) for i in result_changed]
#     return list(np.array(result) + np.array(result_changed))


# message = 'masterpiece'
# key = 1939
# print(encode(message, key))


#  6 A Narcissistic Number is a number of length l in which the sum of its digits to the power of l
# is equal to the original number. If this seems confusing, refer to the example below.
# Ex: 153, where l = 3 (the number of digits in 153)
# 1**3 + 5**3 + 3**3 = 153


# def is_narcissistic(i):
#     res = sum([int(num) ** len(str(i)) for num in str(i)])
#     return True if res == i else False
#
#
# print(is_narcissistic(258))


# 7 Given an array of integers, find the one that appears an odd number of times.
# There will always be only one integer that appears an odd number of times.


# def find_it(seq):
#     for i in seq:
#         if seq.count(i) % 2:
#             return i
#
#
# seq = [1, 2, 2, 3, 3, 3, 4, 3, 3, 3, 2, 2, 1]
# print(find_it(seq))


# 8 You are given an unsorted array containing all the integers from 0 to 100 inclusively.
# However, one number is missing. Write a function to find and return this number.
# What are the time and space complexities of your solution?


# def missing_no(nums):
#     ind = 0
#     nums1 = sorted(nums)
#     for num in nums1:
#         if num + 1 == nums[ind + 1]:
#             ind += 1
#         else:
#             return num + 1
#
#
# nums = list(range(0, 101))
# nums.remove(5)
# print(nums)
# print(missing_no(nums))


# def missing_no(nums):
#     return tuple(set(range(0, 101)) - set(nums))[0]
#
#
# nums = list(range(0, 101))
# nums.remove(78)
# print(missing_no(nums))
#

# 9. Remove words from the sentence if they contain exactly one exclamation mark.
# Words are separated by a single space, without leading/trailing spaces.

# def remove(s):
#     s = [word for word in s.split(' ') if word.count('!') != 1]
#     return ', '.join(s).replace(',', '')
#
#
# s = "!Hi! ! !Hi!"
# print(remove(s))

# 10. Count the number of divisors of a positive integer n.

# def divisors(n):
#     count = 1
#     divisors = []
#     while count <= n:
#         if n % count == 0:
#             divisors.append(count)
#         count += 1
#     return len(divisors)
#
#
# n = 30
# print(divisors(n))


# 11. Given a string of words (x), you need to return an array of the words, sorted alphabetically
# by the final character in each.
# If two words have the same last letter, they returned array should show them in the order they appeared
# in the given string.


# def last(s):
#     lst = [word[::-1] for word in s.split(' ')]
#     dct = {word[0]: [word for word in lst] for word in lst}
#     for key, value in dct.items():
#         for word in lst:
#             if word[0] != key:
#                 value.remove(word)
#     result0 = []
#     for item in sorted(list(dct.values())):
#         for word in item:
#             result0.append(word)
#     result = [word[::-1] for word in result0]
#     return result
#
#
# s = "what time are we climbing up the volcano"
# print(last(s))
# print(s.split(' '))


# 12. Three semicircles are drawn on AB, AD, and AF. Here CD is perpendicular to AB and EF is perpendicular to AD.
# Task. Given the radius of the semicircle ADBCA, find out the area of the lune AGFHA (the shaded area).

#
# def blood_moon(r):
#     result = (r ** 2) / 4
#     return result


# 13. Create a function that returns the sum of the two lowest positive numbers
# given an array of minimum 4 positive integers. No floats or non-positive integers will be passed.


# def sum_two_smallest_numbers(numbers):
#     min1 = min(numbers)
#     numbers.remove(min1)
#     min2 = min(numbers)
#     return min1 + min2
#
#
# numbers = [10, 343445353, 3453445, 3453545353453]
# print(sum_two_smallest_numbers(numbers))


# 14. You are given a list of unique integers arr, and two integers a and b.
# Your task is to find out whether or not a and b appear consecutively in arr,
# and return a boolean value (True if a and b are consecutive, False otherwise).


# def consecutive(arr, a, b):
#     return arr.index(b) == arr.index(a) + 1 or arr.index(a) == arr.index(b) + 1
#
#
# arr = [1, 3, 5, 7]
# a = 3
# b = 1
# print(consecutive(arr, a, b))


# 15 Return the number (count) of vowels in the given string.
# We will consider a, e, i, o, u as vowels for this Kata (but not y).
# The input string will only consist of lower case letters and/or spaces.

# def get_count(sentence):
#     lst = ['a', 'e', 'i', 'o', 'u']
#     result = 0
#     for s in sentence:
#         if s in lst:
#             result += 1
#     return result
#
#
# sentence = ""
# print(get_count(sentence))


# 16. In this kata, you are asked to square every digit of a number and concatenate them.
# For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1.
# Note: The function accepts an integer and returns an integer


# def square_digits(num):
#     result0 = []
#     for digit in str(num):
#         sq = int(digit) ** 2
#         result0.append(sq)
#     result = ''
#     for item in result0:
#         result = result + str(item)
#     return int(result)
#
#
# num = 0
# print(square_digits(num))


# 17. Trolls are attacking your comment section!
# A common way to deal with this situation is to remove all of the vowels from the trolls' comments,
# neutralizing the threat. A common way to deal with this situation is to remove all of the vowels
# from the trolls' comments, neutralizing the threat. Your task is to write a function that takes a string
# and return a new string with all vowels removed. Note: for this kata y isn't considered a vowel.


# def disemvowel(string_):
#     vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
#     string = ''
#     for s in string_:
#         if s not in vowels:
#             string += s
#     return string
#
#
# string_ = "This website is for losers LOL!"
# print(disemvowel(string_))


# 18. You are given a string of space separated numbers, and have to return the highest and lowest number.

# def high_and_low(numbers):
#     lst = [int(d) for d in numbers.split(' ')]
#     result = f"{max(lst)} {min(lst)}"
#     return result
#
#
# numbers = "8 3 -5 42 -1 0 0 -9 4 7 4 -4"
# print(high_and_low(numbers))


# 19. The examples below show you how to write function accum:
# accum("abcd") -> "A-Bb-Ccc-Dddd"


# def accum(s):
#     result = ''
#     ind = 1
#     for i in s:
#         if ind == 1:
#             result += i.upper()
#             result += '-'
#             ind += 1
#         else:
#             result += i.upper()
#             result += i.lower()*(ind-1)
#             result += '-'
#             ind += 1
#     return result[:-1]
#
#
# s = "ZpglnRxqenU"
# print(accum(s))


# 20. Your task is to make a function that can take any non-negative integer as an argument
# and return it with its digits in descending order. Essentially, rearrange the digits to create
# the highest possible number.


# def descending_order(num):
#     lst = sorted([int(n) for n in str(num)], reverse=True)
#     result = ''
#     for i in lst:
#         result += str(i)
#     return int(result)
#
#
# num = 145263
# print(descending_order(num))


# 21. Digital root is the recursive sum of all the digits in a number.
# Given n, take the sum of the digits of n. If that value has more than one digit,
# continue reducing in this way until a single-digit number is produced. The input will be a non-negative integer.


# def digital_root(n):
#     lst = [int(d) for d in str(n)]
#     result = sum(lst)
#     while result > 9:
#         result = sum(int(d) for d in str(result))
#     return result
#
#
# n = 16
# print(digital_root(n))


# 22. If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
# The sum of these multiples is 23.
# Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.
# Additionally, if the number is negative, return 0 (for languages that do have them).
# Note: If the number is a multiple of both 3 and 5, only count it once.


# def solution(number):
#     return sum([i for i in range(1, number) if i % 3 == 0 or i % 5 == 0])
#
#
# number = 45
# print(solution(number))


# 23. Write a function that takes in a string of one or more words, and returns the same string,
# but with all five or more letter words reversed (Just like the name of this Kata). Strings passed
# in will consist of only letters and spaces. Spaces will be included only when more than one word is present.
# Examples: spinWords( "Hey fellow warriors" ) => returns "Hey wollef sroirraw" spinWords( "This is a test") =>
# returns "This is a test" spinWords( "This is another test" )=> returns "This is rehtona test"


# def spin_words(sentence):
#     result = []
#     for word in sentence.split(' '):
#         if len(word) < 5:
#             result.append(word)
#         else:
#             result.append(word[::-1])
#     return ','.join(result).replace(',', ' ')
#
#
# sentence = "Hey fellow warriors"
# print(spin_words(sentence))


# 24. Write a function, persistence, that takes in a positive parameter num and returns
# its multiplicative persistence, which is the number of times you must multiply the digits
# in num until you reach a single digit.


# from numpy import cumprod
#
#
# def persistence(n):
#     production = []
#     result = 1
#     for d in [int(d) for d in str(n)]:
#         result *= d
#     production.append(result)
#     if len(str(n)) == 1:
#         return 0
#     else:
#         while result > 9:
#             res = cumprod([int(d) for d in str(result)])[-1]
#             result = res
#             production.append(result)
#     return len(production)
#
#
# n = 4
# print(persistence(n))


# 25. Your task is to sort a given string. Each word in the string will contain a single number.
# This number is the position the word should have in the result.
# Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).
# If the input string is empty, return an empty string. The words in the input String will only contain
# valid consecutive numbers.


# def order(sentence):
#     lst = [word for word in sentence.split(' ')]
#     lst1 = [ind for ind in range(1, len(lst)+1)]
#     lst2 = []
#     for ind in lst1:
#         for word in lst:
#             if str(ind) in word:
#                 lst2.append(word)
#     result = ''
#     for item in lst2:
#         result += item
#         result += ' '
#     return result.rstrip()
#
#
# sentence = "4of Fo1r pe6ople g3ood th5e the2"
# print(order(sentence))


# 26. You are given an array (which will have a length of at least 3, but could be very large)
# containing integers. The array is either entirely comprised of odd integers or entirely comprised
# of even integers except for a single integer N. Write a method that takes the array as an argument
# and returns this "outlier" N.


# def find_outlier(integers):
#     a = []
#     b = []
#     for i in integers:
#         if i % 2:
#             a.append(i)
#         else:
#             b.append(i)
#     if len(a) < len(b):
#         for i in a:
#             return i
#     else:
#         for i in b:
#             return i
#
#
# integers = [2, 4, 0, 100, 4, 11, 2602, 36]
# print(find_outlier(integers))


# 27. You probably know the "like" system from Facebook and other pages. People can
# "like" blog posts, pictures or other items. We want to create the text that should be displayed
# next to such an item. For 4 or more names, the number in "and 2 others" simply increases.
# []                                -->  "no one likes this"
# ["Peter"]                         -->  "Peter likes this"
# ["Jacob", "Alex"]                 -->  "Jacob and Alex like this"
# ["Max", "John", "Mark"]           -->  "Max, John and Mark like this"
# ["Alex", "Jacob", "Mark", "Max"]  -->  "Alex, Jacob and 2 others like this"


# def likes(names):
#     result = ''
#     ind = 0
#     if len(names) == 0:
#         result = "no one likes this"
#     elif len(names) == 1:
#         result = f"{names[ind]} likes this"
#     elif len(names) == 2:
#         result = f"{names[ind]} and {names[ind+1]} like this"
#     elif len(names) == 3:
#         result = f"{names[ind]}, {names[ind+1]} and {names[ind+2]} like this"
#     elif len(names) > 3:
#         result = f"{names[ind]}, {names[ind+1]} and {len(names)-2} others like this"
#     return result
#
#
# names = []
# print(likes(names))


# 28. Write a function that accepts an array of 10 integers (between 0 and 9), that returns a string of those numbers
# in the form of a phone number.
# create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890"

# def create_phone_number(n):
#     return f'({n[0]}{n[1]}{n[2]}) {n[3]}{n[4]}{n[5]}-{n[6]}{n[7]}{n[8]}{n[9]}'
#
#
# n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
# print(create_phone_number(n))

# better
# def create_phone_number(n):
#    return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)


# 29. You live in the city of Cartesia where all roads are laid out in a perfect grid.
# You arrived ten minutes too early to an appointment, so you decided to take the opportunity
# to go for a short walk. The city provides its citizens with a Walk Generating App on their
# phones -- everytime you press the button it sends you an array of one-letter strings representing
# directions to walk (eg. ['n', 's', 'w', 'e']). You always walk only a single block for each letter
# (direction) and you know it takes you one minute to traverse one city block, so create a function
# that will return true if the walk the app gives you will take you exactly ten minutes (you don't want
# to be early or late!) and will, of course, return you to your starting point. Return false otherwise.

# Note: you will always receive a valid array (string in COBOL) containing a random assortment of direction
# letters ('n', 's', 'e', or 'w' only). It will never give you an empty array (that's not a walk, that's
# standing still!).


# def is_valid_walk(walk):
#     if len(walk) != 10:
#         return False
#     if walk.count('n') != walk.count('s') or walk.count('w') != walk.count('e'):
#         return True
#
#
# walk  = ['s', 'w', 'n', 'e', 'n', 'e', 's', 'w']
# print(is_valid_walk(walk))


# 30 Your goal in this kata is to implement a difference function, which subtracts one list from
# another and returns the result. It should remove all values from list a, which are present
# in list b keeping their order.


# def array_diff(a, b):
#     return [i for i in a if i not in b]
#
#
# a = [1, 2, 2, 2, 3]
# b = [2]
# print(array_diff(a, b))


# 31 You are going to be given an array of integers. Your job is to take that array and find an index N
# where the sum of the integers to the left of N is equal to the sum of the integers to the right of N.
# If there is no index that would make this happen, return -1.
# For example:
# Let's say you are given the array {1,2,3,4,3,2,1}:
# Your function will return the index 3, because at the 3rd position of the array, the sum of left side
# of the index ({1,2,3}) and the sum of the right side of the index ({3,2,1}) both equal 6.
# Let's look at another one.
# You are given the array {1,100,50,-51,1,1}:
# Your function will return the index 1, because at the 1st position of the array, the sum of left side
# of the index ({1}) and the sum of the right side of the index ({50,-51,1,1}) both equal 1.
# Last one:
# You are given the array {20,10,-80,10,10,15,35}
# At index 0 the left side is {}
# The right side is {10,-80,10,10,15,35}
# They both are equal to 0 when added. (Empty arrays are equal to 0 in this problem)
# Index 0 is the place where the left side and right side are equal.
# Note: Please remember that in most programming/scripting languages the index of an array starts at 0.
# Input:
# An integer array of length 0 < arr < 1000. The numbers in the array can be any integer positive or negative.
# Output:
# The lowest index N where the side to the left of N is equal to the side to the right of N.
# If you do not find an index that fits these rules, then you will return -1.
# Note:
# If you are given an array with multiple answers, return the lowest correct index.


# def find_even_index(arr):
#     lst = list(range(0, 1000))
#     for ind in lst:
#         if sum(arr[0:ind]) != sum(arr[ind+1:]):
#             ind += 1
#         else:
#             return ind
#         if ind == len(arr):
#             return -1
#
#
# arr = list(range(1,100))
# print(find_even_index(arr))


# 32 Find the missing letter. Write a method that takes an array of consecutive (increasing) letters
# as input and that returns the missing letter in the array. You will always get an valid array.
# And it will be always exactly one letter be missing. The length of the array will always be at least 2.
# The array will always contain letters in only one case.


# import string
#
#
# def find_missing_letter(chars):
#     lst = string.ascii_letters
#     chars2 = []
#     for i in lst:
#         if i in chars:
#             chars2 = lst[lst.index(i):]
#             break
#     for i in chars2:
#         if i not in chars:
#             return i
#
#
# chars = ['O','Q','R','S']
# print(find_missing_letter(chars))


# 33 A pangram is a sentence that contains every single letter of the alphabet at least once.
# For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram, because it uses
# the letters A-Z at least once (case is irrelevant). Given a string, detect whether or not it is a pangram.
# Return True if it is, False if not. Ignore numbers and punctuation.


# import string


# def is_pangram(s):
#     alph = string.ascii_lowercase
#     return False if set(alph).difference(set(s.lower())) else True
#
#
# s = "ABCD45EFGH,IJK,LMNOPQR56STUVW3XYZ"
# print(is_pangram(s))

import pandas as pd


def tower_builder(n_floors):

    lst0 = ['  *  ', ' *** ', '*****']
    lst = []
    i = ''
    while len(lst) < n_floors:
        i = '*' * (n_floors+2)
        lst.append(i)
        print(lst)
        i.replace('*', ' ')
        i.replace(-1, ' ')
        i+= ' '
    print(lst)


n_floors = 3
print(tower_builder(n_floors))
