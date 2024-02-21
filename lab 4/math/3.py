import math

def polygon_area(n, s):
    area = (n * s**2) / (4 * math.tan(math.pi / n))
    return area

num_sides = int(input("Input number of sides: "))
side_length = float(input("Input the length of a side: "))

area = int(polygon_area(num_sides, side_length))

print("The area of the polygon is:", area)
