# M8P1 - Five years of compound interest.
principal = float(input("Enter principal amount: "))
rate = float(input("Enter interest rate as a decimal (0.10 for 10%): "))
total_interest = 0.0
print(f"{'Year':<6}{'Beginning Balance':>20}{'Ending Balance':>20}")
for year in range(1, 6):
    beginning_balance = principal
    interest = beginning_balance * rate
    principal = beginning_balance + interest
    total_interest = total_interest + interest
    print(f"{year:<6}{'$' + format(beginning_balance, ',.2f'):>20}{'$' + format(principal, ',.2f'):>20}")
print(f"Total interest earned: ${total_interest:,.2f}")
