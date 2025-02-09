# Task 6

def right_number(n):
    return len(n) > 0 and int(n) > 5


def task6():
    number = ''
    amount = 0
    for i in input('Provide a line: '):
        if i.isdigit():
            number += i
        else:
            if right_number(number):
                amount += 1
            number = ''
    # check last char
    if right_number(number):
        amount += 1
    print(f'Amount of numbers bigger than 5 in line: {amount}')


# Task 7
def get_cyrillic_chars():
    alphabet = []
    for code_point in range(0x0410, 0x0450):
        alphabet.append(chr(code_point))
    return alphabet


def task7():
    chars = get_cyrillic_chars()
    for i in input('Provide a line (in cyrillic): '):
        if i in chars:
            chars.remove(i)
    print('Unused cyrillic letters in line: ')
    print(''.join(chars))


# Task 8
def task8():
    print('Task 8')


# Main
def invalid_input():
    print('Invalid input.')
    main()


def main():
    index = input('Select a task (6-8): ')
    if index.isdigit():
        index = int(index)
        if index == 6:
            task6()
        elif index == 7:
            task7()
        elif index == 8:
            task8()
        else:
            invalid_input()
    else:
        invalid_input()


if __name__ == '__main__':
    main()
