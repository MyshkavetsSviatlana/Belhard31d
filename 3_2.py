# Пользователь вводит 3 числа, надо найти среднее арифмитическое с
# точностью 3 знака после запятой.

first_num = input('Enter any integer: ')
second_num = input('Enter any integer: ')
third_num = input('Enter any integer: ')

# 1
def mean_3nums(first_num, second_num, third_num):
    """"Returns the mean of 3 arguments"""
    sum_num = float(first_num) + float(second_num) + float(third_num)
    return round(sum_num/3, 3)
print(mean_3nums(first_num, second_num, third_num))

# 2
print(round((float(first_num) + float(second_num) + float(third_num))/3, 3))


