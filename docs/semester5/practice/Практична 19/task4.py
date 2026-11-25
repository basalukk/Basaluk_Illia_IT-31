import csv
from pathlib import Path


class Wallet:
    def __init__(self, owner, balance):
        if not owner.strip():
            raise ValueError("Ім'я власника не може бути порожнім")
        if balance < 0:
            raise ValueError("Баланс не може бути від'ємним")

        self.owner = owner
        self.__balance = round(balance, 2)

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Сума має бути більшою за нуль")
        if amount > self.__balance:
            raise ValueError("Недостатньо коштів")
        self.__balance = round(self.__balance - amount, 2)

    @property
    def balance(self):
        return self.__balance


print("Illia Basalukk, IT-31")

wallet = Wallet("Illia Basalukk", 6000)
expenses = []

with Path("data/expenses.csv").open(
    "r", encoding="utf-8-sig", newline=""
) as file:
    header = file.readline().strip().lstrip("#").strip().split(";")
    reader = csv.DictReader(file, fieldnames=header, delimiter=";")

    for row in reader:
        if row.get("amount"):
            expenses.append(row)

print(f"Початковий бюджет: {wallet.balance:.2f} UAH")
print(f"Кількість витрат: {len(expenses)}")

for expense in expenses:
    amount = float(expense["amount"])

    try:
        wallet.withdraw(amount)
        print(
            f"Списано {amount:.2f} UAH | "
            f"{expense['category']} | "
            f"Залишок: {wallet.balance:.2f} UAH"
        )
    except ValueError as error:
        print(f"Не вдалося списати {expense['amount']} UAH: {error}")
        print(f"Причина: {expense['note']}")
        break

print(f"\nКінцевий залишок: {wallet.balance:.2f} UAH")
