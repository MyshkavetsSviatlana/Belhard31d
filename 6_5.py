# Дан список чисел, необходимо его развернуть без использования метода revese и
# функции reversed, а так же дополнительного списка и среза.

num_list = [1, 2, 3, 4, 5, 6, 7]
print(num_list)

# 1
print(sorted(num_list, reverse=True))

# 2
ind = 0
while ind < (len(num_list)-1):
    new_num = num_list.pop(-1)
    num_list.insert(ind, new_num)
    ind += 1
print(num_list)