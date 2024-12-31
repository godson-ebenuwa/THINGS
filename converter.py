import requests

API_KEY = "afa3527ba51a4f948bd848524808022d"
BASE_URL = "https://openexchangerates.org/api/latest.json"


def fetch_exchange_rates():
    try:
        response = requests.get(BASE_URL, params={"app_id": API_KEY})
        response.raise_for_status()
        return response.json().get("rates", {})
    except requests.exceptions.RequestException as e:
        print(f"Error fetching rates: {e}")
        return {}


def convert_from_currency(amount, from_currency, to_currency, rates):
    try:
        # Convert from the specified 'from_currency' to the 'to_currency'
        converted_amount = amount / rates[from_currency] * rates[to_currency]
        return converted_amount
    except KeyError:
        print(f"Conversion error: {from_currency} or {to_currency} not found in rates.")
        return None



rates = fetch_exchange_rates()

if not rates:
    print("Failed to fetch exchange rates. Exiting.")

print("Available currencies: NGN, USD, GHS, EUR, GBP")

# Ask the user for the currency they are converting from
from_currency = input("Enter the currency you are converting from (e.g., NGN): ").upper()

# If the user enters an unsupported currency, default to NGN
if from_currency not in rates and from_currency != "NGN":
    print(f"Currency {from_currency} is not supported. Defaulting to NGN.")
    from_currency = "NGN"

# Ask the user for the currency they are converting to
to_currency = input("Enter the currency you want to convert to (e.g., USD, GHS, EUR, GBP): ").upper()

if to_currency not in rates:
    print(f"Currency {to_currency} is not supported. Exiting.")


print(f"You are converting from {from_currency} to {to_currency}.")

try:
    amount = float(input(f"Enter the amount in {from_currency} to convert: "))
    result = convert_from_currency(amount, from_currency, to_currency, rates)

    if result is not None:
        print(f"{amount:.2f} {from_currency} = {result:.2f} {to_currency}")
except ValueError:
    print("Invalid input. Please enter a numeric value.")



