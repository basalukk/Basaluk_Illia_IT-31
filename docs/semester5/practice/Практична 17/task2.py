import csv
import requests
import sys
from pathlib import Path

API_URL = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange"
CSV_PATH = Path("data") / "expenses.csv"


def run_error_test(mode):
    try:
        if mode == "--test-connection":
            requests.get("https://127.0.0.1:1", timeout=3)

        elif mode == "--test-404":
            response = requests.get(
                "https://bank.gov.ua/ua/this-page-does-not-exist",
                timeout=10
            )
            response.raise_for_status()

        elif mode == "--test-timeout":
            requests.get(API_URL, timeout=0.001)

        else:
            print("Невідомий режим тестування.", file=sys.stderr)
            sys.exit(1)

        print("Помилка не виникла.")

    except requests.RequestException as error:
        print(f"Тест {mode}: {type(error).__name__}: {error}", file=sys.stderr)
        sys.exit(1)


def get_rate(currency_code):
    response = requests.get(
        API_URL,
        params={"valcode": currency_code, "json": ""},
        timeout=10
    )
    response.raise_for_status()
    data = response.json()

    if not data:
        raise ValueError(f"НБУ не повернув курс {currency_code}")

    return float(data[0]["rate"]), data[0]["exchangedate"]


if __name__ == "__main__":
    if len(sys.argv) > 1:
        run_error_test(sys.argv[1])

    try:
        with CSV_PATH.open("r", encoding="utf-8-sig", newline="") as file:
            header = file.readline().strip().lstrip("#").strip().split(";")
            reader = csv.DictReader(file, fieldnames=header, delimiter=";")
            total_uah = sum(
                float(row["amount"])
                for row in reader
                if row.get("amount")
            )

        usd_rate, usd_date = get_rate("USD")
        eur_rate, eur_date = get_rate("EUR")

    except (OSError, ValueError, KeyError, requests.RequestException) as error:
        print(f"Помилка: {error}", file=sys.stderr)
        sys.exit(1)

    print("Illia Basalukk, IT-31")
    print(f"Загальні витрати: {total_uah:.2f} UAH")
    print(f"Курс USD ({usd_date}): {usd_rate:.4f} UAH")
    print(f"Витрати в USD: {total_uah / usd_rate:.2f} USD")
    print(f"Курс EUR ({eur_date}): {eur_rate:.4f} UAH")
    print(f"Витрати в EUR: {total_uah / eur_rate:.2f} EUR")
