# *Заполнить словарь, где ключами будут выступать числа от 0 до n,
# значениями - вложенный словарь с ключами "name" и "email", а значения
# для этих ключей будут браться с клавиатуры.

n = int(input('Enter any integer: '))

# # 1
# outer_dict = {}
# for i in range(0, n + 1):
#     inner_dict = {}
#     outer_dict[i] = inner_dict
#     inner_dict['name'] = input('Enter your name: ')
#     inner_dict['email'] = input('Enter your email: ')
#     print(outer_dict)
#
# # 2
# outer_dict1 = {}
# for i in range(0, n):
#     text = {'name': input('Enter your name: '), 'email': input('Enter your email: ')}
#     outer_dict1[i] = text
# print(outer_dict1)

# 3
users_dict = {i: {'name': input('Enter your name: '), 'email': input('Enter your email: ')} for i in range(0, n)}
print(users_dict)
