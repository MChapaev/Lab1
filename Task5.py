months = [
    'января', 'февраля', 'марта', 'апреля', 'мая', 'июня',
    'июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря'
]
line = input('Provide a line: ')

# prompt for fast testing
# line = '23 февраля 2007 123 сентября 20 щцшкзщцук 23 сент 20123 9312 февраля 12 сентября 2005'

words = line.split(' ')
for i in range(len(words) - 2):
    if words[i].isdigit():
        if 0 < int(words[i]) < 32:
            if words[i+1] in months:
                if words[i+2].isdigit():
                    if int(words[i+2]) > 0:
                        print(f'Found date: {words[i]} {words[i+1]} {words[i+2]}')
