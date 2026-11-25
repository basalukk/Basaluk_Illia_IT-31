import requests
import sys

URL = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange"

try:
    response = requests.get(URL, params={"json": ""}, timeout=10)
    response.raise_for_status()
    rates = response.json()
except requests.RequestException as error:
    print(f"Помилка запиту до НБУ: {error}", file=sys.stderr)
    sys.exit(1)

print("Illia Basalukk, IT-31")
print("HTTP status:", response.status_code)
print("Content-Type:", response.headers.get("Content-Type"))
print("Кількість валют:", len(rates))

for code in ("USD", "EUR"):
    currency = next((item for item in rates if item.get("cc") == code), None)
    if currency:
        print(f"{code}: {currency['rate']} UAH")
        print(f"Дата курсу: {currency['exchangedate']}")
