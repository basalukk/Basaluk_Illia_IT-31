class Wallet:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
        print(f"Створено гаманець: {self.owner}")

    def __del__(self):
        print(f"wallet of {self.owner} deleted")


print("Illia Basalukk, IT-31")

print("\n1. Видалення об'єкта:")
wallet = Wallet("Illia Basalukk", 6000)
del wallet
print("Об'єкт wallet видалено")

print("\n2. Друге посилання на об'єкт:")
wallet = Wallet("Illia Basalukk", 6000)
other = wallet
del wallet
print("Видалено лише перше посилання")
del other
print("Видалено друге посилання")

print("\n3. Видалення наприкінці програми:")
wallet = Wallet("Illia Basalukk", 4702)
print("Програма завершується")
