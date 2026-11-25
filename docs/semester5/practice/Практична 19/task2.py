class Wallet:
    def __init__(self, owner, balance):
        if not owner.strip():
            raise ValueError("Ім'я власника не може бути порожнім")
        if balance < 0:
            raise ValueError("Баланс не може бути від'ємним")

        self.owner = owner
        self.__balance = round(balance, 2)

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Сума поповнення має бути більшою за нуль")
        self.__balance = round(self.__balance + amount, 2)

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Сума зняття має бути більшою за нуль")
        if amount > self.__balance:
            raise ValueError("Недостатньо коштів на рахунку")
        self.__balance = round(self.__balance - amount, 2)


print("Illia Basalukk, IT-31")

wallet = Wallet("Illia Basalukk", 6000)

wallet.deposit(500)
print(f"Після поповнення: {wallet._Wallet__balance:.2f} UAH")

wallet.withdraw(200)
print(f"Після зняття: {wallet._Wallet__balance:.2f} UAH")

try:
    print(wallet.__balance)
except AttributeError as error:
    print("Помилка доступу:", error)

print("Доступ через name mangling:", wallet._Wallet__balance)

try:
    wallet.withdraw(10000)
except ValueError as error:
    print("Помилка зняття:", error)
