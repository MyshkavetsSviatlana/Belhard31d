# *Заполнить словарь, где ключами будут выступать числа от 0 до n,
# значениями - вложенный словарь с ключами "name" и "email", а значения
# для этих ключей будут браться с клавиатуры.

n = int(input('Enter any integer: '))

outer_dict = {}
for i in range(0, n + 1):
    inner_dict = {}
    outer_dict[i] = inner_dict
    inner_dict['name'] = input('Enter your name: ')
    inner_dict['email'] = input('Enter your email: ')
    print(outer_dict)
