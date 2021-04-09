from urllib.parse import parse_qs

my_values = parse_qs('red=5&blue=0&green=',keep_blank_values=True)
print(my_values)

green_str = my_values.get('green', [''])
print(green_str)
if green_str[0]:
    green = int(green_str[0])
else:
    green = 0

def get_first_int(values, key, default=0):
    found = values.get(key,[''])
    if found[0]:
        return int(found[0])
    return default

print(get_first_int(my_values, 'red'))
