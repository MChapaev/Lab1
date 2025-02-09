import random


# Task 2
def shake(word):
    middle = list(word[1:-1])
    random.shuffle(middle)
    return word[0] + ''.join(middle) + word[-1]


def task2():
    line = input('Provide a sentence: ')
    words = line.split(' ')
    shaken_words = ''
    for i in words:
        shaken_words += shake(i) + ' '
    print('Shaken words: ', shaken_words)


# Task 3
def task3():
    line = input('Provide a line: ')
    digits = ''
    chars = ''
    for i in line:
        if i.isdigit():
            digits += i
        else:
            chars += i
    print('Sorted line: ', digits + chars)


# Task 4
def task4():
    line = input('Provide a sentence: ')
    words = list(line.split())
    random.shuffle(words)
    print('Master Yoda says:', ' '.join(words))


# Main
def invalid_input():
    print('Invalid input.')
    main()


def main():
    index = input('Select a task (2-4): ')
    if index.isdigit():
        index = int(index)
        if index == 2:
            task2()
        elif index == 3:
            task3()
        elif index == 4:
            task4()
        else:
            invalid_input()
    else:
        invalid_input()


if __name__ == '__main__':
    main()
