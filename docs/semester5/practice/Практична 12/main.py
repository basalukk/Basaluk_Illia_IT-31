
import os
import basalukk_files


print("Illia Basalukk, IT-31")
print("\n--- СПИСОК ФАЙЛІВ ---")

directory = os.path.dirname(os.path.abspath(__file__))

files = basalukk_files.list_files(directory)
for file in files:
    print(file)


print("\n--- ПОШУК ФАЙЛІВ ---")

found = basalukk_files.find_files(directory, "basalukk")
print(found)


print("\n--- СТВОРЕННЯ ФАЙЛУ ---")

path = os.path.join(directory, "Illia_Basalukk_IT-31.txt")

basalukk_files.create_file(
    path,
    "Ім'я: Illia\nПрізвище: Basalukk\nГрупа: IT-31"
)

print("Файл успішно створено:", path)
