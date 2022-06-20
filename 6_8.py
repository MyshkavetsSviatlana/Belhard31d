# Дан словарь, ключ - название страны, значение - список городов, на вход
# поступает город, необходимо сказать из какой он страны.

country_city_dict = {
    'Australia': ['Sydney', 'Melbourne'],
    'Austria': ['Vienna', 'Linz'],
    'Belarus': ['Minsk', 'Ossipovichy'],
    'Germany': ['Berlin', 'Kassel']
}


city = input('Enter any city: ').capitalize()
for country, element in country_city_dict.items():
    if city in element:
        print(f'{city} is in {country}.')

