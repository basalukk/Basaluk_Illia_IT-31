# Практична 8
# Завдання 2. Розклад тижня

schedule = {
    "Mon": [
        "Programming",
        "Ukrainian Language",
        "Operating Systems Administration"
    ],
    "Tue": [
        "Programming",
        "IT Law",
        "Databases in Information Systems"
    ],
    "Wed": [
        "Foreign Language",
        "Databases in Operating Systems",
        "Web Resource Development"
    ],
    "Thu": [
        "Programming",
        "Web Development",
        "Operating Systems Administration"
    ],
    "Fri": [
        "Foreign Language",
        "Web Resource Development",
        "IT Law"
    ]
}

# 1. Виведення таблиці розкладу
print("=== Розклад тижня ===")
print(f"{'День':<6} {'Кількість пар':<15} Предмети")

for day, subjects in schedule.items():
    print(f"{day:<6} {len(subjects):<15} {', '.join(subjects)}")

# 2. Загальна кількість пар
total_lessons = sum(len(subjects) for subjects in schedule.values())

print("\n=== Загальна кількість пар ===")
print(total_lessons)

# 3. День із найбільшою кількістю пар
max_day = max(schedule, key=lambda day: len(schedule[day]))

print("\n=== Найбільше пар ===")
print(max_day, "-", len(schedule[max_day]), "пари")

# 4. Множина всіх різних предметів
all_subjects = set()

for subjects in schedule.values():
    all_subjects.update(subjects)

print("\n=== Усі різні предмети ===")
print(all_subjects)
print("Кількість різних предметів:", len(all_subjects))

# 5. Порівняння понеділка і середи
monday_subjects = set(schedule["Mon"])
wednesday_subjects = set(schedule["Wed"])

print("\n=== Порівняння понеділка і середи ===")

both_days = monday_subjects & wednesday_subjects
print("Є і в понеділок, і в середу:", both_days)

only_monday = monday_subjects - wednesday_subjects
print("Є в понеділок, але немає в середу:", only_monday)

# 6. Функція підрахунку кількості пар кожного предмета
def count_subjects(schedule):
    subject_count = {}

    for subjects in schedule.values():
        for subject in subjects:
            subject_count[subject] = subject_count.get(subject, 0) + 1

    return subject_count


subject_counts = count_subjects(schedule)

print("\n=== Кількість пар кожного предмета ===")
for subject, count in subject_counts.items():
    print(f"{subject}: {count}")

# 7. Рейтинг предметів
rating = sorted(
    subject_counts.items(),
    key=lambda item: item[1],
    reverse=True
)

print("\n=== Рейтинг предметів ===")

for number, (subject, count) in enumerate(rating, start=1):
    print(f"{number}. {subject} — {count} пар")