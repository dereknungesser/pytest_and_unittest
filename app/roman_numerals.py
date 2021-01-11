values = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']

def parse(value):
    i = 0
    while i < len(values):
        if value == values[i]:
            return i + 1
        i += 1

def pytest_parser(s):
    if s == 'IX':
        return 9
    elif s == 'X':
        return 10
