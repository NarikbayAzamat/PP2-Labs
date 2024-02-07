from math import sqrt

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(f"({self.x}, {self.y})")

    def move(self):
        self.x += int(input())
        self.y += int(input())

    def dist(self, otherPoint):
        dx = self.x - otherPoint.x
        dy = self.y - otherPoint.y
        distance = sqrt(dx**2 + dy**2)
        return distance

point1 = Point(3, 4)
point2 = Point(7, 1)

point1.show()
point2.show()

print(point1.dist(point2))

point1.move()
point1.show()

    
