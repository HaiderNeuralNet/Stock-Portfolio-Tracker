stock_prices = {
     "NFLX": 620,
    "META": 500,
    "NVDA": 800,
    "UBER": 70,
    "DIS": 110
}

print("Hey! Welcome to your Stock Portfolio Tracker ")
print("Let's see how much your stocks are worth.")
print()
print("Here are the stocks we have today:")
for stock, price in stock_prices.items():
    print(f"  {stock} — ${price} per share")
print()

portfolio = {}

while True:
    name = input("Which stock do you want to add? (or type 'done' when finished): ").upper().strip()

    if name == "DONE":
        if not portfolio:
            print("You didn't add any stocks. Come back anytime!")
        break

    if name not in stock_prices:
        print(f"Hmm, we don't have '{name}' in our list. Please pick from the available stocks.")
        continue

    try:
        qty = int(input(f"How many shares of {name} do you own? "))
        if qty <= 0:
            print("Please enter a number greater than 0.")
            continue
    except ValueError:
        print("That doesn't look like a number. Try again.")
        continue

    portfolio[name] = qty
    print(f"Got it! Added {qty} shares of {name}.\n")

if portfolio:
    print("\nAlright, here's a summary of your portfolio:\n")
    total = 0
    for stock, qty in portfolio.items():
        value = stock_prices[stock] * qty
        print(f"  {stock}: {qty} shares x ${stock_prices[stock]} = ${value}")
        total += value

    print(f"\nYour total investment comes to: ${total}")

    save = input("\nWould you like to save this to a file? (yes / no): ").lower().strip()
    if save in ("yes", "y"):
        with open("portfolio.csv", "w") as f:
            f.write("Stock,Quantity,Price per Share,Total Value\n")
            for stock, qty in portfolio.items():
                value = stock_prices[stock] * qty
                f.write(f"{stock},{qty},{stock_prices[stock]},{value}\n")
            f.write(f",,Total,{total}\n")
        print("Done! Your portfolio has been saved to portfolio.csv 📁")
    else:
        print("No worries! Your data was not saved.")

print("\nThanks for using the Stock Tracker. See you next time! 😊")