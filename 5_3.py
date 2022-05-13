# **Вывести четные числа от 2 до N по 5 в строку.

# 1
n = int(input('Enter any number: '))
result = [i for i in range(0, n+1) if i % 2 == 0]

a = 0
b = 5
while b < len(result) + 5:
    print(result[a:b])
    a += 5
    b += 5

# 2
n = int(input('Enter any number: '))

result = []
for i in range(2, n+1):
    if i % 2 == 0:
        result.append(i)

a = 0
b = 5
while b < len(result) + 5:
    print(result[a:b])
    a += 5
    b += 5
