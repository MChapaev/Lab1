# Task 6
def task6():
    print('Task 6')


# Task 7
def task7():
    print('Task 7')


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
