fresh_fruit = {
'apple': 10,
'banana': 1,
'lemon': 2,
}
class OutOfBananas(Exception):
    pass

def out_of_stock():
    for x in fresh_fruit:
        if fresh_fruit[x] == 0:
            print("Out of stock", x)
'''
print(type(fresh_fruit))

def make_lemonade(count):
    for x in fresh_fruit:
        if fresh_fruit[x] != 0:
            print("In stock", x)

def out_of_stock():
    for x in fresh_fruit:
        if fresh_fruit[x] == 0:
            print("Out of stock", x)

def make_cider(count):
    if count >= 4:
        print("Making cider")


# python3.8
# if count:= fresh_fruit.get('lemon', 0):
#     make_lemonade(count)
# else:
#     out_of_stock()

# python3.8
if (count:=fresh_fruit.get('apple', 0))>=4:
    make_cider(count)
else:
    out_of_stock()
'''
def slice_bananas(count):
    if count >=2:
        return count * 2

class OutOfBananas(Exception):
    pass

def make_smoothies(count):
    if count >=4:
        return True
    raise OutOfBananas('lol')

# python3.8
# pieces = 0
# if(count:=fresh_fruit.get('banana',0))>=2:
#     pieces = slice_bananas(count)
#     print(f'we have {pieces} pieces')
# try:
#     smoothies = make_smoothies(pieces) 
# except OutOfBananas:
#     out_of_stock()

# python 3
# pieces = 0
# count = fresh_fruit.get('banana', 0)
# if count >= 2:
#     pieces = slice_bananas(count)
# try:
#     smoothies = make_smoothies(pieces)
# except OutOfBananas:
#     out_of_stock()

# count = fresh_fruit.get('banana', 0)
# if count >= 2:
#     pieces = slice_bananas(count)
#     print(pieces)
# else:
#     pieces = 0
# try:
#     smoothies = make_smoothies(pieces)
# except OutOfBananas:
#     out_of_stock()

# python3.8
# if (count := fresh_fruit.get('banana', 0)) >= 2:
#     pieces = slice_bananas(count)
#     to_enjoy = make_smoothies(pieces)
# elif (count := fresh_fruit.get('apple', 0)) >= 4:
#     to_enjoy = make_cider(count)
# elif count := fresh_fruit.get('lemon', 0):
#     to_enjoy = make_lemonade(count)
# else:
#     to_enjoy = 'Nothing'

# if (count:=fresh_fruit.get('apple'))>0:
#     print('disco ')

# bottles = []
# while True:
#     fresh_fruit = pick_fruit()
#     if not fresh_fruit:
#         break
#     for fruit, count in fresh_fruit.items():
#         batch = make_juice(fruit, count)
#         bottles.extend(batch)

import random
def pick_fruit():
    a = (random.choice(list(fresh_fruit.items())))
    fruit, count = a     
    basket = {fruit:count}
    return basket

def make_juice(fruit, count):
    if (count:=fresh_fruit.get(fruit))>0:
        print(fruit + ' Juice')
        return (fruit,count)
    else:
        print("no stock")
# pick_fruit()
# prefered approach
bottles = []
point = 0
while (fresh_fruit:= pick_fruit()) and point<=0:
    for fruit, count in fresh_fruit.items():
        batch = make_juice(fruit, count)
        bottles.extend(batch)
        print(bottles)
        point+=1
        
