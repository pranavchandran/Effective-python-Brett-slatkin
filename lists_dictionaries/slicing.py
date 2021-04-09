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

