'''
sum doesn't have a value set before sum += number
prints a value instead of returning one
prints a string "sum" instead of a value
'''

def century(lst):
    result = []
    for i in lst:
        if type(i) != type(1):
            raise ValueError
    for i in lst:
        if i > 100:
            result.append(i)
    result = list(set(result))
    return result

'''
It opens a file and reads each line. Stores each word in a list without punctuation (,) 
and returns a sum of the first element in each row.
'''

'''
They should add a f.close() statement since they are likely dealing with a file to close that connection.
'''



'''
False
False
False
False
False
False   
'''
'''
import PIL.Image as pim

image = pim.new("RGB", (64, 64))

for i in range(64):
    for j in range(32):
        image.putpixel((i, j), (255,0,0))

for i in range(64):
    for j in range(32, 64):
        image.putpixel((i, j), (0,0,255))
image.save("output.png")
'''

row = [0 ,1, 2, 3, 4]

data = []
for i in range(10):
    data.append(row)

col4 = []
for i in data:
    col4.append(i[3])

print(min(col4))
print(max(col4))

'''
O(n)
O(1)
O(n)
O(1)
O(1)
O(n**2)
'''

'''
<html>
<body>
<h1> MELBOURNE BUSINESS SCHOOL (The University of
Melbourne)
MBUSA90500 Programming, Module 2 2015
Programming Practice Exam </h1>
<p> <b> Identical Examination papers: </b> None. </p>
</body.
</html>'''


def read_cards(filename):
    fp = open(filelname)
    content = []
        for line in fp.readlines():
            content.append(line)
    fp.close()
    return content

def print_cards(content)
    print(content)