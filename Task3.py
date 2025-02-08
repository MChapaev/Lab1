line = input('Provide a line: ')
digits = ''
chars = ''
for i in line:
    if i.isdigit():
        digits += i
    else:
        chars += i
print('Sorted line: ', digits + chars)