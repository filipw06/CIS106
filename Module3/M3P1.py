# M3P1 - Stock investment
# Input: Ticker symbol; number of shares; cost per share
# Process: amount_invested = number_of_shares * cost_per_share
# Output: Ticker symbol; amount invested

ticker_symbol = input("Enter the stock ticker symbol: ")
number_of_shares = float(input("Enter the number of shares: "))
cost_per_share = float(input("Enter the cost per share: "))

amount_invested = number_of_shares * cost_per_share

print(f"Stock ticker symbol: {ticker_symbol}")
print(f"Amount invested: ${amount_invested:.2f}")
