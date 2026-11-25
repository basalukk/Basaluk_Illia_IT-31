import sys
from pathlib import Path


NAME = "Illia"
SURNAME = "Basalukk"
GROUP = "IT-31"


def check_file(file_path):
    path = Path(file_path)

    try:
        if path.is_dir():
            raise IsADirectoryError("це папка, а не файл")

        with path.open("r", encoding="utf-8") as file:
            lines = file.readlines()

        if not lines:
            raise ValueError("файл порожній")

        first_line = lines[0].rstrip("\n")

        print(f"{file_path}: {len(lines)} рядків")
        print(f"Перший рядок: {first_line}")
        return True

    except (FileNotFoundError, PermissionError, IsADirectoryError,
            UnicodeDecodeError, ValueError) as error:
        print(
            f"{file_path}: помилка — {type(error).__name__}: {error}",
            file=sys.stderr
        )
        return False


def main():
    print(f"{NAME} {SURNAME}, {GROUP}")

    if len(sys.argv) < 2:
        print("Помилка: потрібно вказати хоча б один шлях до файлу.",
              file=sys.stderr)
        return 2

    checked = 0
    failed = 0

    for file_path in sys.argv[1:]:
        checked += 1

        if not check_file(file_path):
            failed += 1

    print(f"\nПеревірено: {checked}")
    print(f"Помилок: {failed}")

    if failed > 0:
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())