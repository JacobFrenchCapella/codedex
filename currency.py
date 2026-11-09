import currency

def convert_currency(amount, from_currency, to_currency):
    # Placeholder function - replace with actual currency conversion logic
    return amount * currency.RATES.get((from_currency, to_currency), 1)

def main():
    amount = float(input("Enter the amount: "))
    from_currency = input("Enter the currency to convert from (e.g., USD): ")
    to_currency = input("Enter the currency to convert to (e.g., EUR): ")
    
    converted_amount = convert_currency(amount, from_currency, to_currency)
    print(f"{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}")