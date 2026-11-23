def miles_per_gallon(miles, gallons):
    if gallons == 0:
        return 0
    return miles / gallons


tripCount = 0
again = "Y"
while again == "Y":
    city = input("Enter destination city: ")
    miles = float(input("Enter miles traveled: "))
    gallons = float(input("Enter gallons used: "))
    mpg = miles_per_gallon(miles, gallons)
    print("Destination:", city)
    print("Miles:", miles)
    print("MPG:", format(mpg, ".2f"))
    tripCount = tripCount + 1
    again = input("Enter Y to continue or N to stop: ").upper()
print("Number of trips:", tripCount)
