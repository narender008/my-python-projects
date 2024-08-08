import requests

API_KEY = "MASKED_API_KEY"
BASE_URL = f"https://api.freecurrencyapi.com/v1/latest?apikey={API_KEY}"


CURRENCRIES = ["USD", "EUR", "GBP", "INR", "JPY", "AUD", "CAD", "CHF"]


def convert_currency(base):
    currencies = ",".join(CURRENCRIES)
    url = f"{BASE_URL}&base_currency={base}&currencies={currencies}"
    try:
        response = requests.get(url)
        data = response.json()
        return data["data"]
    except:
        print("invalid currency")
        return None


while True:
    base = input("Enter base currency: (press  q to quit) ").upper()

    if base == "Q":
        break

    data = convert_currency(base)
    if not data:
        continue

    del data[base]

    for abbreviation, value in data.items():
        print(f"{abbreviation}: {value}")
