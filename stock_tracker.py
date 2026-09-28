# CodeAlpha Internship - Task 2
# Stock Portfolio Tracker

# Predefined stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 400,
    "AMZN": 190
}

portfolio = {}

print("=" * 40)
print(" STOCK PORTFOLIO TRACKER")
print("=" * 40)

print("\nAvailable stocks:")
for stock, price in stock_prices.items():
    print(f"{stock}: ${price}")

# Get stock details from the user
while True:
    stock = input(
        "\nEnter stock name (or 'done' to finish): "
    ).strip().upper()

    if stock == "DONE":
        break

    if stock not in stock_prices:
        print("Invalid stock name. Please try again.")
        continue

    try:
        quantity = int(input("Enter quantity: "))

        if quantity <= 0:
            print("Quantity must be greater than zero.")
            continue

        portfolio[stock] = portfolio.get(stock, 0) + quantity

        print("Stock added successfully!")

    except ValueError:
        print("Please enter a valid whole number.")

# Calculate total investment
total_investment = 0

print("\n" + "=" * 40)
print(" YOUR PORTFOLIO")
print("=" * 40)

for stock, quantity in portfolio.items():
    price = stock_prices[stock]
    value = price * quantity

    total_investment += value

    print(
        f"{stock}: {quantity} shares x "
        f"${price} = ${value}"
    )

print("-" * 40)
print(f"Total Investment: ${total_investment}")
print("=" * 40)

# Save portfolio details to a text file
with open("portfolio.txt", "w") as file:
    file.write("STOCK PORTFOLIO REPORT\n\n")

    for stock, quantity in portfolio.items():
        price = stock_prices[stock]
        value = price * quantity

        file.write(
            f"{stock}: {quantity} shares = ${value}\n"
        )

    file.write(
        f"\nTotal Investment: ${total_investment}"
    )

print("\nPortfolio saved to portfolio.txt")
print("Thank you for using Stock Portfolio Tracker!")

