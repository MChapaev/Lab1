print('Provide lines. Type \"stop\" to end input')
lines = []
while True:
    line = input()
    if line.lower() == 'stop':
        break
    lines.append(line)

for i in range(len(lines)):
    for j in range(len(lines)):
        if len(lines[i].split(' ')) < len(lines[j].split(' ')):
            lines[i], lines[j] = lines[j], lines[i]
print('Sorted lines:\n', '\n'.join(lines))
