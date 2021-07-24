import math


class Circle:
    def __init__(self, xcenter, ycenter, radius):
        self.xcenter = xcenter
        self.ycenter = ycenter
        self.radius = radius

    def prettyprint(self):
        return"({x}, {y}) radius= {r}".format(x = self.xcenter, y = self.ycenter, r = self.radius)

    def overlap(self, circle2):
        xdistance = abs(self.xcenter - circle2.xcenter)
        ydistance = abs(self.ycenter - circle2.ycenter)
        radius_total = self.radius + circle2.radius
        center_distance = math.sqrt(xdistance**2 + ydistance**2)
        if radius_total >= center_distance:
            return True
        else:
            return False


s1 = Circle(100, 200, 20)
s2 = Circle(100, 100, 200)

print(s1.prettyprint())
print(s1.overlap(s2))



import random
import csv

header = ['Id', 'Product', 'Quantity', 'Date', 'Shipping']
data = []
for i in range(20):
    transaction = [random.randint(0,250), random.randint(0,10), math.floor(random.gammavariate(2, 2)) + 1,
    random.randint(0,75), random.randint(0,100)]
    data.append(transaction)
data.insert(0, header)
with open("test.csv", "w+", newline='') as my_csv:
    csvWriter = csv.writer(my_csv, delimiter=',')
    csvWriter.writerows(data)






filename = "test.csv"
def stats(filename):
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
    avg = []
    for i in data_t:
        total = 0
        for j in i:
            total += float(j)
        avg.append(total/len(data_t[0]))
    result = {}
    for i in range(len(header)):
        result[header[i]] = avg[i]
    return result

import numpy as np

def stats2(filename):
    filehandle = open(filename)
    data = csv.reader(filehandle)
    header = next(data)
    data_2d = list(data)
    filehandle.close
    data_t = []
    for col in range(len(header)):
        rowcol = []
        for row in data_2d:
            rowcol.append(float(row[col]))
        data_t.append(rowcol)
    var = []
    for i in data_t:
        var.append(np.var(i))
    result = {}
    for i in range(len(header)):
        result[header[i]] = var[i]
    return result
'''
def stats3(filename):
    filehandle = open(filename)
    data = csv.reader(filehandle)
    header = next(data)
    data_2d = list(data)
    filehandle.close
    data_t = []
    for col in range(len(header)):
        rowcol = []
        for row in data_2d:
            if type(row) == type("s"):
                rowcol.append(float(row[col]))
            else:
                rowcol.append(row[col])
        data_t.append(rowcol)
    variances = []
    for i in data_t:
        variances.append(np.var(i))
    result = {}
    for i in range(len(header)):
        result[header[i]] = variances[i]
    return result
'''
print(stats(filename))
print(stats2(filename))
print(stats(filename))

'''
Line 1 O(1)
Line 2 O(n)
Line 3 O(1)
Line 4 O(1)
Line 5 O(1)

Overal O(n)

Still O(n)

Line 1 O(1)
Line 2 O(n)
Line 3 O(n)
Line 4 O(1)
Line 5 O(1)
Line 6 O(1)

Overall O(n**2)

sub_list 1 has length n/2
sub_list 2 has length n/2
Overall O(n)
'''
names = ['yadsfo', 'eadfk', 'dasfeadew']

def count_es(lst):
    total = 0
    for i in lst:
        for j in i:
            if j in 'eE':
                total += 1
    return total

print(count_es(names))

'''
<html>
<div class = price>2.3</div>
<div class = price>2.3</div>
<div class = price>2.3</div>
<\html>
'''

header1 = ['Date', 'ID', 'ReadTime', 'NumSales']
data1 = []
for i in range(20):
    transaction = ["Date", random.randint(1, 10), math.floor(random.gammavariate(2, 2)) + 1, random.randint(100, 1000)]
    data1.append(transaction)
data1.insert(0, header1)
with open("test1.csv", "w+", newline='') as my_csv:
    csvWriter = csv.writer(my_csv, delimiter=',')
    csvWriter.writerows(data1)

def highest(filename):
    filehandle = open(filename)
    data = csv.reader(filehandle)
    header = next(data)
    data_2d = list(data)
    filehandle.close
    result = {}
    for row in data_2d:
        if row[1] in result:
            result[row[1]] += row[3]
        else:
            result[row[1]] = row[3]
    items = result.items()
    maxquantity = max(result.values())
    for k, v in items:
        if v == maxquantity:
            return {k: v}

filename1 = "test1.csv"
print(highest(filename1))

'''
Because you need to shuffle the list before accessing it each time, adding one extra task.
What the computer is doing besides executing this code will execute the runtime.
The random order in the second run might have been more detrimental to runtime, python may have had to traverse further
in the list than previously.
'''
import json

def make_jsont(filename):
    filehandle = open(filename)
    data = csv.reader(filehandle)
    header = next(data)
    data_2d = list(data)
    filehandle.close
    readtotals = {}
    for row in data_2d:
        if row[1] in readtotals:
            readtotals[row[1]] += row[2]
        else:
            readtotals[row[1]] = row[2]
    qtotals = {}
    for row in data_2d:
        if row[1] in qtotals:
            qtotals[row[1]] += row[3]
        else:
            qtotals[row[1]] = row[3]
    products = list(readtotals.keys())
    result = []
    for product in products:
        result.append({"Total Read": readtotals[product], "Total Sales": qtotals[product]})
    json_result = json.dumps(result)
    return json_result

print(make_jsont(filename1))