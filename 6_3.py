# Дан список чисел и на вход поступает число N, необходимо сместить список на
# указанное число, пример: [1,2,3,4,5,6,7] N=3 ответ: [5,6,7,1,2,3,4].

num_list = [1, 2, 3, 4, 5, 6, 7]
n = int(input('Enter any number: '))
length = len(num_list) - 1
result_list = []
if n > len(num_list)-1:
    print(f'The number is too big. It should be < {length}.')
elif n == 0 or n == (len(num_list)-1):
    result_list = num_list[:]
    print(result_list)
else:
    result_list.extend(num_list[n+1:])
    result_list.extend(num_list[:n+1])
    print(result_list)

