# Module 5, Problem 4: Appliance warranty
appliance_name = input("Enter the appliance name: ")
appliance_cost = float(input("Enter the appliance cost: "))

if appliance_cost > 1000.00:
    warranty_cost = appliance_cost * 0.10
else:
    warranty_cost = appliance_cost * 0.05

total = appliance_cost + warranty_cost

print(f"Appliance: {appliance_name}")
print(f"Appliance cost: ${appliance_cost:.2f}")
print(f"Warranty cost: ${warranty_cost:.2f}")
print(f"Total: ${total:.2f}")
