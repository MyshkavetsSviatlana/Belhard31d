# Дан список рандомных чисел, необходимо отсортировать его в виде, сначала
# четные, потом нечётные.

import random

random_list = []
while len(random_list) < 10:
    random_list.append(random.randint(1, 1000))
print(random_list)

evens = []
odds = []
for num in random_list:
    if num % 2 == 0:
        evens.append(num)
    else:
        odds.append(num)
print(sorted(evens) + sorted(odds))

