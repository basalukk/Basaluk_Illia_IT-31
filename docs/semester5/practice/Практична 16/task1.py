import csv
import json
from pathlib import Path

print("Illia Basalukk, IT-31")

csv_path = Path("data/expenses.csv")
json_path = Path("data/expenses.json")

records = []

with csv_path.open("r", encoding="utf-8-sig", newline="") as file:
    header = file.readline().strip().lstrip("#").strip().split(";")
    reader = csv.DictReader(file, fieldnames=header, delimiter=";")

    for row in reader:
        records.append({
            "date": row["date"],
            "category": row["category"],
            "amount": float(row["amount"]),
            "comment": row["note"]
        })

with json_path.open("w", encoding="utf-8") as file:
    json.dump(records, file, indent=2, ensure_ascii=False)

print(f"records: {len(records)}")
print(f"saved: {json_path} ({json_path.stat().st_size} bytes)")
