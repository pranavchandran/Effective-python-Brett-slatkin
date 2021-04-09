from random import randint

random_bits = 0
for i in range(32):
    if randint(0, 1):
        random_bits |= 1 << 1

print(bin(random_bits))

flavor_list = ['vanilla', 'chocolate', 'pecan', 'strawberry']
for flavor in flavor_list:
    print(f'{flavor} is delicious')

for i in range(len(flavor_list)):
    flavor = flavor_list[i]
    print(f'{i+1}: {flavor}')

it = enumerate(flavor_list)
print(it)
print(next(it))

for i, flavor in enumerate(flavor_list):
    print(f'{i + 1}: {flavor}')
