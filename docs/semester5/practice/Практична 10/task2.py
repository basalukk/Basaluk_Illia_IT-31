from pathlib import Path
from datetime import datetime


NAME = "Illia"
SURNAME = "Basalukk"


def count_runs(path):
    if not path.exists():
        return 0

    with path.open("r", encoding="utf-8") as file:
        return sum(1 for line in file if line.strip())


def add_run(path, number):
    path.parent.mkdir(exist_ok=True)

    stamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with path.open("a", encoding="utf-8") as file:
        file.write(f"{number};{stamp};{NAME} {SURNAME}\n")


def show_history(path, last=3):
    if not path.exists():
        print("runs so far: 0")
        return

    with path.open("r", encoding="utf-8") as file:
        lines = [line.strip() for line in file if line.strip()]

    print(f"runs so far: {len(lines)}")
    print("last runs:")

    for line in lines[-last:]:
        number, stamp, name = line.split(";", 2)
        print(f"  # {number}  {stamp}  {name}")

    if lines:
        first_number, first_stamp, first_name = lines[0].split(";", 2)
        print(f"first run was at {first_stamp}")


def main():
    script_dir = Path(__file__).resolve().parent
    path = script_dir / "data" / "runs.log"

    runs = count_runs(path)
    current_run = runs + 1

    add_run(path, current_run)

    print(f"Hello, {NAME} {SURNAME}! This is run number {current_run}.")

    if current_run == 1:
        print("runs.log was just created.")

    show_history(path)


if __name__ == "__main__":
    main()