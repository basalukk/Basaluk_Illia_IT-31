
from pathlib import Path
from datetime import date, timedelta
import math
import sys

print("Illia Basalukk, IT-31")

BASE_DIR = Path(__file__).parent
FILE_PATH = BASE_DIR / "data" / "expenses.csv"

expenses = []

try:
    with FILE_PATH.open("r", encoding="utf-8-sig") as file:
        for line_number, line in enumerate(file, start=1):
            line = line.strip()

            if not line or line.startswith("#"):
                continue

            try:
                parts = line.split(";")

                if len(parts) != 4:
                    raise ValueError("неправильна кількість полів")

                expense_date = date.fromisoformat(parts[0])
                amount = float(parts[2])

                if amount < 0:
                    raise ValueError("сума не може бути від'ємною")

                expenses.append((expense_date, amount))

            except ValueError as error:
                print(
                    f"Попередження: рядок {line_number}: {error}",
                    file=sys.stderr
                )

except FileNotFoundError:
    print("Помилка: файл expenses.csv не знайдено.", file=sys.stderr)
    sys.exit(1)

if not expenses:
    print("Помилка: немає даних для аналізу.", file=sys.stderr)
    sys.exit(1)

expenses.sort(key=lambda item: item[0])

first_date = expenses[0][0]
last_date = expenses[-1][0]

period_days = (last_date - first_date).days + 1

print(
    f"period: {first_date.strftime('%d.%m.%Y')} "
    f"({first_date.strftime('%A')}) - "
    f"{last_date.strftime('%d.%m.%Y')} "
    f"({last_date.strftime('%A')}), {period_days} days"
)

daily_expenses = {}

current_date = first_date

while current_date <= last_date:
    daily_expenses[current_date] = []
    current_date += timedelta(days=1)

for expense_date, amount in expenses:
    daily_expenses[expense_date].append(amount)

daily_totals = {
    day: math.fsum(amounts)
    for day, amounts in daily_expenses.items()
}

weekday_names = [
    "Monday", "Tuesday", "Wednesday",
    "Thursday", "Friday", "Saturday", "Sunday"
]

weekday_totals = [[] for _ in range(7)]

for day, total in daily_totals.items():
    weekday_totals[day.weekday()].append(total)

print("\nweekday      total")

for i in range(7):
    total = math.fsum(weekday_totals[i])
    print(f"{weekday_names[i]:12} {total:8.2f}")

total_expenses = math.fsum(daily_totals.values())

average = total_expenses / period_days

variance = math.fsum(
    (amount - average) ** 2
    for amount in daily_totals.values()
) / period_days

standard_deviation = math.sqrt(variance)

top_day = max(daily_totals, key=daily_totals.get)
top_amount = daily_totals[top_day]

no_spend_days = sum(
    1 for amount in daily_totals.values()
    if amount == 0
)

print(f"\ntotal:         {total_expenses:.2f}")
print(f"per day:       {average:.2f} +- {standard_deviation:.2f}")

print(
    f"top day:       {top_day.strftime('%d.%m.%Y')} "
    f"({top_day.strftime('%A')}), {top_amount:.2f}"
)

print(f"no-spend days: {no_spend_days}")

next_month = date(
    last_date.year + (last_date.month == 12),
    last_date.month % 12 + 1,
    1
)

this_month = date(last_date.year, last_date.month, 1)

days_in_month = (next_month - this_month).days
days_left = (next_month - last_date).days

forecast = average * days_in_month

print(
    f"days in {last_date.strftime('%B')}: "
    f"{days_in_month}, left after {last_date.strftime('%d.%m')}: {days_left}"
)

print(f"month forecast: {forecast:.2f}")
