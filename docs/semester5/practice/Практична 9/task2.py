# Практична 9. Завдання 2

name = "Illia"
surname = "Basalukk"
group = "IT-31"

# 1. Оцінки одним рядком
grades_text = "6, 7, 8, 9, 10, 5, 8, 11"

# 2. Перетворення рядка на список цілих чисел
grades = [int(grade.strip()) for grade in grades_text.split(",")]

print(f"{name} {surname}, {group}")
print()

print("Grades:", grades)

# 3. Середня, найвища та найнижча оцінки
average = sum(grades) / len(grades)

print(f"Average: {average:.2f}")
print("Highest:", max(grades))
print("Lowest:", min(grades))
print()

# 4. Оцінки через |
grades_line = " | ".join(str(grade) for grade in grades)

print("Grades with |:", grades_line)
print()

# 5. Предмети одним рядком
subjects_text = (
    "Programming, Ukrainian Language, "
    "Operating Systems Administration, "
    "Databases in Information Systems, "
    "Web Resource Development, "
    "IT Law, Foreign Language"
)

subjects = [subject.strip() for subject in subjects_text.split(",")]

# Беремо перші 8 оцінок і перші 8 предметів
subjects = subjects[:len(grades)]

print("Subjects:", subjects)
print()

# 6. Таблиця
print(f"{'#':<4}{'Subject':<35}{'Grade':>5}")
print("-" * 44)

for number, (subject, grade) in enumerate(zip(subjects, grades), start=1):
    print(f"{number:<4}{subject:<35}{grade:>5}")

print()

# 7. Предмет із найдовшою назвою
longest_subject = max(subjects, key=len)

print("Longest subject:", longest_subject)
print("Number of characters:", len(longest_subject))