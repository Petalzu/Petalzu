
import math
class circular_shape():
    def __init__(self,radius):
        self.radius = radius

class circle(circular_shape):
    def __init__(self, radius):
        super().__init__(radius)
    
    def get_area(self,radius):
        area = math.pi*radius**2
        return area

class circular_column(circular_shape):
    def __init__(self,radius,high):
        super().__init__(radius)
        self.high = high

    def get_area(self,radius,high):
        area = 2*math.pi*radius**2 + radius*2*math.pi*high
        return area

circle1 = circle(2)
area1 = circle1.get_area(circle1.radius)
circle2 = circular_column(2,2)
area2 = circle2.get_area(circle2.radius,circle2.high)
print(area1,area2)