import csv
from pathlib import Path


class Expense:
    def __init__(self, date, category, amount, comment):
        self.date = date
        self.category = category
        self.amount = float(amount)
        self.comment = comment

    def is_big(self, limit):
        return self.amount > limit

    def describe(self):
        date_parts = self.date.split("-")
        formatted_date = ".".join(reversed(date_parts))
        return f"{formatted_date} {self.category} {self.amount:.2f} ({self.comment})"


expenses = []
csv_path = Path("data") / "expenses.csv"

with csv_path.open("r", encoding="utf-8-sig", newline="") as file:
    header = file.readline().strip().lstrip("#").strip().split(";")
    reader = csv.DictReader(file, fieldnames=header, delimiter=";")

    for row in reader:
        if row.get("amount"):
            expense = Expense(
                row["date"],
                row["category"],
                row["amount"],
                row["note"]
            )
            expenses.append(expense)

limit = 100

print("Illia Basalukk, IT-31")
print("Кількість об'єктів Expense:", len(expenses))
print(f"\nВеликі витрати (понад {limit} грн):")

for expense in expenses:
    if expense.is_big(limit):
        print(expense.describe())
