class Tool:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def __repr__(self):
        return f'Tool({self.name!r}, {self.weight})'

tools = [
    Tool('level', 3.5),
    Tool('hammer', 1.25),
    Tool('Screwdriver', 0.5),
    Tool('Chisel', 0.25)
]
# print(tools)
print('Unsorted', repr(tools))
tools.sort(key=lambda x: x.name)
print('\nsorted', tools)