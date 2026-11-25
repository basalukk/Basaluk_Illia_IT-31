import sys
import shutil
from pathlib import Path

NAME = "Illia"
SURNAME = "Basalukk"
GROUP = "IT-31"


def main():
    print(f"{NAME} {SURNAME}, {GROUP}")

    args = sys.argv[1:]
    force = False

    if args and args[0] == "--force":
        force = True
        args = args[1:]

    if len(args) != 2:
        print(
            "Використання: python task2.py [--force] <джерело> <призначення>",
            file=sys.stderr
        )
        return 2

    source = Path(args[0])
    destination = Path(args[1])

    try:
        if not source.exists():
            raise FileNotFoundError(
                f"джерело не знайдено: {source}"
            )

        if source.is_dir():
            raise IsADirectoryError(
                "джерело є папкою"
            )

        if source.resolve() == destination.resolve():
            raise shutil.SameFileError(
                "джерело та призначення — один і той самий файл"
            )

        if destination.exists() and destination.is_dir():
            raise IsADirectoryError(
                "призначення є папкою"
            )

        if not destination.parent.exists():
            raise FileNotFoundError(
                f"папка призначення не існує: {destination.parent}"
            )

        if destination.exists() and not force:
            raise FileExistsError(
                "файл призначення вже існує. Використайте --force"
            )

        shutil.copyfile(source, destination)

        print("Файл успішно скопійовано:")
        print(f"  Джерело: {source}")
        print(f"  Призначення: {destination}")

        return 0

    except (
        FileNotFoundError,
        IsADirectoryError,
        FileExistsError,
        PermissionError,
        shutil.SameFileError
    ) as error:
        print(
            f"Помилка — {type(error).__name__}: {error}",
            file=sys.stderr
        )
        return 1


if __name__ == "__main__":
    sys.exit(main())