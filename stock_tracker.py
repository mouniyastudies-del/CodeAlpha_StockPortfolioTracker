

stocks = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 150,
    "MSFT": 300,
    "AMZN": 200
}

portfolio = {}
total_value = 0

print("=" * 55)
print("📊      WELCOME TO STOCK PORTFOLIO TRACKER")
print("=" * 55)
print("\nAvailable Stocks:")

for stock, price in stocks.items():
    print(f"• {stock}  -->  ${price}")

print("\nType 'DONE' to finish.\n")

while True:
    stock_name = input("Enter Stock Name: ").upper()

    if stock_name == "DONE":
        break

    if stock_name in stocks:
        quantity = int(input("Enter Quantity: "))

        portfolio[stock_name] = quantity

        print("✅ Added Successfully!\n")

    else:
        print("❌ Stock Not Available!\n")

print("\n")
print("=" * 55)
print("📋           YOUR PORTFOLIO SUMMARY")
print("=" * 55)

print(f"{'Stock':<10}{'Qty':<10}{'Price':<10}{'Value'}")
print("-" * 55)

for stock, qty in portfolio.items():
    price = stocks[stock]
    value = price * qty
    total_value += value

    print(f"{stock:<10}{qty:<10}${price:<9}${value}")

print("-" * 55)
print(f"💰 Total Portfolio Value : ${total_value}")
print("=" * 55)

print("\n🙏 Thank you for using Stock Portfolio Tracker!")