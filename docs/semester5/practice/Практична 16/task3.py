import json
import sys
from pathlib import Path

print("Illia Basalukk, IT-31")

settings_path = Path("settings.json")
expenses_path = Path("data/expenses.json")

default_settings = {
    "owner": "Illia Basalukk",
    "group": "IT-31",
    "currency": "UAH",
    "monthly_limit": 6000,
    "categories": ["food", "transport", "fun"]
}

if not settings_path.exists():
    with settings_path.open("w", encoding="utf-8") as file:
        json.dump(default_settings, file, indent=2, ensure_ascii=False)
    print("settings.json not found, default created")
    sys.exit(0)

try:
    with settings_path.open("r", encoding="utf-8") as file:
        settings = json.load(file)
except json.JSONDecodeError as error:
    print(f"JSON error at line {error.lineno}", file=sys.stderr)
    sys.exit(1)

with expenses_path.open("r", encoding="utf-8") as file:
    expenses = json.load(file)

spent = sum(record["amount"] for record in expenses)
limit = settings["monthly_limit"]
left = limit - spent

print(f"limit: {limit:.2f} {settings['currency']}, spent: {spent:.2f} {settings['currency']}, left: {left:.2f} {settings['currency']}")
