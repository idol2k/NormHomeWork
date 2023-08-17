class Sphere:
    
    @staticmethod
    def area(radius):
        return 4 * 3.14 * radius ** 2
    
    @classmethod
    def main(cls, radius):
        radius += 2
        return cls.area(radius)
    
print(Sphere.main(1))
