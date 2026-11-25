import sys
import csv
from datetime import datetime
from decimal import Decimal, InvalidOperation
from pathlib import Path

NAME = "Illia"
SURNAME = "Basalukk"
GROUP = "IT-31"


def print_error(message):
    print(f"Помилка: {message}", file=sys.stderr)


def read_expenses(path):
    expenses = []

    try:
        if not path.exists():
            raise FileNotFoundError(f"файл не знайдено: {path}")

        if path.is_dir():
            raise IsADirectoryError(f"це папка, а не файл: {path}")

        with path.open("r", encoding="utf-8", newline="") as file:
            reader = csv.reader(file, delimiter=";")

            for line_number, row in enumerate(reader, start=1):
                if line_number == 1:
                    continue

                if not row or all(not item.strip() for item in row):
                    continue

                if len(row) != 4:
                    print(
                        f"Пропущено рядок {line_number}: очікується 4 поля",
                        file=sys.stderr
                    )
                    continue

                date_text, category, amount_text, note = [
                    item.strip() for item in row
                ]

                try:
                    date = datetime.strptime(
                        date_text, "%Y-%m-%d"
                    ).date()
                except ValueError:
                    print(
                        f"Пропущено рядок {line_number}: некоректна дата",
                        file=sys.stderr
                    )
                    continue

                try:
                    amount = Decimal(amount_text)
                except InvalidOperation:
                    print(
                        f"Пропущено рядок {line_number}: некоректна сума",
                        file=sys.stderr
                    )
                    continue

                if amount < 0:
                    print(
                        f"Пропущено рядок {line_number}: "
                        f"сума не може бути від'ємною",
                        file=sys.stderr
                    )
                    continue

                expenses.append({
                    "date": date,
                    "category": category,
                    "amount": amount,
                    "note": note
                })

    except (
        FileNotFoundError,
        IsADirectoryError,
        UnicodeDecodeError
    ) as error:
        print_error(f"{type(error).__name__}: {error}")
        return None

    return expenses


def add_expense(path, date_text, category, amount_text, note):
    try:
        date = datetime.strptime(
            date_text, "%Y-%m-%d"
        ).date()
    except ValueError:
        print_error("некоректна дата")
        return 1

    try:
        amount = Decimal(amount_text)
    except InvalidOperation:
        print_error("некоректна сума")
        return 1

    if amount < 0:
        print_error("сума не може бути від'ємною")
        return 1

    try:
        if not path.exists():
            raise FileNotFoundError(f"файл не знайдено: {path}")

        if path.is_dir():
            raise IsADirectoryError(f"це папка, а не файл: {path}")

        with path.open("r", encoding="utf-8") as file:
            lines = file.readlines()

        if not lines:
            print_error("файл порожній")
            return 1

        with path.open("a", encoding="utf-8", newline="") as file:
            writer = csv.writer(file, delimiter=";")
            writer.writerow([
                date.isoformat(),
                category,
                amount,
                note
            ])

    except (
        FileNotFoundError,
        IsADirectoryError,
        UnicodeDecodeError
    ) as error:
        print_error(f"{type(error).__name__}: {error}")
        return 1

    print("Витрату успішно додано.")
    return 0


def main():
    print(f"{NAME} {SURNAME}, {GROUP}")

    args = sys.argv[1:]

    if not args:
        print(
            "Використання: python task3.py "
            "[list|report|add] [файл] <аргументи>",
            file=sys.stderr
        )
        return 2

    command = args[0]

    if command == "list":
        if len(args) == 1:
            path = Path("data/expenses.csv")
        elif len(args) == 2:
            path = Path(args[1])
        else:
            print(
                "Використання: python task3.py list [файл]",
                file=sys.stderr
            )
            return 2

        expenses = read_expenses(path)

        if expenses is None:
            return 1

        if not expenses:
            print("Немає витрат.")
            return 0

        for expense in expenses:
            print(
                f"{expense['date']} | "
                f"{expense['category']} | "
                f"{expense['amount']:.2f} | "
                f"{expense['note']}"
            )

        return 0

    if command == "report":
        if len(args) == 1:
            path = Path("data/expenses.csv")
        elif len(args) == 2:
            path = Path(args[1])
        else:
            print(
                "Використання: python task3.py report [файл]",
                file=sys.stderr
            )
            return 2

        expenses = read_expenses(path)

        if expenses is None:
            return 1

        if not expenses:
            print("Нічого звітувати.")
            return 1

        total = sum(
            (expense["amount"] for expense in expenses),
            Decimal("0")
        )

        categories = {}

        for expense in expenses:
            category = expense["category"]
            categories[category] = (
                categories.get(category, Decimal("0"))
                + expense["amount"]
            )

        print(f"Кількість витрат: {len(expenses)}")
        print(f"Загальна сума: {total:.2f}")
        print("За категоріями:")

        for category, amount in sorted(categories.items()):
            print(f"  {category}: {amount:.2f}")

        return 0

    if command == "add":
        if len(args) != 5:
            print(
                "Використання: python task3.py "
                "add <дата> <категорія> <сума> <опис>",
                file=sys.stderr
            )
            return 2

        path = Path("data/expenses.csv")

        return add_expense(
            path,
            args[1],
            args[2],
            args[3],
            args[4]
        )

    print(
        f"Невідома команда: {command}",
        file=sys.stderr
    )
    return 2


if __name__ == "__main__":
    sys.exit(main())