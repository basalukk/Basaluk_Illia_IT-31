import csv
from pathlib import Path


class Expense:
    def __init__(self, date, category, amount, comment):
        self.date = date
        self.category = category
        self.amount = float(amount)
        self.comment = comment

    def describe(self):
        date_parts = self.date.split("-")
        formatted_date = ".".join(reversed(date_parts))
        return f"{formatted_date} {self.category} {self.amount:.2f} ({self.comment})"


class ExpenseBook:
    def __init__(self):
        self.expenses = []

    def add(self, expense):
        self.expenses.append(expense)

    def total(self):
        return sum(expense.amount for expense in self.expenses)

    def by_category(self, category):
        return [
            expense for expense in self.expenses
            if expense.category == category
        ]

    def top(self, n):
        return sorted(
            self.expenses,
            key=lambda expense: expense.amount,
            reverse=True
        )[:n]


book = ExpenseBook()
csv_path = Path("data") / "expenses.csv"

with csv_path.open("r", encoding="utf-8-sig", newline="") as file:
    header = file.readline().strip().lstrip("#").strip().split(";")
    reader = csv.DictReader(file, fieldnames=header, delimiter=";")

    for row in reader:
        if row.get("amount"):
            book.add(Expense(
                row["date"],
                row["category"],
                row["amount"],
                row["note"]
            ))

print("Illia Basalukk, IT-31")
print("Кількість витрат:", len(book.expenses))
print(f"Загальна сума: {book.total():.2f} UAH")

print("\nВитрати за категоріями:")
categories = sorted(set(expense.category for expense in book.expenses))

for category in categories:
    category_expenses = book.by_category(category)
    category_total = sum(expense.amount for expense in category_expenses)
    print(f"{category}: {category_total:.2f} UAH ({len(category_expenses)} записів)")

print("\nТоп-5 найбільших витрат:")
for expense in book.top(5):
    print(expense.describe())
