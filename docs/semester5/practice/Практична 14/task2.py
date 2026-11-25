import csv
from pathlib import Path
from collections import defaultdict
from math import fsum
from tabulate import tabulate

FILE = Path(__file__).parent / "data" / "expenses.csv"

expenses = defaultdict(list)

with FILE.open("r", encoding="utf-8-sig", newline="") as file:
    reader = csv.reader(file, delimiter=";")

    for row in reader:
        if not row or not row[0].strip() or row[0].strip().startswith("#"):
            continue

        if len(row) < 3:
            continue

        category = row[1].strip()
        amount = float(row[2].strip().replace(",", "."))
        expenses[category].append(amount)

rows = []

for category in sorted(expenses):
    amounts = expenses[category]
    rows.append([category, len(amounts), fsum(amounts)])

total_count = sum(row[1] for row in rows)
total_amount = fsum(row[2] for row in rows)

rows.append(["TOTAL", total_count, total_amount])

print("Illia Basalukk, IT-31")
print(tabulate(
    rows,
    headers=["category", "count", "total"],
    tablefmt="github",
    floatfmt=".2f"
))
