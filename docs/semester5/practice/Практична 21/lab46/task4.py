import csv


class Expense:
    def __init__(self, category, amount):
        self.category = category
        self.amount = float(amount)

    def balance_change(self):
        return -self.amount


class Income:
    def __init__(self, category, amount):
        self.category = category
        self.amount = float(amount)

    def balance_change(self):
        return self.amount


class Transfer:
    def __init__(self, category, amount):
        self.category = category
        self.amount = float(amount)

    def balance_change(self):
        return 0


print("Illia Basalukk, IT-31")
print("Група: IT-31\n")

expenses = []

with open("data/expenses.csv", "r", encoding="utf-8-sig") as file:
    header = file.readline().strip().lstrip("#").strip().split(";")
    reader = csv.DictReader(file, fieldnames=header, delimiter=";")

    for row in reader:
        expenses.append(
            Expense(row["category"], float(row["amount"]))
        )

transactions = [
    Income("scholarship", 2000),
    Income("part-time job", 600),
    *expenses,
    Transfer("own cards", 1500)
]

income_total = 0
expenses_total = 0
transfers_total = 0
balance = 0

for transaction in transactions:
    change = transaction.balance_change()
    balance += change

    if isinstance(transaction, Income):
        income_total += change
    elif isinstance(transaction, Expense):
        expenses_total += change
    elif isinstance(transaction, Transfer):
        transfers_total += change

print(f"Дохід:      {income_total:>10.2f} UAH")
print(f"Витрати:    {expenses_total:>10.2f} UAH")
print(f"Перекази:   {transfers_total:>10.2f} UAH")
print("-" * 30)
print(f"Баланс:     {balance:>10.2f} UAH")
