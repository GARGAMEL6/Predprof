def binary_search(arr, el):
    if el not in arr:
        return -1
    left, right = 0, len(arr) - 1
    while arr[left] != el:
        mid = (left + right) // 2
        if el < arr[mid]:
            right = mid
        else:
            left = mid

    return left


with open('scientist.txt', 'r', encoding='utf-8') as file:
    data = [x[:-1].split('#') for x in file]
    data = data[1:]

    s = []
    date = input()
    while date != 'эксперимент':
        date = '-'.join(date.split('.')[::-1])
        index = binary_search([data[i][2] for i in range(len(data))], date)

        if index == -1:
            print('В этот день ученые отдыхали')
        else:
            left, right = index - 1, index + 1
            while data[left][2] == date:
                left -= 1
            while data[right][2] == date:
                right += 1

            for i in range(left + 1, right):
                print(f'Ученый {data[i][0]} создал препарат: {data[i][1]} - {data[i][2]}')

        date = input()