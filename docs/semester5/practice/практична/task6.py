# Task 6, Basalyk, IT-31

name = input("Enter your name: ")
age = int(input("Enter your age: "))

is_in_age_range = 18 <= age <= 60
is_even_age = age % 2 == 0
both_conditions = is_in_age_range and is_even_age
at_least_one_condition = is_in_age_range or is_even_age
years_to_60 = 60 - age

print(f"{name}, age {age} is between 18 and 60: {is_in_age_range}")
print(f"{name}, age {age} is even: {is_even_age}")
print(f"Both conditions are true: {both_conditions}")
print(f"At least one condition is true: {at_least_one_condition}")
print(f"Years until 60: {years_to_60}")