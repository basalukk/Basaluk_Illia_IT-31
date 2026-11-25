
import os


def list_files(directory):
    """
    Повертає список файлів у вказаній директорії.

    Параметри:
        directory (str): шлях до директорії.

    Результат:
        list: список назв файлів.
    """
    return [
        file for file in os.listdir(directory)
        if os.path.isfile(os.path.join(directory, file))
    ]


def find_files(directory, substring):
    """
    Шукає файли, у назві яких є заданий підрядок.

    Параметри:
        directory (str): шлях до директорії.
        substring (str): підрядок для пошуку.

    Результат:
        list: список знайдених файлів.
    """
    return [
        file for file in list_files(directory)
        if substring in file
    ]


def create_file(path, text):
    """
    Створює файл і записує в нього текст.

    Параметри:
        path (str): шлях до файлу.
        text (str): текст для запису.

    Результат:
        str: шлях до створеного файлу.
    """
    with open(path, "w", encoding="utf-8") as file:
        file.write(text)

    return path


if __name__ == "__main__":
    print("Модуль basalukk_files.py працює правильно!")

    test_files = list_files(".")
    print("Файли в поточній папці:", test_files)

    found_files = find_files(".", "basalukk")
    print("Знайдені файли:", found_files)
