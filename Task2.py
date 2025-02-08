import random


def shake(word):
    middle = list(word[1:-1])
    random.shuffle(middle)
    return word[0] + ''.join(middle) + word[-1]


line = input('Provide a sentence: ')
words = line.split(' ')
shaken_words = ''
for i in words:
    shaken_words += shake(i) + ' '
print('Shaken words: ', shaken_words)
