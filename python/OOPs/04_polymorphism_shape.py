class shape :
    def area (self) :
        print("Area of Shape !")

class Circle(shape) :
    def area(self, radius) :
        print(f"Area of the circle is : {3.14*radius*radius} ")

class Rectangle(shape) :
    def area(self, l , b) :
        print(f"Area of the Rectangle is : {l*b}")

class Triangle(shape) :
    def area(self, l , b) :
        print(f"Area of the Triangle is : { l * b }")


c1 = Circle();
r1 = Rectangle();
t1 = Triangle();

c1.area(10)
r1.area(10,5)
t1.area(10,20)
