# Module 5, Problem 5: Income tax
last_name = input("Enter your last name: ")
dependents = int(input("Enter the number of dependents: "))
gross_income = float(input("Enter gross income: "))

adjusted_gross_income = gross_income - dependents * 12000

if adjusted_gross_income > 50000:
    tax_rate = 0.20
else:
    tax_rate = 0.10

income_tax = adjusted_gross_income * tax_rate

if income_tax < 0:
    income_tax = 100.00

print(f"Last name: {last_name}")
print(f"Gross income: ${gross_income:.2f}")
print(f"Number of dependents: {dependents}")
print(f"Adjusted gross income: ${adjusted_gross_income:.2f}")
print(f"Income tax: ${income_tax:.2f}")
