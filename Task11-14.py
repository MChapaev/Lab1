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
          '\n'.join(frequency_sort(read_multiline())))


# Task 12
def extract_numbers(s):
    nums = []
    current_num = ''

    for c in s:
        if c.isdigit():
            current_num += c
        elif current_num:
            nums.append(int(current_num))
            current_num = ''
    if current_num:
        nums.append(int(current_num))
    return nums


def find_median(lst):
    lst.sort()
    n = len(lst)
    if n == 0:
        return None
    if n % 2 == 1:
        return lst[n // 2]
    else:
        return (lst[n // 2 - 1] + lst[n // 2]) / 2


def median_sort(strings):
    sorted_strings = []

    while strings:
        values = [(s, extract_numbers(s)) for s in strings]
        medians = [(s, find_median(nums)) for s, nums in values if nums]

        if not medians:
            sorted_strings.extend(strings)
            break

        min_median_str, _ = min(medians, key=lambda x: x[1])

        sorted_strings.append(min_median_str)
        strings.remove(min_median_str)

    return sorted_strings


def task12():
    data = input('Provide a line: ').split(' ')
    sorted_data = median_sort(data)
    print('Sorted in order of increasing the median value of the row selection: ', ' '.join(sorted_data))


# Task 13
def max_ascii(s):
    max_code = 0
    for c in s:
        max_code = max(max_code, ord(c))
    return max_code


def mirrored_diff(s):
    n = len(s)
    diffs = []
    for i in range(n // 2):
        diffs.append(abs(ord(s[i]) - ord(s[n - i - 1])))
    return diffs


def quadratic_deviation(s):
    max_code = max_ascii(s)
    diffs = mirrored_diff(s)

    if not diffs:
        return 0

    squared_diffs = [(max_code - d) ** 2 for d in diffs]
    return sum(squared_diffs) / len(squared_diffs)


def deviation_sort(strings):
    return sorted(strings, key=quadratic_deviation)


def task13():
    data = input('Provide a line: ').split(' ')
    sorted_data = deviation_sort(data)
    print('Sorted in order of increasing the square deviation\n'
          'between the largest The ASCII character code of the string\n'
          'and the difference in the ASCII codes of pairs of mirrored characters\n'
          'of the string (relative to its middle):\n', ' '.join(sorted_data))


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