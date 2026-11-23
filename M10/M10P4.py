def ticket_price(miles):
    if miles >= 30:
        return 12
    elif miles >= 20:
        return 10
    elif miles >= 10:
        return 8
    else:
        return 5

total_tickets = 0
again = input("Do you want to enter a ticket? (Yes or No): ").lower()
while again == "yes":
    last_name = input("Enter last name: ")
    miles = float(input("Enter miles from downtown Chicago: "))
    price = ticket_price(miles)
    print("Last Name:", last_name)
    print("Ticket Price: $", format(price, ".2f"))
    total_tickets += price
    again = input("Do you want to enter a ticket? (Yes or No): ").lower()
print("Total Ticket Prices: $", format(total_tickets, ".2f"))
