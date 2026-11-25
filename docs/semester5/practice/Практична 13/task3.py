
from pathlib import Path
from datetime import datetime
import math
import sys

print("Illia Basalukk, IT-31")

def human_size(size):
    if size == 0:
        return "0 B"

    units = ["B", "KB", "MB", "GB", "TB"]
    index = min(int(math.log(size, 1024)), len(units) - 1)
    value = size / (1024 ** index)

    return f"{value:.2f} {units[index]}"


def main():
    args = sys.argv[1:]
    dry_run = False

    if "--dry-run" in args:
        dry_run = True
        args.remove("--dry-run")

    if len(args) != 1:
        print(
            "Використання: python task3.py [--dry-run] <папка>",
            file=sys.stderr
        )
        sys.exit(2)

    source_dir = Path(args[0])

    if not source_dir.exists() or not source_dir.is_dir():
        print("Помилка: вказана папка не існує.", file=sys.stderr)
        sys.exit(1)

    files = [item for item in source_dir.iterdir() if item.is_file()]

    if not files:
        print("У папці немає файлів.")
        sys.exit(0)

    file_info = []

    for file_path in files:
        modified = datetime.fromtimestamp(file_path.stat().st_mtime)
        folder_name = modified.strftime("%Y-%m")
        size = file_path.stat().st_size

        file_info.append((modified, file_path, folder_name, size))

    file_info.sort(key=lambda item: item[0])

    print("\nФайли від найстарішого до найновішого:")

    for modified, file_path, folder_name, size in file_info:
        print(
            f"{modified:%d.%m.%Y %H:%M} | "
            f"{human_size(size):>10} | "
            f"{folder_name}/{file_path.name}"
        )

    destinations = [
        source_dir / folder_name / file_path.name
        for _, file_path, folder_name, _ in file_info
    ]

    conflicts = [
        destination
        for destination in destinations
        if destination.exists()
    ]

    if conflicts:
        print("\nКонфлікт: файли з такими іменами вже існують:")
        for conflict in conflicts:
            print(conflict)
        sys.exit(1)

    if not dry_run:
        for modified, file_path, folder_name, size in file_info:
            target_dir = source_dir / folder_name
            target_dir.mkdir(exist_ok=True)
            file_path.rename(target_dir / file_path.name)

        print("\nФайли успішно розсортовано.")
    else:
        print("\nРежим dry-run: файли не переміщувалися.")

    report_dir = Path(__file__).parent / "reports"
    report_dir.mkdir(exist_ok=True)

    report_time = datetime.now().strftime("%Y%m%d_%H%M")
    report_path = report_dir / f"organize_{report_time}.txt"

    with report_path.open("w", encoding="utf-8") as report:
        report.write("Illia Basalukk, IT-31\n")
        report.write("Звіт сортування файлів\n\n")

        for modified, file_path, folder_name, size in file_info:
            report.write(
                f"{modified:%d.%m.%Y %H:%M} | "
                f"{human_size(size)} | "
                f"{folder_name}/{file_path.name}\n"
            )

        report.write(
            "\nРежим: "
            + ("dry-run" if dry_run else "переміщення")
            + "\n"
        )

    print(f"Звіт збережено: {report_path}")


if __name__ == "__main__":
    main()
