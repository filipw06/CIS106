# M3P5 - Circle area and perimeter
# Input: Circle radius
# Process: pi = 3.14; area = pi * radius * radius; perimeter = 2 * pi * radius
# Output: Area in square units; perimeter in units

radius = float(input("Enter the radius of the circle: "))

pi = 3.14
area = pi * radius * radius
perimeter = 2 * pi * radius

print(f"Area: {area:.2f} square units")
print(f"Perimeter: {perimeter:.2f} units")
