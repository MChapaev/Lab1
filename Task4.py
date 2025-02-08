import random


line = input('Provide a sentence: ')
words = list(line.split())
random.shuffle(words)
print('Master Yoda says:', ' '.join(words))
