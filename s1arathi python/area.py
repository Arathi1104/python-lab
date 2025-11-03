#r=int(input("enter radius:"))
#circlearea=3.14*r*r
#print("area of the circle is",circlearea)
#l=int(input("enter length:"))
#b=int(input("enter breadth:"))
#rectarea=l*b
#print("area of the rectangle is",rectarea)


def circle_area(r):
    area = 3.14 * r * r
    return area

def rectangle_area(l, b):
    area = l * b
    return area


r =int(input("Enter radius: "))
print("Area of the circle is", circle_area(r))


l = int(input("Enter length: "))
b = int(input("Enter breadth: "))
print("Area of the rectangle is", rectangle_area(l, b))
