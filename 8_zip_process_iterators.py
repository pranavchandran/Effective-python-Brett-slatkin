names = ['Cecilia', 'Lise', 'Marie']
counts = [len(n) for n in names]
# print(counts)

longest_name = None
max_count = 0

# for i in range(len(names)):
#     count = counts[i]
#     if count > max_count:
#         longest_name = names[i]
#         max_count = count

# print(longest_name, max_count)

for i,name in enumerate(names):
    count = counts[i]
    if count > max_count:
        longest_name = name
        max_count = count

print(longest_name, max_count)

for name, count in zip(names, counts):
    if count > max_count:
        longest_name = name
        max_count = count

print(longest_name, max_count)

import itertools

names.append('Sasangan')
# for name,count in zip(names,counts):
#     print(name,count)

for name,count in itertools.zip_longest(names, counts):
    print(f'{name}:{count}')

def number(n):
    if n > 0:
        number(n-1)
        print(n,end=' ')

print(number(100))

for i in range(3):
    print('loop', i)
    if i == 1: break
else: print('ooh')

for x in []: print('never runs')
else: print('oops')

while False: print("never runs")
else: print('i ll run')

# i = 0
# while i < 10:
#     print(i)
#     i+=1

'''
The else block runs when the numbers are
coprime because the loop doesn’t encounter a break :
'''

a = 4
b = 9

for i in range(2, min(a,b) + 1):
    print('Testing', i)
    if a%1==0 and b%i==0:
        print('Not Coprime')
        break
    else:
        print('Coprime')

def coprime(a, b):
    for i in range(2, min(a,b)+1):
        if a%i==0 and b%i==0:
            return False
    return True

print(coprime(4,9))

# second way
def coprime_alternate(a, b):
    is_coprime = True
    for i in range(2, min(a,b)+1):
        if a%i==0 and b%i==0:
            is_coprime = False
            break
    return is_coprime

    

