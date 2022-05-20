# 1
# In this kata you are required to, given a string, replace every letter with its position in the alphabet.
# If anything in the text isn't a letter, ignore it and don't return it.


def alphabet_position(text: str) -> str:
    """Replaces every letter with its position in the alphabet. Ignores any symbol that isn't a letter."""
    letters = (
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
        'w', 'x', 'y', 'z')
    numbers = [str(num) + ' ' for num in range(1, 27)]
    letters_numbers = dict(zip(letters, numbers))
    result_list = ''
    for symbol in text.lower().replace(' ', ''):
        if symbol.isalpha():
            result_list += letters_numbers[symbol]
        else:
            continue
    return result_list.rstrip()


text = "The sunset sets at twelve o' clock."
print(alphabet_position(text))
