class Expense:
    def __init__(self, date, category, amount):
        self.date = date
        self.category = category
        self.amount = float(amount)

    def monthly_cost(self):
        return self.amount


class RecurringExpense(Expense):
    def __init__(self, date, category, amount, times_per_month):
        super().__init__(date, category, amount)
        self.times_per_month = times_per_month

    def monthly_cost(self):
        return self.amount * self.times_per_month


class SharedExpense(Expense):
    def __init__(self, date, category, amount, people):
        super().__init__(date, category, amount)
        if people <= 0:
            raise ValueError("Кількість людей має бути більшою за нуль")
        self.people = people

    def monthly_cost(self):
        return self.amount / self.people


class YearlyExpense(Expense):
    def monthly_cost(self):
        return self.amount / 12


print("Illia Basalukk, IT-31")
print("Місячні витрати:\n")

expenses = [
    RecurringExpense("2026-11-01", "transport", 32, 20),
    RecurringExpense("2026-11-01", "mobile", 250, 1),
    SharedExpense("2026-11-01", "rent", 6000, 2),
    SharedExpense("2026-11-01", "internet", 400, 2),
    Expense("2026-11-25", "books", 220),
    YearlyExpense("2026-11-01", "subscription", 1200)
]

total = 0

for expense in expenses:
    cost = expense.monthly_cost()
    total += cost
    print(f"{expense.category:<15} {cost:>10.2f} UAH")

print("-" * 30)
print(f"Загальна місячна вартість: {total:.2f} UAH")
