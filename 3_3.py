# Пользователь вводит Имя, Возраст и Город, сформировать
# приветственное сообщение путем форматирования 3-мя способами.

# 1 f-str
first_name = input('Enter your first name: ')
age = input('Enter your first age: ')
city = input('Enter the city where you live: ')

print(f"Hi! I am {first_name} from {city}. I am {age} years old.")

# 2 concatenation
print('Hi! ' + 'I am ' + str(first_name) + ' from ' + str(city) + '. I am ' + str(age) + ' years old.')

# 3 str.format()
print('Hi! I am {} from {}. I am {} years old.'.format(first_name, city, age))
