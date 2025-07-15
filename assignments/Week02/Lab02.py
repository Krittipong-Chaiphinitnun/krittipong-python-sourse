"""
Question 2: Currency Converter (20 points)

Write a program that converts between Thai Baht (THB) and US Dollars (USD).
Requirements:

Ask user to choose conversion direction (THB to USD or USD to THB)
Ask for the amount to convert
Use exchange rate: 1 USD = 35.5 THB
Display result with 2 decimal places
Show the calculation formula used
"""

direction = input("Choose conversion direction (1: THB to USD, 2: USD to THB): ")
amount = float(input("Enter the amount to convert: "))
if direction == "1":
    # THB to USD
    result = amount / 35.5
    print(f"{amount} THB = {result:.2f} USD")
    print(f"Calculation formula: {amount} / 35.5")
elif direction == "2":
    # USD to THB
    result = amount * 35.5
    print(f"{amount} USD = {result:.2f} THB")
    print(f"Calculation formula: {amount} * 35.5")
else:
    print("Invalid direction selected.")
    