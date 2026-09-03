
import math  

class Circle:
    def __init__(self, radius):
        self.radius = radius  

    def get_area(self):
        return math.pi * self.radius ** 2  


circle = Circle(5)  
print("El área del círculo es:", circle.get_area())
