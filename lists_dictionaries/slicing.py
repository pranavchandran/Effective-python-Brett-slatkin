a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
print('Middle Two :', a[3:5])
print('All but ends :', a[1:-1])

# [start:end:stride]
x = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
odds = x[::2]
evens = x[1::2]
print(odds)
print(evens)

# reverse
y = x[::-1]
print(y)

x = 'ᇓৌ'
y = x[::-1]
print(y)

x = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
# x[::2]
# # ['a', 'c', 'e', 'g']
# x[::-2] # ['h', 'f', 'd', 'b']

# x[2::2]
# x[-2::-2]
# x[-2:2:-2]
print(x[2:2:-1])

def generate_csv():
    yield ('Date', 'Make', 'Model', 'Year', 'Price')

all_csv_files = list(generate_csv())
header = all_csv_files[0]
rows = all_csv_files[1:]
print('Csv Header:', header)
print('Row Count:', len(rows))

it = generate_csv()
header, *rows = it
print('CSV header:', header)
print('Row count:', len(rows))

numbers = [95,232,543,123,23]
numbers.sort()
print(numbers, id(numbers))


