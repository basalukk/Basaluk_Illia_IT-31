import csv
from datetime import datetime


class Money:
    def __init__(self, amount, currency="UAH"):
        self.cents = round(float(amount) * 100)
        self.currency = currency

    def __add__(self, other):
        if not isinstance(other, Money):
            return NotImplemented
        if self.currency != other.currency:
            raise ValueError("Різні валюти")
        return Money((self.cents + other.cents) / 100, self.currency)

    def __lt__(self, other):
        if not isinstance(other, Money):
            return NotImplemented
        if self.currency != other.currency:
            raise ValueError("Різні валюти")
        return self.cents < other.cents

    def __gt__(self, other):
        if not isinstance(other, Money):
            return NotImplemented
        if self.currency != other.currency:
            raise ValueError("Різні валюти")
        return self.cents > other.cents

    def __str__(self):
        return f"{self.cents / 100:.2f} {self.currency}"


class Expense:
    def __init__(self, date, category, amount, note):
        self.date = datetime.strptime(date, "%Y-%m-%d").date()
        self.category = category
        self.amount = Money(amount)
        self.note = note

    def __str__(self):
        return f"{self.date} | {self.category:10} | {self.amount} | {self.note}"


class ExpenseBook:
    def __init__(self, expenses=None):
        self.expenses = expenses or []

    def __len__(self):
        return len(self.expenses)

    def __contains__(self, category):
        return any(expense.category == category for expense in self.expenses)

    def __iter__(self):
        return iter(self.expenses)

    def __getitem__(self, index):
        return self.expenses[index]

    def __add__(self, other):
        if not isinstance(other, ExpenseBook):
            return NotImplemented
        return ExpenseBook(self.expenses + other.expenses)

    def total(self):
        return sum((expense.amount for expense in self.expenses), Money(0))

    def __gt__(self, budget):
        if not isinstance(budget, Money):
            return NotImplemented
        return self.total() > budget

    def __str__(self):
        return (
            f"Кількість витрат: {len(self)}\n"
            f"Загальна сума: {self.total()}"
        )


print("Illia Basalukk, IT-31")
print("Завдання 3. Клас ExpenseBook\n")

expenses = []

with open("data/expenses.csv", "r", encoding="utf-8-sig") as file:
    header = file.readline().strip().lstrip("#").strip().split(";")
    reader = csv.DictReader(file, fieldnames=header, delimiter=";")

    for row in reader:
        expenses.append(
            Expense(
                row["date"].strip(),
                row["category"].strip(),
                row["amount"].strip(),
                row["note"].strip()
            )
        )

first_half = ExpenseBook([e for e in expenses if e.date.day <= 15])
second_half = ExpenseBook([e for e in expenses if e.date.day > 15])

print("Перша половина місяця:")
print(first_half)

print("\nДруга половина місяця:")
print(second_half)

print("\nПеревірка спеціальних методів:")
print("Кількість витрат у другій половині:", len(second_half))
print("Чи є категорія food:", "food" in second_half)
print("Перша витрата:", second_half[0])
print("\nПеребір витрат:")
for expense in second_half:
    print(expense)

merged_book = first_half + second_half
print("\nОб'єднана книга витрат:")
print(merged_book)
print("Кількість після об'єднання:", len(merged_book))

print("\nЗавдання 4. Перевірка бюджету\n")

budget = Money(6000)
total = merged_book.total()

print("Бюджет:", budget)
print("Фактичні витрати:", total)

if merged_book > budget:
    print("Бюджет перевищено!")
else:
    print("Витрати в межах бюджету.")

print("Залишок бюджету:", Money(6000) + Money(-total.cents / 100))
