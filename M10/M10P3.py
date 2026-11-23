def out_the_door_price(msrp, make, model, electric_code):
    if electric_code.upper() == "Y":
        discount = 0.30
    elif make.lower() == "honda" and model.lower() == "accord":
        discount = 0.10
    elif make.lower() == "toyota" and model.lower() in ("rav4", "rav 4"):
        discount = 0.15
    else:
        discount = 0.05
    discounted_price = msrp * (1 - discount)
    return discounted_price * 1.07

msrp_total = 0
sales_total = 0
again = input("Do you want to enter a car? (Yes or No): ").lower()
while again == "yes":
    make = input("Enter make: ")
    model = input("Enter model: ")
    electric = input("Is it electric? (Y or N): ").upper()
    msrp = float(input("Enter MSRP: "))
    sale_price = out_the_door_price(msrp, make, model, electric)
    print("Out the Door Price: $", format(sale_price, ".2f"))
    msrp_total += msrp
    sales_total += sale_price
    again = input("Do you want to enter a car? (Yes or No): ").lower()
print("Total MSRP: $", format(msrp_total, ".2f"))
print("Total Sales Price: $", format(sales_total, ".2f"))
