class Student:
    college = "FKTBP VNU"
    count = 0

    def __init__(self, name, surname, group, birth_year):
        self.name = name
        self.surname = surname
        self.group = group
        self.birth_year = birth_year
        Student.count += 1

    def full_name(self):
        return f"{self.name} {self.surname}"


student1 = Student("Illia", "Basalukk", "IT-31", 2009)
student2 = Student("Andrii", "Shevchenko", "IT-31", 2008)

print("College through class:", Student.college)
print("College through student1:", student1.college)
print("College through student2:", student2.college)

student1.college = "My New College"

print("\nAfter changing college in student1:")
print("student1.college:", student1.college)
print("student2.college:", student2.college)
print("Student.college:", Student.college)

print("\nCreated students:", Student.count)

print("\nstudent1.__dict__:")
print(student1.__dict__)

print("\nStudent.__dict__:")
print(Student.__dict__)
