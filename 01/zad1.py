first_x = float(input("X coordinate of the first circle: "))
first_y = float(input("Y coordinate of the first circle: "))
first_radius = float(input("Radius of the first circle: "))
second_x = float(input("X coordinate of the second circle: "))
second_y = float(input("Y coordinate of the second circle: "))
second_radius = float(input("Radius of the second circle: "))

intersection = (first_x - second_x)**2 + (first_y - second_y)**2 <= (first_radius + second_radius)**2
if intersection:
    print("\nCircles intersect")
else:
    print("\nCircles do not intersect")