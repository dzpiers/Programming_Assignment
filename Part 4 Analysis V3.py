### Part 4A: Import Packages, Open Files & Extract Data

## Import Packages
import codecs
from bs4 import BeautifulSoup
import csv
import json
from collections import defaultdict


## Reference Filenames
html_file="index.html"
json_file="web.json"
csv_file="Purchase.csv"


## Open & Read HTML File
try:
    HTML=codecs.open(html_file, 'r','UTF-8')
    soup = BeautifulSoup(HTML, "lxml")
    
except UnicodeDecodeError:
    HTML=codecs.open(html_file, 'r')
    soup = BeautifulSoup(HTML, "lxml")
    

# Print the parsed data of html
#print(soup.prettify()) # Check if imported correctly

# Extract product ID from HTML file and put them in a list
product_id=[]
for tag in soup.findAll('div'):
    tag.name = "id"
    if tag['id'].isnumeric()==True:
        product_id.append(int(tag['id']))

# Test of all products imported
#print(len(product_id)) # Should = 32
    
# Extract price from HTML file and put them in a list
product_price_html=soup.select('.price')

product_price=[]
for price in product_price_html:
    price = price.text.strip()
    price = price.replace("$", "")
    price = price.replace("Price: ", "")
    product_price.append(float(price))

# Extract info form HTML file
product_info_html=soup.select('.info')

product_info=[]
for info in product_info_html:
    product_info.append(info.text.strip())

# Combine all id, price and info in list
product_all = []
for i in range(32):
    product_all.append([product_id[i], product_price[i], product_info[i]])
#print(product_all) # Check if consolidated correctly
    
    
## Open & Read JSON File
JSON = open(json_file, "r")
JSON = json.load(JSON)
#print(JSON) # Check if imported correctly

# Separate into each date
dates = JSON["all"]

# Separate into each event
events = []
for date in range(len(dates)):
    for event in range(len(dates[date]["events"])):
        events.append(dates[date]["events"][event])
#print(events) # Check if consolidated correctly

        
## Open & Read CSV File
CSV = open(csv_file)
CSV = csv.reader(CSV)
next(CSV)

# Create list of CSV file
purchase = []
for row in CSV:
    purchase.append([row[0], int(row[1]), int(row[2]), row[3], float(row[4])])
#print(purchase) # Check if consolidated correctly

### Part 4B: Analysis & Export Results

## Initiate CSV file to write all results to
results = open("results.csv", "w")

## 1. The highest priced product, giving the product id and the price

# Create dictionary of product ID and price
product_price = {}
for row in product_all:
    product_price[row[0]] = row[1]

# Sort from highest to lowest
max_price = sorted(sorted(product_price.items()), key=lambda x: x[1], reverse=True)
print('{} {}'.format(max_price[0][0],round(max_price[0][1],1)))
print('{} {}'.format(max_price[0][0],round(max_price[0][1],1)), file=results)


## 2. The mean number of words in the 32 info spans

# Define function to get average number of words
def average_words_length(info_list):
    num_words = []
    for info in info_list:
        info_split = info.split()
        num_words.append(len(info_split))
    avg_words = sum(num_words)/len(num_words)
    return round(avg_words,1)
print('{}'.format(average_words_length(product_info)))
print('{}'.format(average_words_length(product_info)), file=results)


## 3. The product that has the most hover time, giving the product id and the total number of seconds;

# Create list of hover product ID and total duration
hover = defaultdict(int)
for row in range(len(events)):
    if "hover" in events[row]:
        if events[row]["hover"] in hover:
            hover[events[row]["hover"]] += events[row]["duration"]
        else:
            hover[events[row]["hover"]] = events[row]["duration"]

# Find product with highest hover time
max_hover = sorted(hover.items(), key=lambda x: x[1], reverse=True)
print('{} {}'.format(max_hover[0][0],round(max_hover[0][1]),1))
print('{} {}'.format(max_hover[0][0],round(max_hover[0][1]),1), file=results)


## 4. The product that has the most read time, giving the product id and the total number of seconds;

# Create list of hover product ID and total duration
read = defaultdict(int)
for row in range(len(events)):
    if "read" in events[row]:
        if events[row]["read"] in read:
            read[events[row]["read"]] += events[row]["duration"]
        else:
            read[events[row]["read"]] = events[row]["duration"]

# Find product with highest hover time
max_read = sorted(read.items(), key=lambda x: x[1], reverse=True)
print('{} {}'.format(max_read[0][0],max_read[0][1]))
print('{} {}'.format(max_read[0][0],max_read[0][1]), file=results)


## 5. The product that has the most sales, giving the product id and the number of units sold;

# Create dictionary of products and total number of units
products_sales = defaultdict(int)
for row in purchase:
    if row[1] in products_sales:
        products_sales[row[1]] += int(row[2])
    else:
        products_sales[row[1]] = int(row[2])

# Sort from highest to lowest
max_sold = sorted(sorted(products_sales.items()), key=lambda x: x[1], reverse=True)
print('{} {}'.format(max_sold[0][0],round(max_sold[0][1]),1))
print('{} {}'.format(max_sold[0][0],round(max_sold[0][1]),1), file=results)


## 6. The product with the highest total shipping cost, giving the product id and the total cost;

# Create dictionary of products and total shopping cost
products_ship = defaultdict(float)
for row in purchase:
    if row[1] in products_ship:
        products_ship[row[1]] += float(row[-1])
    else:
        products_ship[row[1]] = float(row[-1])
        
# Sort from highest to lowest
max_ship = sorted(sorted(products_ship.items()), key=lambda x: x[1], reverse=True)
print('{} {}'.format(max_ship[0][0],round(max_ship[0][1],1)))
print('{} {}'.format(max_ship[0][0],round(max_ship[0][1],1)), file=results)


## 7. The product with the highest proﬁt (price times quantity less shipping), giving the product and proﬁt;

# Create dictionary of products and total profit
profit = defaultdict(float)
for row in purchase:
    if row[1] in profit:
        profit[row[1]] += product_price[row[1]]*row[2]-row[-1]
    else:
        profit[row[1]] = product_price[row[1]]*row[2]-row[-1]

# Sort from highest to lowest
max_profit = sorted(sorted(profit.items()), key=lambda x: x[1], reverse=True)
print('{} {}'.format(max_profit[0][0],round(max_profit[0][1],1)))
print('{} {}'.format(max_profit[0][0],round(max_profit[0][1],1)), file=results)


## 8. The product with the lowest proﬁt, giving the product and proﬁt;

# Sort from lowest to highest
min_profit = sorted(sorted(profit.items()), key=lambda x: x[1])
print('{} {}'.format(min_profit[0][0],round(min_profit[0][1],1)))
print('{} {}'.format(min_profit[0][0],round(min_profit[0][1],1)), file=results)


## 9. The product with the lowest hover-to-proﬁt ratio, giving the product and ratio;

# Create dictionary with product ID and hover/profit ratio
hover_profit = {}
for row in max_profit:
    hover_profit[row[0]] = hover[row[0]]/row[1]

# Sort from lowest to highest
min_hover_profit = sorted(sorted(hover_profit.items()), key=lambda x: x[1])
print('{} {}'.format(min_hover_profit[0][0],round(min_hover_profit[0][1],1)))
print('{} {}'.format(min_hover_profit[0][0],round(min_hover_profit[0][1],1)), file=results)


## 10. The product with the highest hover-to-proﬁt ratio, giving the product and ratio;

# Sort from highest to lowest
max_hover_profit = sorted(sorted(hover_profit.items()), key=lambda x: x[1], reverse=True)
print('{} {}'.format(max_hover_profit[0][0],round(max_hover_profit[0][1],1)))
print('{} {}'.format(max_hover_profit[0][0],round(max_hover_profit[0][1],1)), file=results)


## 11. The product with the highest read-to-proﬁt ratio, giving the product and ratio;

# Create dictionary with product ID and hover/profit ratio
read_profit = {}
for row in max_profit:
    read_profit[row[0]] = read[row[0]]/row[1]

# Sort from highest to lowest
max_read_profit = sorted(sorted(read_profit.items()), key=lambda x: x[1], reverse=True)
print('{} {}'.format(max_read_profit[0][0],round(max_read_profit[0][1],1)))
print('{} {}'.format(max_read_profit[0][0],round(max_read_profit[0][1],1)), file=results)


### 12. The product with the lowest read-to-proﬁt ratio, giving the product and ratio.

# Sort from lowest to highest
min_read_profit = sorted(sorted(hover_profit.items()), key=lambda x: x[1])
print('{} {}'.format(min_read_profit[0][0],round(min_read_profit[0][1],1)))
print('{} {}'.format(min_read_profit[0][0],round(min_read_profit[0][1],1)), file=results)


## 13. The product with the highest info-to-proﬁt ratio, giving the product and ratio.

# Create dictionary with product ID and info length/profit ratio
info_profit = {}
for row in product_all:
    if profit[row[0]] != 0:
        info_profit[row[0]] = len(row[2].split())/profit[row[0]]
    else:
        info_profit[row[0]] = 0
        
# Sort from highest to lowest
max_info_profit = sorted(sorted(info_profit.items()), key=lambda x: x[1], reverse=True)
print('{} {}'.format(max_info_profit[0][0],round(max_info_profit[0][1],1)))
print('{} {}'.format(max_info_profit[0][0],round(max_info_profit[0][1],1)), file=results)


## 14. The product with the lowest info-to-proﬁt ratio, giving the product and ratio.

# Sort from lowest to highest
min_info_profit = sorted(sorted(info_profit.items()), key=lambda x: x[1])
print('{} {}'.format(min_info_profit[0][0],round(min_info_profit[0][1],1)))
print('{} {}'.format(min_info_profit[0][0],round(min_info_profit[0][1],1)), file=results)