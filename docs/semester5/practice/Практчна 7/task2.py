# Практична 7
# Завдання 2. Прізвище як список літер

surname = "Basalukk"

letters = list(surname.lower())
c = len(letters)

print("=== Прізвище як список літер ===")
print("Прізвище:", surname)
print("Список:", letters)
print("Довжина:", c)

# Перша, середня та остання літери
print("\n=== Літери ===")
print("Перша літера:", letters[0])
print("Середня літера:", letters[c // 2])
print("Остання літера:", letters[-1])
print("Остання літера другим способом:", letters[c - 1])

# Зрізи
print("\n=== Зрізи списку ===")
print("Перші три літери:", letters[:3])
print("Усі, крім перших трьох:", letters[3:])
print("Кожна друга літера:", letters[::2])
print("Зворотний порядок:", letters[::-1])
print("Останні дві літери:", letters[-2:])

# Частина списку довжиною 5, що починається з позиції c
print("Зріз з позиції c довжиною 5:", letters[c:c + 5])

# Унікальні літери без повторів
unique = []

for letter in letters:
    if letter not in unique:
        unique.append(letter)

print("\n=== Унікальні літери ===")
print(unique)

# Повторювані літери
repeated = False

for letter in unique:
    count = letters.count(letter)

    if count > 1:
        print(f"Літера '{letter}' повторюється {count} рази")
        repeated = True

if not repeated:
    print("No repeated letters")

# Алфавітний порядок
print("\n=== Алфавітний порядок ===")
print(sorted(letters))