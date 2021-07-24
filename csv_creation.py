## 1: Importing relevant pac
import random
import math
import names
import csv
from datetime import date, timedelta
random.seed(a=69)

## https://docs.python.org/3/library/random.html

## 2: Generating list of dates
sdate = date(2000, 1, 1)   # start date
edate = date(2016, 12, 31)   # end date

delta = edate - sdate       # as timedelta

date_list = []

for i in range(delta.days + 1):
    day = sdate + timedelta(days=i)
    dates = date_list.append(day)
#print(date_list)

## Source: https://stackoverflow.com/questions/7274267/print-all-day-dates-between-two-dates

## 3: Creating dictionary with product prices
product_prices = {
    1:199,
    2:489,
    3:1459,
    4:189,
    5:199,
    6:35.99,
    7:25.99,
    8:1089,
    9:1329,
    10:649,
    11:1622,
    12:129.99,
    13:379,
    14:64.99,
    15:89.99,
    16:64.99,
    17:49.99,
    18:49.99,
    19:25.99,
    20:65,
    21:109,
    22:129,
    23:119,
    24:64,
    25:159,
    26:39.99,
    27:39,
    28:459,
    29:99,
    30:89.99,
    31:1622,
    32:1500.99}

#print(product_prices)

## 3: Creating dictionary with shipping prices
ship_prices = {}
for i in range(1, 33):
    ship_prices[i] = round(product_prices[i] * 0.10, 2)
#print(ship_prices)

## 30 transactions a day, 200 customers a year with 50 sales a year
## 4: Creating list of customer IDs

customers = []
for i in range(1, 201):
    name = names.get_full_name()
    name = name.split()
    customer_id = name[1] + name[0][0]
    customer_id = customer_id.lower()
    customers.append(customer_id)
#print(customers)

## 5: Creating Header
header = ['Id', 'Product', 'Quantity', 'Date', 'Shipping']
product_ids = list(range(1, 33))

## 6: Creating 2D data
data = []
for i in range(1000):
    productid = random.choice(product_ids)
    transaction = [random.choice(customers), productid, math.floor(random.gammavariate(2, 2)) + 1,
    random.choice(date_list), ship_prices[productid]]
    data.append(transaction)

## 7: Sorting by date
data = sorted(data, key=lambda x: x[3])

for row in data:
    row[3] = str(row[3].strftime('%d/%m/%Y'))

## 8: Ensuring certain products only have quantity of 1
for row in data:
    if row[1] in (1, 2, 3, 8, 9, 28, 30):
        row[2] = 1

## Help from https://jingwen-z.github.io/converting-between-datetime-and-string/

## 9: Inserting header
data.insert(0, header)

#print(data)

## 10: Writing data to csv
with open("Purchase.csv", "w+", newline='') as my_csv:
    csvWriter = csv.writer(my_csv, delimiter=',')
    csvWriter.writerows(data)

## Help from https://stackoverflow.com/questions/44691524/write-a-2d-array-to-a-csv-file-with-delimiter


