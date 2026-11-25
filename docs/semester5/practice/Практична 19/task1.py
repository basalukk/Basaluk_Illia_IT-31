class Wallet:
    def __init__(self, owner, balance):
        if not owner.strip():
            raise ValueError("Ім'я власника не може бути порожнім")

        if balance < 0:
            raise ValueError("Початковий баланс не може бути від'ємним")

        self.owner = owner
        self.balance = round(balance, 2)


print("Illia Basalukk, IT-31")

wallet = Wallet("Illia Basalukk", 6000)
print(f"Власник: {wallet.owner}")
print(f"Баланс: {wallet.balance:.2f} UAH")

try:
    wallet2 = Wallet("", 1000)
except ValueError as error:
    print("Помилка створення гаманця:", error)

try:
    wallet3 = Wallet("Illia Basalukk", -500)
except ValueError as error:
    print("Помилка створення гаманця:", error)
