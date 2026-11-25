class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def describe(self):
        return f"{self.name} {self.surname}"


class Student(Person):
    def __init__(self, name, surname, group):
        super().__init__(name, surname)
        self.group = group

    def describe(self):
        return f"{super().describe()}, {self.group}"


class GroupLeader(Student):
    def __init__(self, name, surname, group, phone):
        super().__init__(name, surname, group)
        self.phone = phone

    def describe(self):
        return f"{super().describe()}, group leader, {self.phone}"


print("Illia Basalukk, IT-31")

student = Student("Illia", "Basalukk", "IT-31")
leader = GroupLeader("Andrii", "Hordii", "IT-31", "+380933237161")

classes = [Person, Student, GroupLeader]

print("\n1. Перевірка isinstance():")
print(f"{'Тип':<15}", end="")
for cls in classes:
    print(f"{cls.__name__:<15}", end="")
print()

for obj in [student, leader]:
    print(f"{type(obj).__name__:<15}", end="")
    for cls in classes:
        print(f"{str(isinstance(obj, cls)):<15}", end="")
    print()

print("\n2. Перевірка issubclass():")
print(f"{'Клас':<15}", end="")
for cls in classes:
    print(f"{cls.__name__:<15}", end="")
print()

for child in classes:
    print(f"{child.__name__:<15}", end="")
    for parent in classes:
        print(f"{str(issubclass(child, parent)):<15}", end="")
    print()

print("\n3. Порядок пошуку методів GroupLeader:")
for cls in GroupLeader.__mro__:
    print(cls.__name__)

print("\nОпис старости:")
print(leader.describe())
