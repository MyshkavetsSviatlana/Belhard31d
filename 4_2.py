# Без использования collections, написать программу, которая будет
# создавать словарь для подсчитывания количества вхождений каждой
# буквы в текст, введенный с клавиатуры.

text = input('Enter any text: ')

#1
count_dict = {}
for key in text:
    if key in count_dict.keys():
        count_dict[key] += 1
    else:
        count_dict[key] = 1
print(count_dict)

#2
count_dict = {key: text.count(key) for key in text}
print(count_dict)
