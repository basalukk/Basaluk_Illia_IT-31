import csv
import json
from pathlib import Path
from exporters import Exporter


class CsvExporter(Exporter):
    def extension(self):
        return "csv"

    def export(self, expenses, path):
        with open(path, "w", newline="", encoding="utf-8-sig") as file:
            writer = csv.writer(file, delimiter=";")
            writer.writerow(["date", "category", "amount", "note"])

            for expense in expenses:
                writer.writerow([
                    expense["date"],
                    expense["category"],
                    expense["amount"],
                    expense["note"]
                ])


class JsonExporter(Exporter):
    def extension(self):
        return "json"

    def export(self, expenses, path):
        with open(path, "w", encoding="utf-8") as file:
            json.dump(expenses, file, ensure_ascii=False, indent=4)


class TxtExporter(Exporter):
    def extension(self):
        return "txt"

    def export(self, expenses, path):
        with open(path, "w", encoding="utf-8") as file:
            file.write("ЗВІТ ПРО ВИТРАТИ\n")
            file.write("=" * 75 + "\n")
            file.write(f"{'Дата':<12} {'Категорія':<14} {'Сума':>10}  Примітка\n")
            file.write("-" * 75 + "\n")

            for expense in expenses:
                file.write(
                    f"{expense['date']:<12} "
                    f"{expense['category']:<14} "
                    f"{float(expense['amount']):>10.2f}  "
                    f"{expense['note']}\n"
                )


def load_expenses():
    expenses = []

    with open("data/expenses.csv", "r", encoding="utf-8-sig") as file:
        header = file.readline().strip().lstrip("#").strip().split(";")
        reader = csv.DictReader(file, fieldnames=header, delimiter=";")

        for row in reader:
            expenses.append({
                "date": row["date"],
                "category": row["category"],
                "amount": float(row["amount"]),
                "note": row["note"]
            })

    return expenses


def main():
    print("Illia Basalukk, IT-31")
    print("Завдання 2. Три реалізації експортерів\n")

    expenses = load_expenses()

    exporters = [
        CsvExporter(),
        JsonExporter(),
        TxtExporter()
    ]

    for exporter in exporters:
        path = exporter.target("report")
        exporter.export(expenses, path)
        print(f"saved: {path} ({len(expenses)} records)")


if __name__ == "__main__":
    main()
