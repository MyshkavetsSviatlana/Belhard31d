# Ввести предложение, заменить все пробелы на "-" 2-мя
# способами

sentence = input('Enter any sentence: ')
sentence_2 = sentence.replace(' ', '-')
print(sentence_2)

sentence_3 = '-'.join(sentence.split(' '))
print(sentence_3)

