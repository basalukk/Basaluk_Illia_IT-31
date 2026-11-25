# Task 5, Basalyk, IT-31

birth_day = 11
birth_month = 7

is_positive = birth_day > 0
is_even = birth_day % 2 == 0
is_positive_and_even = is_positive and is_even

print(f"Number {birth_day} is positive: {is_positive}")
print(f"Number {birth_day} is even: {is_even}")
print(f"Number {birth_day} is positive and even: {is_positive_and_even}")

second_number = birth_day * birth_month

second_is_positive = second_number > 0
second_is_even = second_number % 2 == 0
second_is_positive_and_even = second_is_positive and second_is_even

print(f"Number {second_number} is positive: {second_is_positive}")
print(f"Number {second_number} is even: {second_is_even}")
print(f"Number {second_number} is positive and even: {second_is_positive_and_even}")