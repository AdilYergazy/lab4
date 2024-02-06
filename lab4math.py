import math


# 1
def radians():
    cen = int(input('Input degree:'))
    rad = math.radians(cen)
    return f'Output radian:', rad


print(*radians())


# 2
def trapezoid():
    height = int(input('Height:'))
    base = int(input('Base, first value:'))
    base2 = int(input('Base, second value:'))
    rad = height * (base + base2) / 2
    return f'Expected Output:', rad


print(*trapezoid())


# 3
def area():
    base = int(input('Input number of sides:'))
    base2 = int(input('Input the length of a side:'))
    return f'The area of the polygon is:', base * base2


print(*area())


def parallelogram():
    base = int(input('Length of base:'))
    base2 = int(input('Height of parallelogram:'))
    return f'Expected Output:', base * base2


print(*parallelogram())
