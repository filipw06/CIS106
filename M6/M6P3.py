# Module 6, Problem 3: CD interest
principal = float(input("Enter the principal amount: "))
years_to_maturity = int(input("Enter the years to maturity: "))

if principal > 100000 and years_to_maturity == 5:
    interest_rate = 0.06
elif 50000 <= principal <= 100000 and years_to_maturity == 10:
    interest_rate = 0.05
elif 50000 <= principal <= 100000 and years_to_maturity == 5:
    interest_rate = 0.04
else:
    interest_rate = 0.02

first_year_interest = principal * interest_rate

print()
print(f"{'Principal:':<22}${principal:>14,.2f}")
print(f"{'Interest rate:':<22} {interest_rate:>14.2%}")
print(f"{'First-year interest:':<22}${first_year_interest:>14,.2f}")
