# Вывести первые N чисел кратные M и больше K.

n = int(input('Enter any integer for n: '))
m = int(input('Enter any integer for m: '))
k = int(input('Enter any integer for k: '))

numbers_result = []
for i in range(0, 1000):
    if i % m == 0 and i > k:
        numbers_result.append(i)
print(numbers_result[0:n])


