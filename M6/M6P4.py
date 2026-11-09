# Module 6, Problem 4: Concert tickets
number_of_tickets = int(input("Enter the number of concert tickets: "))

if number_of_tickets >= 25:
    price_per_ticket = 50.00
elif number_of_tickets >= 10:
    price_per_ticket = 60.00
elif number_of_tickets >= 5:
    price_per_ticket = 70.00
else:
    price_per_ticket = 75.00

total_cost = number_of_tickets * price_per_ticket

print()
print(f"{'Number of tickets:':<22} {number_of_tickets:>14}")
print(f"{'Price per ticket:':<22}${price_per_ticket:>14,.2f}")
print(f"{'Total cost:':<22}${total_cost:>14,.2f}")
