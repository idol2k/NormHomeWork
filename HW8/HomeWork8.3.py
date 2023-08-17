class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2
    
    def __sub__(self, other):
        difference = abs(self.radius - other.radius)
        if difference == 0:
            return Dot(0, 0)
        return difference
    
class Dot:
    def __init__(self, x, y):
        self.x = x
        self.y = y

circle1 = Circle(12)
circle2 = Circle(24)
print(circle1 - circle2)