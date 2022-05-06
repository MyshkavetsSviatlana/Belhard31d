# Пользователь вводит 3 числа, надо найти среднее арифмитическое с
# точностью 3 знака после запятой.

first_num = float(input('Enter any integer: '))
second_num = float(input('Enter any integer: '))
third_num = float(input('Enter any integer: '))

# 1
def mean_nums(*args):
    """"Returns the mean of all arguments"""
    sum_num = 0
    for num in args:
        sum_num += num
    return sum_num/len(args)

print('The mean of the numbers you entered is ' + str(round(mean_nums(first_num, second_num, third_num), 3)) + '.')


# 2
print(round((float(first_num) + float(second_num) + float(third_num))/3, 3))


