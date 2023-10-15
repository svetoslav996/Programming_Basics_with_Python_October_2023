age = float(input())
gender = input()

# first variant

# if age >= 16 and gender == "m":
#     print("Mr.")
# elif age < 16 and gender == "m":
#     print("Master")
# elif age >= 16 and gender == "f":
#     print("Ms.")
# elif age < 16 and gender == "f":
#     print("Miss")
# else:
#     print("unknown")

# second variant

if gender == "m":
    if age >= 16:
        print("Mr.")
    else:
        print("Master")
if gender == "f":
    if age >= 16:
        print("Ms.")
    else:
        print("Miss")