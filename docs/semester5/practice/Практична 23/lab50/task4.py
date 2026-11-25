import sys
from exporters import Exporter
from task2 import CsvExporter, JsonExporter, TxtExporter, load_expenses
from task3 import HtmlExporter


print("Illia Basalukk, IT-31")
print("Завдання 4. Вибір формату експорту\n")

exporters = {
    "csv": CsvExporter(),
    "json": JsonExporter(),
    "txt": TxtExporter(),
    "html": HtmlExporter()
}

if len(sys.argv) != 2 or sys.argv[1] not in exporters:
    print("Невідомий формат.")
    print("Доступні формати: csv, json, txt, html")
    raise SystemExit(2)

format_name = sys.argv[1]
expenses = load_expenses()
exporter = exporters[format_name]

path = exporter.target("report")
exporter.export(expenses, path)

print(f"Збережено: {path}")
print(f"Кількість записів: {len(expenses)}")
