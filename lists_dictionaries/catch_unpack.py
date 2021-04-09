car_ages = [0, 9, 4, 8, 7, 20, 19, 1, 6, 15]
car_ages_desc = sorted(car_ages,reverse=True)
#print(car_ages_desc)

oldest = car_ages_desc[0]
second_oldest = car_ages_desc[1]
others = car_ages_desc

#print(oldest, second_oldest, others)

#second metod is more elogant
oldest, second_oldest, *others = car_ages_desc
#print(oldest, second_oldest, others)

#* can used at any place
oldest, *others, youngest = car_ages_desc
#print(oldest, youngest, others)

#find second youngest and youngest
*others, second_youngest, youngest = car_ages_desc
#print(youngest, second_youngest, others)
oth_list = car_ages_desc.copy()
print(oth_list)
print(id(oth_list), id(car_ages_desc))

car_inventory = {
    'Downtown': ('silver Shadow', 'Pinto', 'DMC'),
    'Airport': ('Skyline', 'Viper', 'Gremlin', 'Nova')
}

((loc1, (best1, *rest1)),(loc2, (best2, *rest2)))= car_inventory.items()

print(f'Best at {loc1} is {best1}, {len(rest1)} others')
print(f'Best at {loc2} is {best2}, {len(rest2)} others')

short_list = [1, 2]
first, second, *rest = short_list
print(first, second, rest)
print(short_list)

it = iter(range(1,3))
print(it)
one,two = it
print(f'{one} {two}')

