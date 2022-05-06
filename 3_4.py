# Пользователь вводит 3 числа, сказать сколько из них положительных
# и сколько отрицательных.

first_num = input('Enter any number: ')
second_num = input('Enter any number: ')
third_num = input('Enter any number: ')

positive_nums = bool(int(first_num) > 0) + bool(int(second_num) > 0) + bool(int(third_num) > 0)
print(f'You have entered {positive_nums} positive numbers.')

negative_nums = bool(int(first_num) < 0) + bool(int(second_num) < 0) + bool(int(third_num) < 0)
print(f'You have entered {negative_nums} negative numbers.')
