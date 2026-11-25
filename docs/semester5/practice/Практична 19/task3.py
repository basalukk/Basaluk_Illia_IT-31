class Wallet:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    @property
    def owner(self):
        return self.__owner

    @owner.setter
    def owner(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Ім'я власника не може бути порожнім")
        self.__owner = value.strip()

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError("balance can not be negative")
        self.__balance = round(value, 2)

    @property
    def is_empty(self):
        return self.__balance == 0


print("Illia Basalukk, IT-31")

wallet = Wallet("Illia Basalukk", 1500)
print("Початковий баланс:", wallet.balance)

wallet.balance = 1200.555
print("Після зміни:", wallet.balance)

print("Власник:", wallet.owner)
print("Гаманець порожній:", wallet.is_empty)

try:
    wallet.balance = -100
except ValueError as error:
    print("Помилка балансу:", error)

try:
    wallet.owner = ""
except ValueError as error:
    print("Помилка власника:", error)

try:
    wallet.is_empty = True
except AttributeError as error:
    print("Помилка зміни is_empty:", error)
