

print("=== Personal Profile Generator ===")

name = input("Enter your full name: ")
age = int(input("Enter your age:"))
height = float(input("Enter your height in meters:"))
favorite_number = int(input("Enter your favorite number: "))
currentYear = 2026
birthYear = int(input("Enter your birth year: "))
age = currentYear - birthYear
height = float(input("Enter your height in meters: "))
height_m = height / 100
print("Your height in meters is:", height_m)
favorite_number = int(input("Enter your favorite number: "))
squared = favorite_number ** 2
print("Your favorite number is:", favorite_number)
print("Its square is:", squared)
'''
print("\n" + "=" * 40)
print("           PERSONAL PROFILE")
print("=" * 40)
print(f"Name               : {name}")
print(f"Age                : {age}")
print(f"Height (meters)    : {height: 2f}")
print(f"Favorite Number    : {favorite_number}")
print(f"Age                : {age}")
print("=" * 40)
'''