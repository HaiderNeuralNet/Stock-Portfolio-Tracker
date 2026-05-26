# 📈 Stock Portfolio Tracker

> A simple, beginner-friendly Python program that calculates your total stock investment using a hardcoded price dictionary — with optional CSV export.

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)
![Level](https://img.shields.io/badge/Level-Beginner-orange?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge)

---

## 📌 Table of Contents

- [About the Project](#-about-the-project)
- [Features](#-features)
- [Demo](#-demo)
- [Getting Started](#-getting-started)
- [How It Works](#-how-it-works)
- [Code Theory](#-code-theory)
- [Project Structure](#-project-structure)
- [Customization](#-customization)
- [Key Concepts Used](#-key-concepts-used)
- [Sample Output](#-sample-output)
- [Contributing](#-contributing)
- [License](#-license)

---

## 🧠 About the Project

This project was built as **Task 2** of a Python beginner assignment. The goal is to build a simple stock tracker that:

- Takes stock names and quantities as user input
- Uses a **hardcoded dictionary** for stock prices
- Calculates the **total investment value**
- Optionally **saves the result** to a `.csv` file

No external APIs or libraries are needed — just pure Python!

---

## ✨ Features

| Feature | Description |
|---|---|
| 📋 Stock Listing | Displays all available stocks with prices |
| ✏️ User Input | Enter stock name and quantity interactively |
| ✅ Input Validation | Handles invalid stock names and non-numeric input |
| 💰 Total Calculation | Computes value of each holding and grand total |
| 💾 CSV Export | Optionally saves portfolio to `portfolio.csv` |
| 💬 Human-Friendly | Conversational prompts and friendly error messages |

---

## 🎬 Demo

```
Hey! Welcome to your Stock Portfolio Tracker 👋
Let's see how much your stocks are worth.

Here are the stocks we have today:
   "NFLX": 620,
    "META": 500,
    "NVDA": 800,
    "UBER": 70,
    "DIS": 110

Which stock do you want to add? (or type 'done' when finished): AAPL
How many shares of AAPL do you own? 10
Got it! Added 10 shares of AAPL.

Which stock do you want to add? (or type 'done' when finished): TSLA
How many shares of TSLA do you own? 5
Got it! Added 5 shares of TSLA.

Which stock do you want to add? (or type 'done' when finished): done

Alright, here's a summary of your portfolio:

  NFLX: 10 shares x $620 = $6200
  META: 5 shares x $500 = $2500

Your total investment comes to: $8700

Would you like to save this to a file? (yes / no): yes
Done! Your portfolio has been saved to portfolio.csv 📁

Thanks for using the Stock Tracker. See you next time! 😊
```

---

## 🚀 Getting Started

### Prerequisites

Make sure you have Python 3 installed:

```bash
python --version
```

### Installation

1. **Clone the repository**

```bash
git clone https://github.com/HaiderNeuralNet/Stock-Portfolio-Tracker
```

2. **Navigate into the folder**

```bash
cd stock-portfolio-tracker
```

3. **Run the program**

```bash
python task1.py
```

That's it — no installs, no setup, no dependencies! ✅

---

## ⚙️ How It Works

```
┌─────────────────────────────────────────────────────┐
│                   PROGRAM FLOW                      │
├─────────────────────────────────────────────────────┤
│  1. Display available stocks from dictionary        │
│  2. Ask user for stock name → validate it           │
│  3. Ask user for quantity → validate it             │
│  4. Store in portfolio dictionary                   │
│  5. Repeat until user types 'done'                  │
│  6. Calculate value for each stock                  │
│  7. Display summary + grand total                   │
│  8. Optionally save to portfolio.csv                │
└─────────────────────────────────────────────────────┘
```

---

## 📚 Code Theory

### 1. 📖 Dictionary — Stock Price Database

```python
stock_prices = {
    "NFLX": 620,
    "META": 500,
    "NVDA": 800,
    "UBER": 70,
    "DIS": 110
}
```

A **dictionary** is a key-value data structure. The stock ticker is the **key**, and the price is the **value**. Dictionaries provide instant O(1) lookup — no matter how many stocks you add, finding a price is always fast.

---

### 2. 🔁 While Loop — Infinite Input Loop

```python
while True:
    name = input("Which stock? ").upper().strip()
    if name == "DONE":
        break
```

`while True` creates an infinite loop that only exits when `break` is called. This is the classic **input loop pattern** — keep asking until the user signals they're finished. `.upper()` normalizes input and `.strip()` removes accidental spaces.

---

### 3. 🛡️ Input Validation — Defensive Programming

```python
if name not in stock_prices:
    print("Stock not found. Try again.")
    continue

try:
    qty = int(input("How many shares? "))
except ValueError:
    print("That doesn't look like a number.")
    continue
```

**Never trust user input.** Two types of validation are used:
- `not in` prevents a `KeyError` crash if the stock doesn't exist
- `try/except ValueError` catches non-numeric input before `int()` crashes

`continue` skips to the next loop iteration, giving the user another chance.

---

### 4. ➕ Accumulator Pattern — Running Total

```python
total = 0
for stock, qty in portfolio.items():
    value = stock_prices[stock] * qty
    total += value
```

The **accumulator pattern** starts at zero and adds to a running total each iteration. `stock_prices[stock]` does a dictionary lookup, then multiplies by quantity. `total += value` is shorthand for `total = total + value`.

---

### 5. 💾 File Handling — Data Persistence

```python
with open("portfolio.csv", "w") as f:
    f.write("Stock,Quantity,Price,Value\n")
```

Programs lose data when they close (stored in RAM). File handling gives **persistence** — data survives after the program ends. The `with` statement is a **context manager** that automatically closes the file safely, even if an error occurs.

---

## 📁 Project Structure

```
stock-portfolio-tracker/
│
├── task1.py      # Main program file
├── portfolio.csv         # Generated after saving (auto-created)
└── README.md             # You are here!
```

---

## 🎨 Customization

### Add your own stocks

Open `task1.py` and edit the dictionary at the top:

```python
stock_prices = {
    "NFLX": 620,
    "META": 500,
    "NVDA": 800,
    "UBER": 70,
    "DIS": 110
}
```

Just follow the format — `"TICKER": price` — and the rest of the program adapts automatically.

### Change the output file name

```python
with open("my_portfolio.csv", "w") as f:   # change filename here
```

---

## 🧩 Key Concepts Used

| Concept | Where Used |
|---|---|
| `dictionary` | Stock prices database, portfolio storage |
| `while loop` | Continuous input collection |
| `if-else` | Stock validation, save prompt |
| `try/except` | Quantity input validation |
| `for loop` | Displaying stocks, calculating totals |
| `f-strings` | Formatted output messages |
| `file handling` | Saving portfolio to CSV |
| `accumulator pattern` | Calculating grand total |
| `.upper()` / `.strip()` | Input normalization |

---

## 📄 Sample Output (CSV)

After saving, `portfolio.csv` looks like this:

```
Stock,Quantity,Price per Share,Total Value
AAPL,10,180,1800
TSLA,5,250,1250
,,Total,3050
```

You can open this directly in **Microsoft Excel** or **Google Sheets**.

---

## 📜 License

This project is licensed under the **MIT License** — feel free to use, modify, and distribute it.

---


> *"First, solve the problem. Then, write the code."* — John Johnson

---
