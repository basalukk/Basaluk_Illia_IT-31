from exporters import Exporter
from task2 import load_expenses


class HtmlExporter(Exporter):
    def extension(self):
        return "html"

    def export(self, expenses, path):
        with open(path, "w", encoding="utf-8") as file:
            file.write("""<!DOCTYPE html>
<html lang="uk">
<head>
<meta charset="UTF-8">
<title>Звіт про витрати</title>
<style>
body { font-family: Arial; margin: 30px; }
table { border-collapse: collapse; width: 100%; }
th, td { border: 1px solid #999; padding: 10px; }
th { background: #e5e5e5; }
</style>
</head>
<body>
<h1>Звіт про витрати — Illia Basalukk, IT-31</h1>
<table>
<tr><th>Дата</th><th>Категорія</th><th>Сума (UAH)</th><th>Примітка</th></tr>
""")
            for expense in expenses:
                file.write(
                    f"<tr><td>{expense['date']}</td>"
                    f"<td>{expense['category']}</td>"
                    f"<td>{float(expense['amount']):.2f}</td>"
                    f"<td>{expense['note']}</td></tr>\n"
                )
            file.write("</table></body></html>")


if __name__ == "__main__":
    print("Illia Basalukk, IT-31")
    print("Завдання 3. HTML-експортер\n")

    try:
        class IncompleteHtmlExporter(Exporter):
            def extension(self):
                return "html"

        IncompleteHtmlExporter()
    except TypeError as error:
        print("Очікувана помилка:")
        print(error)

    expenses = load_expenses()
    exporter = HtmlExporter()
    path = exporter.target("report")
    exporter.export(expenses, path)

    print("HTML-звіт створено:", path)
    print("Кількість записів:", len(expenses))
