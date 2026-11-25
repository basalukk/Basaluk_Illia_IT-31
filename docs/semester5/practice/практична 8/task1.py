# Практична 8
# Завдання 1. Словник "про мене"

me = {
    "name": "Illia",
    "surname": "Basalukk",
    "group": "IT-31",
    "city": "Lutsk",
    "birth_year": 2009,
    "hobbies": ["drawing", "gym", "gaming"]
}

# 1. Виведення кожної пари ключ → значення
print("=== Інформація про мене ===")

for key, value in me.items():
    print(f"{key}: {value}")

# 2. Список ключів і кількість пар
print("\n=== Ключі словника ===")
print(list(me.keys()))
print("Кількість пар:", len(me))

# 3. Отримання групи та безпечне отримання email
print("\n=== Додаткова інформація ===")
print("Група:", me["group"])
print("Email:", me.get("email", "unknown"))

# me["email"] викликало б помилку KeyError,
# тому що такого ключа ще немає у словнику.

# 4. Зміна словника

# Додаємо email
me["email"] = "himry12@gmail.com"

# Змінюємо місто
me["city"] = "Lviv"

# Вилучаємо рік народження
removed_year = me.pop("birth_year")

print("\n=== Вилучене значення ===")
print("Вилучений рік народження:", removed_year)

# Виводимо словник після всіх змін
print("\n=== Словник після змін ===")
print(me)

# 5. Перевірка наявності ключа phone
print("\n=== Перевірка phone ===")
print("Чи є ключ phone?", "phone" in me)