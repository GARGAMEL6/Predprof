with open('scientist.txt', 'r', encoding='utf-8') as file:
    data = [x[:-1].split('#') for x in file]
    data = data[1:]

    for i in range(len(data) - 1):
        for j in range(i+1, len(data)):
            if data[j][2] < data[i][2]:
                temp = data[i][:]
                data[i] = data[j][:]
                data[j] = temp[:]

    d = dict()
    for i in range(len(data)):
        d[data[i][1]] = d.get(data[i][1], []) + [(data[i][0], data[i][2], i)]

    map_of_rights = []

    for lec in d.values():
        m = lec[0][1]
        I = lec[0][2]
        for pair in lec:
            if pair[1] < m:
                m = pair[1]
                I = pair[2]

        map_of_rights.append(I)

    print("Разработчиками Аллопуринола были такие люди:")
    for banned in d['Аллопуринол'][1:]:
        print(f'{banned[0]} - {banned[1]}')

    print(f'Оригинальный рецепт принадлежит: {d["Аллопуринол"][0][0]}')




with open('scientist_origin.txt', 'w', encoding='utf-8') as file:
    for i in range(len(data)):
        if i in map_of_rights:
            file.write('#'.join(data[i]))
            file.write('\n')

