import csv
import random
import math
'''
vic_visitors = [["Victoria's Regions", '2004', '2005', '2006', '2007'], ['Gippsland', '63354', '47083', '51517', '54872'], ['Goldfields', '42625', '36358', '30358', '36486'], ['Grampians', '64092', '41773', '29102', '38058'], ['Great Ocean Road', '185456', '153925', '150268', '167458'], ['Melbourne', '1236417', '1263118', '1357800', '1377291']]
with open("vic_visitors.csv", "w+", newline='') as my_csv:
    csvWriter = csv.writer(my_csv, delimiter=',')
    csvWriter.writerows(vic_visitors)



header1 = ['Date', 'ID', 'ReadTime', 'NumSales']
data1 = []
for i in range(20):
    transaction = ["a date", random.randint(1, 10), math.floor(random.gammavariate(2, 2)) + 1, random.randint(100, 1000)]
    data1.append(transaction)
data1.insert(0, header1)
with open("test1.csv", "w+", newline='') as my_csv:
    csvWriter = csv.writer(my_csv, delimiter=',')
    csvWriter.writerows(data1)






filename = "test1.csv"
file_handle = open(filename)
data = csv.reader(file_handle)
header = next(data)
data_2d = list(data)
file_handle.close()

print(data_2d)
for i in range(len(data_2d)):
    for j in range(len(data_2d[i])):
        if data_2d[i][j].isnumeric():
            data_2d[i][j] = float(data_2d[i][j])

for i in data_2d:
    for j in i:
        print(j, type(j))


def transpose(filename):
    filehandle = open(filename)
    data = csv.reader(filehandle)
    header = next(data)
    data_2d = list(data)
    filehandle.close
    data_t = []
    for col in range(len(header)):
        rowcol = []
        for row in data_2d:
            rowcol.append(row[col])
        data_t.append(rowcol)
    return data_t

print(transpose(filename))


def best(id):
    filehandle = open("Purchase.csv")
    data = csv.reader(filehandle)
    header = next(data)
    data_2d = list(data)
    filehandle.close
    tally = {}
    for row in data_2d:
        if row[1] == str(id):
            if row[0] in tally:
                tally[row[0]] += row[2]
            else:
                tally[row[0]] = row[2]
    tally = sorted(tally.items(), key=lambda x: (x[1],x[0]), reverse=True)
    return tally[0][0]

print(best(4))

def total_money(customer):
    filehandle = open("Purchase.csv")
    data = csv.reader(filehandle)
    header = next(data)
    data_2d = list(data)
    filehandle.close
    tally = {}
    for row in data_2d:
        if row[0] == customer:
            if row[1] in tally:
                tally[row[1]] += row[2]
            else:
                tally[row[1]] = row[2]
    total = 0
    for i in tally:
        total += tally[i] * ps[2]
    return total

print(total_money('cunninghamc'))
'''

def flatten(S):
    if S == []:
        return S
    if isinstance(S[0], list):
        return flatten(S[0]) + flatten(S[1:])
    return S[:1] + flatten(S[1:])

s=[[5],[2,[33,[3,3]]],[4],[3,[2,4]]]
print(flatten(s))
