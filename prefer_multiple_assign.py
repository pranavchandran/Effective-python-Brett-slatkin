snack_calories = {
'chips': 140,
'popcorn': 80,
'nuts': 190,
}

# print(snack_calories)
items = tuple(snack_calories.items())
print(items)

for x in items:
    if 'chips' in x:
        print(x)

# the values in tuples can be accessed through numerical indexes
item = ('Peanut butter', 'Jelly')
# first = item[0]
# second = item[1]
first, second = item
print(first ,'and ', second)

favorite_snacks = {
'salty': ('pretzels', 100),
'sweet': ('cookies', 180),
'veggie': ('carrots', 20),
}

((type1, (name1, cals1)),
(type2, (name2, cals2)),
(type3, (name3, cals3))) = favorite_snacks.items()

for x,y in favorite_snacks.items():
# print(f'Favorite {type1} is {name1} with {cals1} calories')
    print(f'Favorite {x} is {y[0]} with {y[1]} calories')

# def bubble_sort(a):
#     for _ in range(len(a)):
#         for i in range(1, len(a)):
#             print(i)
#             if a[i] < a[i-1]:
#                 temp = a[i]
#                 a[i] = a[i-1]
#                 a[i-1] = temp

# names = ['pretzels', 'carrots', 'arugula', 'bacon']
# bubble_sort(names)
# print(names)
    


