import math

figure = input()

if figure == "square":
    square_side = float(input())
    square_area = square_side * square_side
    print(f"{square_area: .3f}")
elif figure == "rectangle":
    rectangle_side1 = float(input())
    rectangle_side2 = float(input())
    rectangle_area = (rectangle_side1 * rectangle_side2)
    print(f"{rectangle_area: .3f}")
elif figure == "circle":
    circle_radius = float(input())
    circle_area = math.pi * circle_radius * circle_radius
    print(f"{circle_area: .3f}")
elif figure == "triangle":
    triangle_side = float(input())
    triangle_height = float(input())
    triangle_area = (triangle_side * triangle_height) / 2
    print(f"{triangle_area: .3f}")
else:
    print("Ivalid input.")