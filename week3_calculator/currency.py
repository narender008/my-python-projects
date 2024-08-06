import requests

API_KEY = "masked"
BASE_URL = f"https://api.freecurrencyapi.com/v1/latest?apikey={API_KEY}"


CURRENCRIES = ["USD", "EUR", "GBP", "INR"]


def convert_currency(base):
    currencies = ",".join(CURRENCRIES)
    url = f"{BASE_URL}&base_currency={base}&currencies={currencies}"
    try:
        response = requests.get(url)
        data = response.json()
        return data["data"]
    except Exception as e:
        print(e)
        return None


data = convert_currency("USD")
print(data)
