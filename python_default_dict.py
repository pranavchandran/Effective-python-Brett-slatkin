from collections import defaultdict
print(issubclass(defaultdict, dict))
'''
# correct instantiation
def_dict = defaultdict(list)
def_dict['one'] = 1
def_dict['missing']
def_dict['another_missing'].append(4)
def_dict['lil_missing'] = 5

# print(def_dict)
# for x,y in def_dict.items():
#     if y == []: print(x)

# Example1
dd = defaultdict(list)
dd['key'].append(1)
dd['key'].append(2)
dd['key'].append(3)
dd['pranav']
print(dd)

# Creating a tuple objects like this
dep = [('Sales', 'John Doe'),
       ('Sales', 'Martin Smith'),
       ('Accounting', 'Jane Doe'),
       ('Marketing', 'Elizabeth Smith'),
       ('Marketing', 'Adam Doe')]

dep_dd = defaultdict(list)
for department,employee in dep:
    dep_dd[department].append(employee)

print(dep_dd)

# Using normal dict
dep_d = dict()
for department, employee in dep:
    dep_d.setdefault(department, []).append(employee)

# counts the number of employees in department
dep = [('Sales', 'John Doe'),
       ('Sales', 'Martin Smith'),
       ('Accounting', 'Jane Doe'),
       ('Marketing', 'Elizabeth Smith'),
       ('Marketing', 'Elizabeth Smith'),
       ('Marketing', 'Adam Doe'),
       ('Marketing', 'Adam Doe'),
       ('Marketing', 'Adam Doe')]


# dep_n = defaultdict(set)
# for department,employee in dep:
#     dep_n[department]= employee
# print(dep_n)

dd = defaultdict(int)
for department,_ in dep:
    dd[department]+=1
print(dd)

dep = [('Sales', 'John Doe'),
       ('Sales', 'Martin Smith'),
       ('Accounting', 'Jane Doe'),
       ('Marketing', 'Elizabeth Smith'),
       ('Marketing', 'Elizabeth Smith'),
       ('Marketing', 'Adam Doe'),
       ('Marketing', 'Adam Doe'),
       ('Marketing', 'Adam Doe')]

# dep_dd = defaultdict(set)
# for department, employee in dep:
#     dep_dd[department].add(employee)
# print(dep_dd)


in_dep = defaultdict(set)
for department, employee in dep:
    in_dep[employee].add(department)
print(in_dep)

dd = defaultdict(int)
s = 'mississippi'
for letter in s:
    dd[letter] += 1
print(dd)

from collections import Counter
counter = Counter('missisippi')
print(counter)

dep = Counter(dep)
print(dep)
'''
# Next, you process the data using Python and get the following list of tuple objects:
# With this data, you want to calculate the total income per product.
incomes = [('Books', 1250.00),
           ('Books', 1300.00),
           ('Books', 1420.00),
           ('Tutorials', 560.00),
           ('Tutorials', 630.00),
           ('Tutorials', 750.00),
           ('Courses', 2500.00),
           ('Courses', 2430.00),
           ('Courses', 2750.00),]

dd_f = defaultdict(float)
for product, income in incomes:
    dd_f[product] += income

print(dd_f)

for product, income in dd_f.items():
    print(f'Total income {product}: ${income}')

print(set(dir(defaultdict)) - set(dir(dict)))

from collections import defaultdict

dd_s = dict()
dd_s.setdefault('pr', list())
dd_s['pr']
print(dd_s)

for x in range(1,10):
    dd_s['pr'].append(x)

print(dd_s)

# Default factory
dd = defaultdict(list, letters=['a', 'b', 'c'])
print(dd.default_factory)
dd['pranav']
dd['pranav'].append(2)
dd['numbers'] += [2,3]
print(dd)
print(dd.keys())

dd01 = defaultdict(list)
print(dd01)

dd01['string']='some_string'
dd01['rent']=100
print(dd01)

dd01.default_factory = int
dd01['raju']
print(dd01)


