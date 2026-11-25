import json
from datetime import date

print("Illia Basalukk, IT-31")

original = {
    "owner": "Illia Basalukk",
    "group": "IT-31",
    "created": date.today(),
    "category": "food"
}

# Початкова помилка
try:
    json.dumps(original)
except TypeError as error:
    print("TypeError:", error)

# Спосіб 1: параметр default
json_text = json.dumps(original, default=lambda value: value.isoformat())
restored = json.loads(json_text)
print("Method 1:", restored)

# Спосіб 2: власні функції перетворення
def convert_dates(data):
    return {
        key: value.isoformat() if isinstance(value, date) else value
        for key, value in data.items()
    }

def restore_dates(data):
    return {
        key: date.fromisoformat(value)
        if key == "created" else value
        for key, value in data.items()
    }

with open("dates.json", "w", encoding="utf-8") as file:
    json.dump(convert_dates(original), file, indent=2, ensure_ascii=False)

with open("dates.json", "r", encoding="utf-8") as file:
    loaded = json.load(file)

restored_original = restore_dates(loaded)

print("Method 2:", restored_original)
print("Data equal:", restored_original == original)
print("Date type:", type(restored_original["created"]))
