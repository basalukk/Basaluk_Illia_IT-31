# Практична 7
# Завдання 1. Список власних оцінок

c = 8

grades = [6, 7, 8, 9, 10, 5, 8, 11]

print("=== Мої оцінки ===")
print("Grades:", grades)
print("Кількість оцінок:", len(grades))
print("Сума:", sum(grades))
print("Найкраща оцінка:", max(grades))
print("Найгірша оцінка:", min(grades))
print("Середня оцінка:", f"{sum(grades) / len(grades):.2f}")

# Сортування копії, оригінальний список не змінюється
sorted_grades = sorted(grades, reverse=True)

print("\n=== Оцінки від найкращої до найгіршої ===")
print(sorted_grades)
print("Оригінальний список:", grades)

# Три найкращі та три найгірші
print("\n=== Три найкращі оцінки ===")
print(sorted_grades[:3])

print("=== Три найгірші оцінки ===")
print(sorted_grades[-3:])

# Позиція найгіршої оцінки
worst_position = grades.index(min(grades)) + 1
print("\nНайгірша оцінка була за порядком:", worst_position)

# Оцінки вище середнього
average = sum(grades) / len(grades)
above_average = [grade for grade in grades if grade > average]

print("\n=== Оцінки вище середнього ===")
print(above_average)
print("Їх кількість:", len(above_average))

# Перевірка 12 та 1
print("\nЧи є оцінка 12?", 12 in grades)
print("Чи є оцінка 1?", 1 in grades)

# Додаємо оцінку в кінець
grades.append(c % 12 + 1)
print("\nПісля додавання оцінки в кінець:", grades)

# Вставляємо 12 на початок
grades.insert(0, 12)
print("Після вставки 12 на початок:", grades)

# Вилучаємо найгіршу оцінку
grades.remove(min(grades))
print("Після вилучення найгіршої оцінки:", grades)

# Вилучаємо останню оцінку
removed_last = grades.pop()
print("Вилучена остання оцінка:", removed_last)
print("Після вилучення останньої оцінки:", grades)

# Кількість оцінок 12
print("\nКількість оцінок 12:", grades.count(12))

# Сортування самого списку
sort_result = grades.sort(reverse=True)

print("\n=== Остаточне сортування ===")
print("Значення, яке повернув sort():", sort_result)
print("Відсортований список:", grades)