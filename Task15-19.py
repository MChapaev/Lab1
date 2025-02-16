# Task 15
def index_min(arr):
    i_min = 0
    for i in range(1, len(arr)):
        if arr[i] < arr[i_min]:
            i_min = i
    return i_min


def index_max(arr):
    i_max = 0
    for i in range(1, len(arr)):
        if int(arr[i]) > int(arr[i_max]):
            i_max = i
    return i_max


def reverse_between_min_max(arr):
    if not arr:
        return arr
    i_min = index_min(arr)
    i_max = index_max(arr)
    start, end = sorted([i_min, i_max])
    arr[start + 1:end] = arr[start + 1:end][::-1]
    return arr


def task15():
    data = input('Provide an array: ').split(' ')
    print('Reversed elements between min and max elements: ', reverse_between_min_max(data))


# Task 16
def task16():
    data = input('Provide an array: ').split(' ')
    data = list(map(int, data))
    print('Two max elements:', sorted(data)[len(data)-2::])


# Task 17
def max_odd_num(arr):
    if not arr:
        print('All elements in array are even. Cannot find max odd number')
        return 0
    max_num = max(arr)
    if max_num % 2 == 0:
        arr.remove(max_num)
        max_num = max_odd_num(arr)
    return max_num


def task17():
    data = input('Provide an array: ').split(' ')
    data = list(map(int, data))
    print('Max odd number:', max_odd_num(data))


# Task 18
def most_frequent_element(input_list):
    frequency = {}

    for item in input_list:
        if item in frequency:
            frequency[item] += 1
        else:
            frequency[item] = 1

    max_count = max(frequency.values())
    result = []
    for index, value in enumerate(input_list):
        if frequency[value] == max_count:
            result.append(index)
    return result


def task18():
    data = input('Provide a line: ')
    print('Indexes of most frequent element:', most_frequent_element(data))


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
