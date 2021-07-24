row = [0 ,1, 2, 3, 4]

data = []
for i in range(21):
    data.append(row)

print(data)

def sum_even(data, colname):
    total = 0
    for i in range(len(data)):
        total += data[i][colname]
    if total // 2 == 0:
        return True
    else:
        return False

#print(sum_even(data, 2))

def odd_total(intlist):
    total = 0
    for i in intlist:
        if i % 2 != 0:
            total += 1
    return total

yo = [1,2,3,4,2,34,22,435,4325,5,423,4325,34,3]

print(odd_total(yo))

a = "andrew loves llamas"


hm = a or False
print(hm)
print(a and True)
#print(a + 3)

print('\n')


class Player:
    def __init__(self, height, footwork):
        self.height = height
        self.footwork = footwork

    def is_singles_player(self):
        if self.height > 180 and self.footwork == "fast":
            return True
        else:
            return False

Player1 = Player(190, 'fast')
Player2 = Player(170, 'fast')
Player3 = Player(192, 'slow')
Player4 = Player(165, 'slow')

print(Player1.is_singles_player())
print(Player2.is_singles_player())
print(Player3.is_singles_player())
print(Player4.is_singles_player())

ps = [Player(180, 'fast'), Player(190, 'slow')]

import random
print(random.randint(0,1))

def serve_order(playerlist):
    if len(playerlist) != 2:
        return None
    else:
        order = []
        first_serve = random.randint(0,1)
        if first_serve == 0:
            order.append(playerlist[0])
            order.append(playerlist[1])
        else:
            order.append(playerlist[1])
            order.append(playerlist[0])
        return order

print(serve_order(ps))

import json
x = json.loads("""{"a":1, "1":"a"}""")
#y = json.loads("andrew")
#z = json.loads('["a", "[", "a", "]"]')
print(type(x))
#print(type(y))
#print(type(z))

new_list = []
for i in range(len(new_list)):
    print(i)

for i in range(1000):
    print(random.randint(0,2))