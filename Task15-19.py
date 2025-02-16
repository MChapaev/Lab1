# Task 15
def task15():
    print('task15')


# Task 16
def task16():
    print('task16')


# Task 17
def task17():
    print('task17')


# Task 18
def task18():
    print('task18')


# Task 19
def task19():
    print('task19')


# Main
def invalid_input():
    print('Invalid input.')
    main()


def main():
    index = input('Select a task (15-19): ')
    if index.isdigit():
        index = int(index)
        if index == 15:
            task15()
        elif index == 16:
            task16()
        elif index == 17:
            task17()
        elif index == 18:
            task18()
        elif index == 19:
            task19()
        else:
            invalid_input()
    else:
        invalid_input()


if __name__ == '__main__':
    main()
