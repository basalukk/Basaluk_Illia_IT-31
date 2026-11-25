import json
from pathlib import Path
from datetime import date

print("Illia Basalukk, IT-31")

source = Path("data/expenses.json")
destination = Path("data/expenses_updated.json")

with source.open("r", encoding="utf-8") as file:
    records = json.load(file)

new_record = {
    "date": date.today().isoformat(),
    "category": "food",
    "amount": 50.0,
    "comment": "Практична робота 16"
}

records.append(new_record)
added = 1

old_count = len(records)
records = [record for record in records if record["amount"] >= 10]
deleted = old_count - len(records)

with destination.open("w", encoding="utf-8") as file:
    json.dump(records, file, indent=2, ensure_ascii=False)

print(f"added: {added}")
print(f"deleted: {deleted}")
print(f"records: {len(records)}")
print(f"saved: {destination}")
