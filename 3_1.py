# Ввести предложение, заменить все пробелы на "-" 2-мя
# способами

sentence = 'Peter Piper picked a peck of pickled peppers.'
sentence_2 = sentence.replace(' ', '-')
print(sentence_2)

sentence_3 = '-'.join(sentence.split(' '))
print(sentence_3)
