# Дан словарь словарей, ключ внешнего словаря - id пользователя, значение -
# словарь с данными о пользователе (имя, фамилия, телефон, почта), вывести
# имена тех, у кого не указана почта (нет ключа email или значение этого ключа -
# пустая строка).

dict_of_dict = {
    '1': {'first name': 'Vera', 'last name': 'Ivanova', 'phone': '1234567', 'email': 'Vera@mail'},
    '2': {'first name': 'Pasha', 'last name': 'Petrov', 'phone': '2345678'},
    '3': {'first name': 'Dima', 'last name': 'Sidorov', 'phone': '3456789', 'email': 'Dima@mail'},
    '4': {'first name': 'Sveta', 'last name': 'Sergeeva', 'phone': '4567891', 'email': ''},
    '5': {'first name': 'Lyuda', 'last name': 'Klimovich', 'phone': '5678912', 'email': 'Lyuda@mail'},
    '6': {'first name': 'Max', 'last name': 'Mironchik', 'phone': '6789123'},
    '7': {'first name': 'Tamara', 'last name': 'Sologub', 'phone': '7891234', 'email': 'Tamara@mail'}}


no_email_ids = []
no_email_names = []
for outer_key, outer_value in dict_of_dict.items():
    for inner_key, inner_value in outer_value.items():
        if 'email'not in outer_value.keys() or outer_value['email'] == '':
            no_email_ids.append(outer_key)
            no_email_names.append(outer_value['first name'])
            break


print(no_email_ids)
print(no_email_names)





