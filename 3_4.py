# Пользователь вводит 3 числа, сказать сколько из них положительных
# и сколько отрицательных.

first_num = input('Enter any number: ')
second_num = input('Enter any number: ')
third_num = input('Enter any number: ')

positive_nums = (int(first_num) > 0) + (int(second_num) > 0) + (int(third_num) > 0)
print(f'You have entered {positive_nums} positive number(s).')

negative_nums = (int(first_num) < 0) + (int(second_num) < 0) + (int(third_num) < 0)
print(f'You have entered {negative_nums} negative number(s).')

# верно
first_num = float(input('Enter any number: '))
second_num = float(input('Enter any number: '))
third_num = float(input('Enter any number: '))

positive_nums = (first_num > 0) + (second_num > 0) + (third_num > 0)
print(f'You have entered {positive_nums} positive number(s).')

negative_nums = (first_num < 0) + (second_num < 0) + (third_num < 0)
print(f'You have entered {negative_nums} negative number(s).')

