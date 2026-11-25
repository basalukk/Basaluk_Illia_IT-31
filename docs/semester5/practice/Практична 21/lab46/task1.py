import csv
import json
import math
from datetime import datetime


class Expense:
    currency = "UAH"
    created_count = 0

    def __init__(self, date, category, amount, comment=""):
        self.date = date
        self.category = category
        self.amount = float(amount)
        self.comment = comment
        Expense.created_count += 1

    @staticmethod
    def is_valid_date(text):
        try:
            parsed = datetime.strptime(text, "%Y-%m-%d")
            return parsed.strftime("%Y-%m-%d") == text
        except ValueError:
            return False

    @staticmethod
    def is_valid_amount(value):
        try:
            amount = float(value)
            return math.isfinite(amount) and amount >= 0
        except (ValueError, TypeError):
            return False

    @classmethod
    def from_csv_line(cls, line):
        parts = line.strip().split(";")
        if len(parts) != 4:
            raise ValueError("Неправильна кількість полів")

        date, category, amount, comment = parts

        if not cls.is_valid_date(date):
            raise ValueError("Некоректна дата")
        if not cls.is_valid_amount(amount):
            raise ValueError("Некоректна сума")

        return cls(date, category, float(amount), comment)

    @classmethod
    def from_dict(cls, data):
        if not cls.is_valid_date(data["date"]):
            raise ValueError("Некоректна дата в JSON")
        if not cls.is_valid_amount(data["amount"]):
            raise ValueError("Некоректна сума в JSON")

        return cls(
            data["date"],
            data["category"],
            float(data["amount"]),
            data.get("comment", "")
        )

    @classmethod
    def from_input(cls):
        date = input("Дата (YYYY-MM-DD): ")
        category = input("Категорія: ")
        amount = input("Сума: ")
        comment = input("Коментар: ")

        if not cls.is_valid_date(date):
            raise ValueError("Некоректна дата")
        if not cls.is_valid_amount(amount):
            raise ValueError("Некоректна сума")

        return cls(date, category, float(amount), comment)

    @classmethod
    def set_currency(cls, code):
        cls.currency = code

    def __str__(self):
        return (
            f"{self.date} | {self.category} | "
            f"{self.amount:.2f} {self.currency} | {self.comment}"
        )


print("Illia Basalukk, IT-31")
print("Дата народження: 11.07.2009\n")

csv_expenses = []

with open("data/expenses.csv", "r", encoding="utf-8-sig") as file:
    header = file.readline().strip().lstrip("#").strip().split(";")
    reader = csv.DictReader(file, fieldnames=header, delimiter=";")

    for row in reader:
        try:
            line = (
                f'{row["date"]};{row["category"]};'
                f'{row["amount"]};{row["note"]}'
            )
            csv_expenses.append(Expense.from_csv_line(line))
        except (ValueError, KeyError) as error:
            print("Пропущено рядок CSV:", error)

with open("data/expenses.json", "r", encoding="utf-8-sig") as file:
    json_data = json.load(file)

json_expenses = []

for item in json_data:
    try:
        json_expenses.append(Expense.from_dict(item))
    except (ValueError, KeyError) as error:
        print("Пропущено запис JSON:", error)

example = Expense.from_csv_line(
    "2026-09-21;food;85.50;lunch"
)

print("Приклад створення з CSV:")
print(example)

print("\nПерші 3 витрати з CSV:")
for expense in csv_expenses[:3]:
    print(expense)

print("\nПерші 3 витрати з JSON:")
for expense in json_expenses[:3]:
    print(expense)

print("\nПорівняння:")
print("Кількість записів CSV:", len(csv_expenses))
print("Кількість записів JSON:", len(json_expenses))
print("Дані збігаються:", len(csv_expenses) == len(json_expenses))

print("\nПеревірка статичних методів:")
print("Дата 2026-02-30:", Expense.is_valid_date("2026-02-30"))
print("Дата 2026-11-25:", Expense.is_valid_date("2026-11-25"))
print("Сума 100.50:", Expense.is_valid_amount("100.50"))
print("Сума -50:", Expense.is_valid_amount("-50"))

print("\nПеревірка некоректного CSV:")
try:
    Expense.from_csv_line("2026-02-30;food;50;test")
except ValueError as error:
    print("Рядок пропущено:", error)

print("\nЛічильник створених об'єктів:", Expense.created_count)

print("\nЗміна валюти:")
Expense.set_currency("USD")
print(example)
print(csv_expenses[0])
print(json_expenses[0])
