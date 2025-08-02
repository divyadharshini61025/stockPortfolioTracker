stock_prices = {"AAPL": 180, "TSLA": 250, "GOOGL": 2000}
total = 0

while True:
    stock = input("Enter stock symbol (or 'done'): ").upper()
    if stock == 'DONE':
        break
    qty = int(input(f"Enter quantity of {stock}: "))
    price = stock_prices.get(stock, 0)
    total += price * qty

print("Total investment value: $", total)
