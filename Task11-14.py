# Task 11
def char_position(c):
    return ord(c) - ord('a')


def frequency(s):
    s = s.lower()
    amount_max = 0
    char_max = ''
    for i in s:
        amount = s.count(i)
        if amount > amount_max:
            amount_max = amount
            char_max = i
    if len(s) > 0:
        return abs(amount_max - char_position(char_max))
    return 0


def frequency_sort(s):
    return sorted(s, key=frequency)


def read_multiline():
    print('Provide lines (type \"stop\" to stop): ')
    lines = []
    while True:
        line = input()
        if line.lower() == 'stop':
            return lines
        lines.append(line)


def task11():
    print('Sorted by frequency difference: ',
          ' '.join(frequency_sort(read_multiline())))


# Task 12
def task12():
    print('task11')


# Task 13
def task13():
    print('task11')


# Task 14
def task14():
    print('task11')


# Main
def invalid_input():
    print('Invalid input.')
    main()


def main():
    index = input('Select a task (11-14): ')
    if index.isdigit():
        index = int(index)
        if index == 11:
            task11()
        elif index == 12:
            task12()
        elif index == 13:
            task13()
        elif index == 14:
            task14()
        else:
            invalid_input()
    else:
        invalid_input()


if __name__ == '__main__':
    main()