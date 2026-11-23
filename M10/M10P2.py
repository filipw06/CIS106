def wall_area(length, width, height):
    return 2 * length * height + 2 * width * height


def ceiling_area(length, width):
    return length * width

again = input("Do you want to calculate paint? (Yes or No): ").lower()
while again == "yes":
    length = float(input("Enter room length: "))
    width = float(input("Enter room width: "))
    height = float(input("Enter room height: "))
    walls = wall_area(length, width, height)
    gallons = walls / 50
    print("Wall Square Footage:", format(walls, ".2f"))
    print("Gallons for Walls:", format(gallons, ".2f"))
    ceiling = ceiling_area(length, width)
    print("Ceiling Area:", format(ceiling, ".2f"))
    print("Gallons for Ceiling (at 50 sq ft per gallon):", format(ceiling / 50, ".2f"))
    again = input("Do you want to calculate paint? (Yes or No): ").lower()
