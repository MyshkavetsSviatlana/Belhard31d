# Сделать калькулятор: у пользователя спрашивается число, потом действие и второе число.

first_number = float(input('Enter any number: '))
operator = input('Enter any math operator: ')
second_number = float(input('Enter any number: '))

result = 0
if operator == '+':
    result = first_number + second_number
elif operator == '-':
    result = first_number - second_number
elif operator == '*':
    result = first_number * second_number
elif operator == '/':
    result = first_number / second_number
elif operator == '**':
    result = first_number ** second_number
elif operator == '%':
    result = first_number % second_number
print(result)
