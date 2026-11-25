from pathlib import Path
from collections import defaultdict
import sys


NAME = "Illia"
SURNAME = "Basalukk"
GROUP = "IT-31"

SCRIPT_DIR = Path(__file__).resolve().parent
DATA_DIR = SCRIPT_DIR / "data"
EXPENSES_FILE = DATA_DIR / "expenses.csv"
REPORTS_DIR = SCRIPT_DIR / "reports"
REPORT_FILE = REPORTS_DIR / "expenses_report.txt"


def usage():
    print("usage: python task3.py add <date> <category> <amount> <note>")
    print("       python task3.py list")
    print("       python task3.py report")


def ensure_file():
    DATA_DIR.mkdir(exist_ok=True)

    if not EXPENSES_FILE.exists():
        EXPENSES_FILE.write_text(
            "# date;category;amount;note\n",
            encoding="utf-8"
        )


def load_expenses():
    ensure_file()

    expenses = []

    with EXPENSES_FILE.open("r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()

            if not line or line.startswith("#"):
                continue

            parts = line.split(";", 3)

            if len(parts) != 4:
                continue

            date, category, amount, note = parts

            try:
                amount = float(amount)
            except ValueError:
                continue

            expenses.append({
                "date": date,
                "category": category,
                "amount": amount,
                "note": note
            })

    return expenses


def add_expense(args):
    if len(args) < 4:
        print("error: add needs date, category, amount and note")
        usage()
        return

    date = args[0]
    category = args[1]

    try:
        amount = float(args[2])
    except ValueError:
        print("error: amount must be a number")
        return

    note = " ".join(args[3:])

    ensure_file()

    with EXPENSES_FILE.open("a", encoding="utf-8") as file:
        file.write(f"{date};{category};{amount:.2f};{note}\n")

    print(f"added: {date} {category} {amount:.2f} ({note})")


def list_expenses():
    expenses = load_expenses()

    if not expenses:
        print("no expenses")
        return

    print(f"{'date':<12} {'category':<15} {'amount':>8}  note")
    print("-" * 65)

    for expense in expenses:
        print(
            f"{expense['date']:<12} "
            f"{expense['category']:<15} "
            f"{expense['amount']:>8.2f}  "
            f"{expense['note']}"
        )

    total = sum(e["amount"] for e in expenses)

    print()
    print(f"{len(expenses)} records, total {total:.2f}")


def report():
    expenses = load_expenses()

    if not expenses:
        print("no expenses")
        return

    total = sum(e["amount"] for e in expenses)

    categories = defaultdict(lambda: {
        "count": 0,
        "total": 0
    })

    days = defaultdict(float)

    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]

        categories[category]["count"] += 1
        categories[category]["total"] += amount
        days[expense["date"]] += amount

    first_date = min(e["date"] for e in expenses)
    last_date = max(e["date"] for e in expenses)

    lines = []

    lines.append(
        f"Expenses report for {NAME} {SURNAME} ({GROUP})"
    )
    lines.append(f"Period: {first_date} .. {last_date}")
    lines.append(f"Records: {len(expenses)}")
    lines.append("")

    lines.append(
        f"{'category':<15} {'count':>5} {'total':>10} "
        f"{'share':>8}  chart"
    )
    lines.append("-" * 65)

    sorted_categories = sorted(
        categories.items(),
        key=lambda item: item[1]["total"],
        reverse=True
    )

    for category, data in sorted_categories:
        share = data["total"] / total * 100
        bars = "#" * int(share / 5)

        lines.append(
            f"{category:<15} "
            f"{data['count']:>5} "
            f"{data['total']:>10.2f} "
            f"{share:>7.1f}%  "
            f"{bars}"
        )

    lines.append("-" * 65)

    lines.append(
        f"{'total':<15} "
        f"{len(expenses):>5} "
        f"{total:>10.2f} "
        f"{100.0:>7.1f}%"
    )

    top_day = max(days.items(), key=lambda item: item[1])

    most_expensive = max(
        expenses,
        key=lambda expense: expense["amount"]
    )

    average_per_day = total / len(days)

    lines.append("")
    lines.append(
        f"Top day: {top_day[0]} ({top_day[1]:.2f})"
    )
    lines.append(
        f"Most expensive: "
        f"{most_expensive['category']} "
        f"{most_expensive['amount']:.2f} "
        f"({most_expensive['note']})"
    )
    lines.append(
        f"Average per day: {average_per_day:.2f}"
    )

    REPORTS_DIR.mkdir(exist_ok=True)

    report_text = "\n".join(lines)

    REPORT_FILE.write_text(
        report_text,
        encoding="utf-8"
    )

    print(report_text)
    print()
    print(f"report saved to: {REPORT_FILE}")


def main():
    if len(sys.argv) < 2:
        usage()
        return

    command = sys.argv[1]

    if command == "add":
        add_expense(sys.argv[2:])

    elif command == "list":
        list_expenses()

    elif command == "report":
        report()

    else:
        print(f"error: unknown command {command}")
        usage()


if __name__ == "__main__":
    main()