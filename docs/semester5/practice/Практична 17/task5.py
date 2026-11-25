import json
import time
import requests
import sys
from pathlib import Path

API_URL = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange"
CACHE_PATH = Path("cache") / "rates.json"
CACHE_DURATION = 3600


def fetch_rates():
    response = requests.get(API_URL, params={"json": ""}, timeout=10)
    response.raise_for_status()
    return response.json()


try:
    now = time.time()
    rates = None
    age = None
    source = None

    if CACHE_PATH.exists():
        try:
            cache_data = json.loads(CACHE_PATH.read_text(encoding="utf-8"))
            age = now - cache_data["timestamp"]

            if 0 <= age < CACHE_DURATION:
                rates = cache_data["rates"]
                source = "cache"
        except (OSError, ValueError, KeyError, TypeError):
            rates = None

    if rates is None:
        rates = fetch_rates()
        CACHE_PATH.parent.mkdir(parents=True, exist_ok=True)

        cache_data = {
            "timestamp": now,
            "rates": rates
        }
        CACHE_PATH.write_text(
            json.dumps(cache_data, ensure_ascii=False, indent=2),
            encoding="utf-8"
        )
        age = 0
        source = "api"

except (requests.RequestException, OSError, ValueError, KeyError) as error:
    print(f"Помилка отримання курсів: {error}", file=sys.stderr)
    sys.exit(1)

print("Illia Basalukk, IT-31")
print(f"Джерело даних: {source}")
print(f"Вік кешу: {int(age)} секунд")
print(f"Кількість валют: {len(rates)}")

for code in ("USD", "EUR"):
    currency = next((item for item in rates if item.get("cc") == code), None)
    if currency:
        print(f"{code}: {currency['rate']} UAH")
        print(f"Дата курсу: {currency['exchangedate']}")
