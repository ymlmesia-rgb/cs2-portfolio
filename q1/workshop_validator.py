#PSHS Workshop Registration Validator

import string
import sys

name = input("Enter your name: ")
if name == "":
    print("REGISTRATION NOT ACCEPTED") 
    print("Student name is required.")
    sys.exit() 

age = int(input("Enter your age: "))
if age < 11 or age > 18:
    print("REGISTRATION NOT ACCEPTED") 
    print("You are not eligible to register for the workshop. Age must be between 11 and 18.")
    sys.exit()
    

grade_level = int(input("Enter your grade level (7-12): "))
if grade_level < 7 or grade_level > 12:
    print("REGISTRATION NOT ACCEPTED")
    print("You are not eligible to register for the workshop. Grade level must be between 7 and 12.")
    sys.exit()

email = input("Enter your email address: ")
if "@" not in email or "." not in email:
    print("REGISTRATION NOT ACCEPTED")
    print("Invalid email address. Please enter a valid email address.")
    sys.exit()

registration_code = input("Enter your registration code: ")
if len(registration_code) != 6:
    print("REGISTRATION NOT ACCEPTED")
"Invalid registration code. The registration code must contain 6 characters."    print()
    sys.exit()

print("-" * 30)
print("   Registration Successful!")
print("-" * 30)
print (f"Name: {name}")
print (f"Age: {age}")   
print (f"Grade Level: {grade_level}")
print (f"Email: {email}")
print (f"Registration Code: {registration_code}")
