# Module 6 Logic

## M6P1 - Widgets
Input: quantity of widgets.
1. If quantity > 10000, set price to $10.
2. Otherwise, if quantity >= 5000, set price to $20; otherwise set price to $30.
3. Extended price = quantity * price.
4. Tax = extended price * 0.07.
5. Total = extended price + tax.
Output: extended price, tax, total.

## M6P2 - Parts
Input: part number (string), quantity.
1. If part number is "10" or "55", set unit cost to $1.
2. Otherwise, if it is "99", set unit cost to $2.
3. Otherwise, if it is "80" or "70", set unit cost to $3.
4. Otherwise set unit cost to $5.
5. Total cost = quantity * unit cost.
Output: part number, unit cost, total cost.

## M6P3 - CD Interest
Input: principal amount, years to maturity.
1. If principal > $100000 AND years = 5, set rate to 6%.
2. Otherwise, if $50000 <= principal <= $100000 AND years = 10, set rate to 5%.
3. Otherwise, if $50000 <= principal <= $100000 AND years = 5, set rate to 4%.
4. Otherwise set rate to 2%.
5. First-year interest = principal * rate.
Output: principal, interest rate, first-year interest.

## M6P4 - Concert Tickets
Input: number of tickets.
1. If quantity >= 25, set price per ticket to $50.
2. Otherwise, if quantity >= 10, set price to $60.
3. Otherwise, if quantity >= 5, set price to $70.
4. Otherwise set price to $75.
5. Total cost = number of tickets * price per ticket.
Output: number of tickets, price per ticket, total cost.

## M6P5 - Employee Bonus
Input: employee last name, salary, job level.
1. If job level >= 10, set bonus rate to 25%.
2. Otherwise, if job level >= 5, set bonus rate to 20%.
3. Otherwise set bonus rate to 10%.
4. Bonus = salary * bonus rate.
Output: employee last name, bonus.
