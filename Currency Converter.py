import requests

def currency_converter():
    print("Currency Converter")
    amount = float(input("Enter amount: "))
    from_currency = input("From currency (e.g., USD): ").upper()
    to_currency = input("To currency (e.g., EUR): ").upper()

    url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"
    response = requests.get(url).json()

    if to_currency in response['rates']:
        conversion_rate = response['rates'][to_currency]
        converted_amount = amount * conversion_rate
        print(f"{amount} {from_currency} is {converted_amount:.2f} {to_currency}")
    else:
        print("Invalid currency code.")

currency_converter()
