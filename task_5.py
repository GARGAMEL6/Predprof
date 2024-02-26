import random
import csv


table = [i for i in range(1024)]
random.shuffle(table)

def hash(s):
     a = 0
     for x in s:
         a += table[ord(x) % 1024]
     return str(a % 2048)


with open('scientist.txt', 'r', encoding='utf-8') as file:
    data = [x[:-1].split() for x in file]
    data = data[1:]

    for i in range(len(data)):
        data[i] = [hash(data[i][0])].extend(data[i])


with open('scientist_with_hash.csv', 'w') as file:
    writer = csv.writer(file, delimiter='#')
    writer.writerow(['hash', 'ScientistName', 'preparation', 'date', 'components'])
    for i in data:
        writer.writerow(i)

