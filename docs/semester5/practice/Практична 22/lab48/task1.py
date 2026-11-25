import csv


class Money:
    def __init__(self, amount, currency="UAH"):
        self.cents = round(amount * 100)
        self.currency = currency

    def __add__(self, other):
        if not isinstance(other, Money):
            return NotImplemented
        if self.currency != other.currency:
            raise ValueError("Різні валюти")
        return Money((self.cents + other.cents) / 100, self.currency)

    def __sub__(self, other):
        if not isinstance(other, Money):
            return NotImplemented
        if self.currency != other.currency:
            raise ValueError("Різні валюти")
        return Money((self.cents - other.cents) / 100, self.currency)

    def __mul__(self, number):
        if not isinstance(number, (int, float)):
            return NotImplemented
        return Money((self.cents * number) / 100, self.currency)

    def __eq__(self, other):
        if not isinstance(other, Money):
            return NotImplemented
        return self.cents == other.cents and self.currency == other.currency

    def __lt__(self, other):
        if not isinstance(other, Money):
            return NotImplemented
        if self.currency != other.currency:
            raise ValueError("Неможливо порівняти різні валюти")
        return self.cents < other.cents

    def __str__(self):
        return f"{self.cents / 100:.2f} {self.currency}"

    def __repr__(self):
        return f"Money({self.cents / 100:.2f}, '{self.currency}')"


print("Illia Basalukk, IT-31")
print("Завдання 1. Клас Money\n")

a = Money(0.1)
b = Money(0.2)
c = Money(0.3)

print("0.1 + 0.2 =", a + b)
print("Money(0.1) + Money(0.2) == Money(0.3):", a + b == c)
print("Перевірка float:", 0.1 + 0.2 == 0.3)

print("\nВіднімання:", Money(100) - Money(35.50))
print("Множення:", Money(25.50) * 3)
print("Порівняння:", Money(100) > Money(50))

print("\nПредставлення об'єкта:")
print(repr(Money(125.50)))

try:
    print(Money(100) + Money(50, "USD"))
except ValueError as error:
    print("Помилка валюти:", error)

print("\nЗавдання 2. Сортування та сума\n")

items = []

with open("data/expenses.csv", "r", encoding="utf-8-sig") as file:
    header = file.readline().strip().lstrip("#").strip().split(";")
    reader = csv.DictReader(file, fieldnames=header, delimiter=";")

    for row in reader:
        items.append(Money(float(row["amount"])))

print("Витрати до сортування:")
print(items)

print("\nВитрати після сортування:")
print(sorted(items))

total = sum(items, Money(0))
print("\nЗагальна сума витрат:", total)
print("Кількість витрат:", len(items))

print("\nПеревірка Money(10) + 5:")
try:
    print(Money(10) + 5)
except TypeError as error:
    print("Очікувана помилка:", error)

print("\nПорівняння з float:")
print("0.1 + 0.2 == 0.3:", 0.1 + 0.2 == 0.3)
print("Money(0.1) + Money(0.2) == Money(0.3):", Money(0.1) + Money(0.2) == Money(0.3))
