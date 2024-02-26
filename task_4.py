import random
import string
import csv


def create_login(name):
    surname, last_name, father = name.split()[0], name.split()[1], name.split()[2]
    return f'{surname}_{last_name[0]}{father[0]}'


def create_password():
    alph = string.ascii_lowercase
    up_alph = alph.upper()
    digits = string.digits

    letters = alph + up_alph + digits
    while True:
        x = ""
        for _ in range(10):
            x += random.choice(letters)

        a = any(i in x for i in alph)
        b = any(i in x for i in up_alph)
        c = any(i in x for i in digits)

        if a + b + c == 3:
            return x


with open('scientist.txt', 'r', encoding='utf-8') as file:
    data = [x[:-1].split("#") for x in file]
    data = data[1:]

    for i in range(len(data)):
        data[i].extend([create_login(data[i][0]), create_password()])

with open('scientist_password.csv', 'w') as file:
    writer = csv.writer(file, delimiter='#')
    writer.writerow(['ScientistName', 'preparation', 'date', 'components', 'login', 'password'])
    for i in data:
        writer.writerow(i)

