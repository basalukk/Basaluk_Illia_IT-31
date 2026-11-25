# Task 4, Basalyk, IT-31

a = 11
b = 7

last_name = "Basalyk"
c = len(last_name)

first_result = a > b
second_result = b < a
third_result = a == b

fourth_result = a < b
fifth_result = b > a
sixth_result = a != b

print(f"a > b = {first_result}, type = {type(first_result)}")
print(f"b < a = {second_result}, type = {type(second_result)}")
print(f"a == b = {third_result}, type = {type(third_result)}")
print(f"a < b = {fourth_result}, type = {type(fourth_result)}")
print(f"b > a = {fifth_result}, type = {type(fifth_result)}")
print(f"a != b = {sixth_result}, type = {type(sixth_result)}")
range_result = b <= c <= a
print(f"b <= c <= a = {range_result}, type = {type(range_result)}")