def assessed_value(county, market_value):
    county = county.lower()
    if county == "cook":
        percent = 0.90
    elif county == "dupage":
        percent = 0.80
    elif county == "mchenry":
        percent = 0.75
    elif county == "kane":
        percent = 0.60
    else:
        percent = 0.70
    return market_value * percent

total_market = 0
total_assessed = 0
again = input("Do you want to enter a home? (Yes or No): ").lower()
while again == "yes":
    county = input("Enter county: ")
    market = float(input("Enter market value: "))
    assessed = assessed_value(county, market)
    print("County:", county)
    print("Assessed Value: $", format(assessed, ".2f"))
    total_market += market
    total_assessed += assessed
    again = input("Do you want to enter a home? (Yes or No): ").lower()
print("Total Market Values: $", format(total_market, ".2f"))
print("Total Assessed Values: $", format(total_assessed, ".2f"))
