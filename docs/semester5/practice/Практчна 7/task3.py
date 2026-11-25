# Практична 7
# Завдання 3. Предмети семестру


def create_subjects():
    subjects = [
        ("Programming", 3, 7),
        ("Operating Systems Administration", 2, 8),
        ("IT Law", 2, 7),
        ("Foreign Language", 2, 9),
        ("Web Resource Development", 2, 10)
    ]

    return subjects


def print_table(subjects):
    print("Illia Basalukk, IT-31")
    print("#  Subject                              Pairs  Grade")

    for number, (title, pairs, grade) in enumerate(subjects, start=1):
        print(f"{number:<3}{title:<37}{pairs:<7}{grade}")


def total_pairs(subjects):
    return sum(pairs for _, pairs, _ in subjects)


def print_most_and_weakest(subjects):
    most_pairs = max(subjects, key=lambda subject: subject[1])
    weakest = min(subjects, key=lambda subject: subject[2])

    print(
        f"Most pairs: {most_pairs[0]} ({most_pairs[1]})"
    )

    print(
        f"Weakest subject: {weakest[0]} ({weakest[2]})"
    )


def print_statistics(subjects):
    titles = [title for title, _, _ in subjects]
    grades = [grade for _, _, grade in subjects]

    average = sum(grades) / len(grades)

    print("Titles:", titles)
    print(f"Grades: {grades}, average: {average:.2f}")


def print_high_grades(subjects):
    high_grades = [
        title for title, _, grade in subjects
        if grade >= 10
    ]

    print("Grade 10+:", high_grades)


def print_histograms(subjects):
    for title, _, grade in subjects:
        print(f"{title}: {'#' * grade}")


def retake_lowest(subjects):
    weakest = min(subjects, key=lambda subject: subject[2])

    old_grade = weakest[2]
    new_grade = min(old_grade + 2, 12)

    updated_subjects = []

    for subject in subjects:
        if subject == weakest:
            updated_subjects.append(
                (subject[0], subject[1], new_grade)
            )
        else:
            updated_subjects.append(subject)

    print(f"Retake: {weakest[0]} {old_grade} -> {new_grade}")

    return updated_subjects


def main():
    subjects = create_subjects()

    print_table(subjects)

    print("\nPairs per week:", total_pairs(subjects))

    print_most_and_weakest(subjects)

    print_statistics(subjects)

    print_high_grades(subjects)

    print_histograms(subjects)

    subjects = retake_lowest(subjects)

    print("Subjects:", subjects)


main()