with open('scientist.txt', 'r', encoding='utf-8') as file:
    data = [x[:-1].split('#') for x in file]
    data = data[1:]

    for i in range(len(data) - 1):
        for j in range(i + 1, len(data)):
            if data[j][2] < data[i][2]:
                temp = data[i][2][:]
                data[i][2] = data[j][2][:]
                data[j][2] = temp[:]


with open('scientist.txt', 'w', encoding='utf-8') as file:
    file.write('ScientistName#preparation#date#components\n')
    for i in range(len(data)):
        file.write('#'.join(data[i]))
        file.write('\n')

        if i < 5:
            print(f'{data[i][0]}: {data[i][1]}')
