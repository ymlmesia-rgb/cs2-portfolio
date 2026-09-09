#PSHS Workshop Registration Validator IMPROVED

#COLLECT INPUTS
name = input("Enter your name: ")
age = input("Enter your age: ")
grade_level = input("Enter your grade level: ")
email_address = input("Enter your email address: ")
registration_code = input("Enter your registration code: ")

is_valid = True
error_message = ""

#VALIDATE NAME
if not name:
    is_valid = False
    error_message_name = "Student name is required."

#VALIDATE AGE
if age == "":
    is_valid = False
    error_message_age = "Age is required."

#VALIDATE GRADE LEVEL
if grade_level == "":
    is_valid = False
    error_message_grade_level = "Grade level is required."
elif int(grade_level) < 7 or int(grade_level) > 12:
    is_valid = False
    error_message_grade_level = "Grade level must be between 7 and 12."

#VALIDATE EMAIL ADDRESS
if email_address is None or "@" not in email_address or "." not in email_address:
    is_valid = False
    error_message_email = "Invalid email address. Please enter a valid email address."

#VALIDATE REGISTRATION CODE
if len(registration_code) > 6:
    is_valid = False
    error_message_registration_code = "Invalid registration code. The registration code must not exceed 6 characters."
if len(registration_code) < 6:
    error_message_registration_code = "Invalid registration code. The registration code must not be less than 6 characters."

#VALIDATION RESULT
if is_valid:
    print("-" * 30)
    print("   Registration Successful!")
    print("-" * 30)
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Grade Level: {grade_level}")
    print(f"Email Address: {email_address}")
    print(f"Registration Code: {registration_code}")
else:
    print("-" * 30)
    print("   Registration Failed!")
    print("-" * 30)
    print("The following errors were found:")
    print(f"- {error_message_name}")
    print(f"- {error_message_age}")
    print(f"- {error_message_grade_level}")
    print(f"- {error_message_email}")
    print(f"- {error_message_registration_code}")
