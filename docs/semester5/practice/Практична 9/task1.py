full_name = "  bASALUKK   iLLIA   pAVLOVYCH  "

words = full_name.split()
full_name = " ".join(words).title()

print("Full name:", full_name)
print("Length:", len(full_name))

surname, name, patronymic = full_name.split()

print("First surname letter:", surname[0])
print("Last surname letter:", surname[-1])
print("Surname reversed:", surname[::-1])

print("Short name:", f"{surname} {name[0]}. {patronymic[0]}.")
print("Initials:", f"{surname[0]}{name[0]}{patronymic[0]}")

vowels = "aeiou"
vowel_count = sum(1 for char in full_name.lower() if char in vowels)

print("Vowels:", vowel_count)

group = "IT-31"

dash_position = group.find("-")
before_dash = group[:dash_position]
after_dash = group[dash_position + 1:]

print("Before dash:", before_dash)
print("After dash:", after_dash)
print("After dash is number:", after_dash.isdigit())

login = f"{name[0].lower()}.{surname.lower()}"
email = f"{login}@student.edu.ua"

print("Login:", login)
print("Email:", email)