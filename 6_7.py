# Дан список чисел, необходимо для каждого элемента посчитать сумму его
# соседей, для крайних чисел одним из соседей является число с противоположной
# стороны списка


def num_in_list_t0_sum_of_its_neighbours(num_list):
    num_sum = []
    ind = 1
    num_sum.append(num_list[-1] + num_list[ind])
    while ind < (len(num_list)-1):
        num_sum.append(num_list[ind-1] + num_list[ind+1])
        ind += 1
    num_sum.append(num_list[-2] + num_list[0])
    return num_sum


print(num_in_list_t0_sum_of_its_neighbours([2, 3, 4, 5, 6]))