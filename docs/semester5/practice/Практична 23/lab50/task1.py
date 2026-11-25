from exporters import Exporter

print("Illia Basalukk, IT-31")
print("Завдання 1. Абстрактний експортер")

try:
    exporter = Exporter()
except TypeError as error:
    print("Очікувана помилка:")
    print(error)
