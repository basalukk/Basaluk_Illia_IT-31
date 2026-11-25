
from pathlib import Path
from datetime import datetime
import random
import math
import csv

print("Illia Basalukk, IT-31")

random.seed(2009)

BASE_DIR = Path(__file__).parent
RESULTS_DIR = BASE_DIR / "results"
HISTORY_FILE = RESULTS_DIR / "history.csv"


def create_questions():
    root_number = random.randint(5, 20)
    square = root_number ** 2

    factorial_number = random.randint(3, 6)

    a = random.randint(20, 60)
    b = random.randint(20, 60)

    n = random.randint(5, 10)
    k = random.randint(2, n - 2)

    percent = random.choice([5, 10, 15, 20, 25])
    amount = random.randint(5, 25) * 20

    return [
        (f"Знайди квадратний корінь з {square}.", math.isqrt(square)),
        (f"Скільки буде {factorial_number}! ?", math.factorial(factorial_number)),
        (f"Знайди НСД чисел {a} і {b}.", math.gcd(a, b)),
        (f"Скільки комбінацій C({n}, {k})?", math.comb(n, k)),
        (f"Скільки становить {percent}% від {amount}?",
         amount * percent // 100)
    ]


def main():
    questions = create_questions()
    score = 0

    print("\nМатематична вікторина!")
    print("Дай відповіді на 5 запитань.\n")

    start_time = datetime.now()

    for number, (question, correct_answer) in enumerate(questions, start=1):
        print(f"{number}. {question}")

        try:
            answer = int(input("Відповідь: "))

            if answer == correct_answer:
                print("Правильно!\n")
                score += 1
            else:
                print(f"Неправильно. Правильна відповідь: {correct_answer}\n")

        except ValueError:
            print(
                f"Потрібно ввести ціле число. "
                f"Правильна відповідь: {correct_answer}\n"
            )

    end_time = datetime.now()
    elapsed = (end_time - start_time).total_seconds()

    print(f"Результат: {score}/5")
    print(f"Час виконання: {elapsed:.2f} секунд")

    RESULTS_DIR.mkdir(exist_ok=True)

    file_exists = HISTORY_FILE.exists()

    with HISTORY_FILE.open("a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        if not file_exists:
            writer.writerow(["date", "score", "time_seconds"])

        writer.writerow([
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            score,
            f"{elapsed:.2f}"
        ])

    with HISTORY_FILE.open("r", newline="", encoding="utf-8") as file:
        history = list(csv.DictReader(file))

    best = max(
        history,
        key=lambda item: (
            int(item["score"]),
            -float(item["time_seconds"])
        )
    )

    print(f"\nУсього спроб: {len(history)}")
    print(
        f"Найкращий результат: {best['score']}/5, "
        f"час: {best['time_seconds']} секунд"
    )


if __name__ == "__main__":
    main()
