def compute_total(qty, unitprice):
    extprice = qty * unitprice
    if extprice > 10000:
        extprice = extprice * 0.90
    return extprice


totalExtPrice = 0
again = "Y"
while again == "Y":
    qty = int(input("Enter quantity: "))
    price = float(input("Enter unit price: "))
    extprice = compute_total(qty, price)
    print("Quantity:", qty)
    print("Unit price: $", format(price, ".2f"))
    print("Extended price: $", format(extprice, ".2f"))
    totalExtPrice = totalExtPrice + extprice
    again = input("Enter Y to continue or N to stop: ").upper()
print("Total extended price: $", format(totalExtPrice, ".2f"))
