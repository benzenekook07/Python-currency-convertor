name = input("Enter your name: ")  # Start of the program ! Enjoy

age = input("Enter your age: ")

print("\nHello", name + "!")

print("Thank you for using this platform!")
rates = {
    "USD": 1,
    "INR": 83.5,
    "EUR": 0.92,
    "GBP": 0.78
}

def convert(amount, from_curr, to_curr):
    if from_curr not in rates or to_curr not in rates:
        return None
    usd_amount = amount / rates[from_curr]     # convert to USD
    return usd_amount * rates[to_curr]         # convert to target currency

amount = float(input("Enter amount: "))
from_curr = input("From currency (USD, INR, EUR, GBP): ").upper()
to_curr = input("To currency (USD, INR, EUR, GBP): ").upper()

result = convert(amount, from_curr, to_curr)

if result:
    print(f"{amount} {from_curr} = {result:.2f} {to_curr}")
else:
    print("Invalid currency code!")
