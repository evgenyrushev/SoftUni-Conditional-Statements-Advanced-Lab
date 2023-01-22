age = float(input())
gender = input()

if age < 16:
    if gender == "m":
        print("Master")
    else:
        print("Miss")
elif age >= 16:
    if gender == "m":
        print("Mr.")
    else:
        print("Ms.")
