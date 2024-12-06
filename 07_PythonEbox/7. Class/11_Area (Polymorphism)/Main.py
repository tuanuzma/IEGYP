class Shape:
    def area(self):
        pass  # Base method, not used directly


class CalAreaSquare(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        print(f"Side of Square : {self.side}")
        print(f"Area of Square : {self.side ** 2:.2f}")


class CalAreaRectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        print(f"Length of Rectangle : {self.length}")
        print(f"Breadth of Rectangle : {self.width}")
        print(f"Area of Rectangle : {self.length * self.width}")


class CalAreaTriangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        print(f"Base of Triangle : {self.base}")
        print(f"Height of Triangle : {self.height}")
        print(f"Area of Triangle : {0.5 * self.base * self.height:.2f}")


class CalAreaCircle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        print(f"Radius of Circle : {self.radius}")
        print(f"Area of Circle : {3.14 * self.radius ** 2:.2f}")


def main():
    print("Select an Option")
    print("1.Square")
    print("2.Rectangle")
    print("3.Triangle")
    print("4.Circle")

    choice = int(input())
    if choice == 1:
        print("Enter the side")
        side = float(input())
        square = CalAreaSquare(side)
        square.area()
    elif choice == 2:
        print("Enter the length")
        length = int(input())
        print("Enter the breadth")
        width = int(input())
        rectangle = CalAreaRectangle(length, width)
        rectangle.area()
    elif choice == 3:
        print("Enter the base")
        base = int(input())
        print("Enter the height")
        height = int(input())
        triangle = CalAreaTriangle(base, height)
        triangle.area()
    elif choice == 4:
        print("Enter the radius")
        radius = int(input())
        circle = CalAreaCircle(radius)
        circle.area()
    else:
        print("Invalid Option")


if __name__ == "__main__":
    main()