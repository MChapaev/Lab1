# Task 11
def task11():
    print('task11')


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