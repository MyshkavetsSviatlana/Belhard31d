# Ввести строку, вывести уникальные символы из этой строки

# text = input('Enter any string: ')
#
# result = []
# for i in text:
#     if text.count(i) == 1:
#         result.append(i)
# print(result)

# Ввести слово, необходимо определить, является ли оно полиндромом

# text = input('Enter any string: ').lower().replace(' ', '')
#
# # if text[::-1] == text:
# #     print(text + ' is polindrome.')
#
# result = 'полиндром' if text == text[::-1] else 'не подиндром'
# print(result)

# Вводится текст, посчитать количество гласных и согласных

# text = input('Enter any string: ').lower()
# vowels = ['a', 'u', 'o', 'a', 'y']
# dict = {'vowels': 0, 'consonants': 0}
#
# for ch in text:
#     if ch.isalpha():
#         if ch in vowels:
#             dict['vowels'] += 1
#         else:
#             dict['consonants'] += 1
# print(dict)
    
# text = input('Enter any text: ').lower()
# vowels_count = 0
# consonants_count = 0
# vowels = 'eyuiaуеаоэяию'
#
# for symbol in text:
#     if symbol.isalpha():
#         if symbol in vowels:
#             vowels_count += 1
#         else:
#             consonants_count += 1
# print(vowels_count, consonants_count)

import pandas as pd


file = r'C:\Python_belhard\drop_dates.xlsx'
data = pd.read_excel(file)
print(data)

clean_data = data.dropna()
print(clean_data)



