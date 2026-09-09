# Input Validation and Output Verification 
**Activity:** PSHS Workshop Registration Validator 
**Name:** Yuan Marcus L. Mesia
**Section:** 8 - Dahlia
**Quarter:** 1 
--- 
## Activity Overview 
In this activity, I created a program that validates information entered into a PSHS workshop registration system. 
The program checks whether user input satisfies specific requirements before accepting the registration. The program validates: 
- student name 
- age 
- grade level 
- email address and 
- registration code.
--- 
# Part A - Validation Requirements 

| Data Captured | Expected Input | Validation Type | Invalid Input Example | Validation Rule | Error Message | 
|---|---|---|---|---|---| 
| Student Name | String/Text | Presence Validator | (blank) | Must not be blank. | Student name is required | 
| Age | Integer (11 to 18) | Data type & Range validation | 25 |  Must be a valid integer. |Age must be between 11 and 18.| 
| Grade Level | Integer (7 to 12) | Acceptable value validation | 13  | Must be one of 7, 8, 9, 10, 11, 12 | Grade level must be between 7 and 12. | 
| Email Address | String/Text | Simple pattern validation | ymlmesia@brcpshseduph | Must contain the characters "@" and ".". | Invalid email address. Please enter a valid email address.| 
| Registration Code | String/Text (6 characters) | Length validation | 12ag111 OR ABC1234 | Must be exactly 6 characters.| Invalid registration code. The registration code must contain exactly 6 characters. | 
--- 
## Validation Questions 
### 1. Why should the student name not be blank? 
> A blank name check ensures the every registered person can be identified.
### 2. Why should age be checked for both data type and range? 
> Checking data type prevents the program from crashing when non-numeric text is entered. Checking range ensures that only students ages 11 to 18 are valid/accepted.
### 3. Why should grade level only accept specific values? 
> The workshop is specifically designed for high school grade levels (7-12).
### 4. What format requirements did you use for the email address? 
> The simpler pattern requirement ensures that the provided string contains both of these characters: "@", and ".".
### 5. What length requirement did you use for the registration code? 
> The registration code must be exactly 6 characters long.
--- 
# Part B - Program Design 
## Pseudocode
```text 
START 
 Input name
  if name is blank, print "student name is required" and end the program
 Input age
  if age is less than 11 or more than 18, print "You are not eligible to register for the workshop." then end the program.
 Input grade level
  if grade level is less than 7 or more than 12, print "You are not eligible to register for the workshop. Grade level must be between 7 and 12." then end the program.
 Input email
  if email does not contain "@" or ".", print "Invalid email address. Please enter a valid email address." then end the program.
 Input registration code
  if registration code does not contain or exceeds 6 characters, print "Invalid registration code. The registration code must contain 6 characters." then end the program.
 Print "Registration Successful!"
  print name, age, grade level. email, and registration code.
END 

Your design should show: 
- user input 
- validation decisions 
- error messages 
- accepted registration 
- rejected registration. 
--- 
# Part C - Program Implementation 
## Programming Language 
> Write the programming language used. 
## Source Code File 
[`workshop_validator.py`](workshop_validator.py) 
## Final Code 
```python 
# Paste your final code here.
#PSHS Workshop Registration Validator IMPROVED

#COLLECT INPUTS
name = input("Enter your name: ")
age_input = (input("Enter your age: "))
grade_level = input("Enter your grade level: ")
email_address = input("Enter your email address: ")
registration_code = input("Enter your registration code: ")

is_valid = True
error_message_name = ""
error_message_age = ""
error_message_grade_level = ""
error_message_email = ""
error_message_registration_code = ""

#VALIDATE NAME
if name == "":
    is_valid = False
    error_message_name = "Student name is required."

#VALIDATE AGE
if not age_input.isdigit():
    is_valid = False
    error_message_age = "Age must be a number."
else:
    age = int(age_input)
    if age < 11 or age > 18:
        is_valid = False
        error_message_age = "Age must be between 11 and 18."

#VALIDATE GRADE LEVEL
elif int(grade_level) < 7 or int(grade_level) > 12:
    is_valid = False
    error_message_grade_level = "Grade level must be between 7 and 12."

#VALIDATE EMAIL ADDRESS
if email_address is None or "@" not in email_address or "." not in email_address:
    is_valid = False
    error_message_email = "Invalid email address. Please enter a valid email address."

#VALIDATE REGISTRATION CODE
if len(registration_code) != 6:
    is_valid = False
    error_message_registration_code = "Invalid registration code. The registration code must contain exactly 6 characters."

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

``` 
--- 
## Validation Techniques Used 
### Presence Validation 
Explain where you used presence validation. 
> I used presence validation on 'name' to ensure ii wasn't left blank.
### Data Type Validation 
Explain where you used data type validation. 
> I used data type validation on 'age' to check if the entered string consists of only numeric digits.
### Range Validation 
Explain where you used range validation. 
> I used range validation on 'age' to verify that the student's age fell within the specified range of 11 and 18.
### Acceptable Value Validation 
Explain where you used acceptable value validation. 
> I used acceptable value validation on 'grade level' to ensure that the program only accepts the valid high school grade levels between 7 and 12.
### Pattern Validation 
Explain the simple pattern rule you used. 
> I used simple patter check on 'email address' to verify if "@" and "." is in the input, ensuring the entered email contains the needed formatting characters.
### Length Validation 
Explain the length rule you used. 
> I used length validation on 'registration code' to guarantee the code has exactly 6 characters.
--- 
# Part D - Testing 

| Test | Input / Condition | Validation Being Tested | Expected Output | Actual Output | Result | |---:|---|---|---|---|---| 
| 1 | All inputs valid | Normal case | 
   Registration Successful!

Name: YUAN MARCUS L. MESIA
Age: 13
Grade Level: 8
Email Address: ymlmesia@brc.pshs.edu.ph
Registration Code: 123456 | 
   Registration Successful!

Name: YUAN MARCUS L. MESIA
Age: 13
Grade Level: 8
Email Address: ymlmesia@brc.pshs.edu.ph
Registration Code: 123456| PASS | 
| 2 | Blank student name | Presence | | | | 
| 3 | Age = `fourteen` | Data type | | | | 
| 4 | Age = `11` | Minimum boundary | | | | 
| 5 | Age = `18` | Maximum boundary | | | | 
| 6 | Age = `10` | Range | | | | 
| 7 | Grade Level = `13` | Acceptable value | | | | 
| 8 | Email = `studentpshs.edu.ph` | Pattern | | | | 
| 9 | Registration Code = `ABC` | Length | | | | 
| 10 | Registration Code = `CS2026` | Valid length | | | | 
Write **PASS** when the actual output matches the expected output. 
Write **FAIL** when it does not. 
--- 
# Part E - Output Verification 

## Verification Test 1 
**Input:** 
```text 
Write the input here.
``` 
**Expected Output:** 
```text 
Write the expected output here. 
``` 
**Actual Output:** 
```text 
Write the actual output here. 
``` 
**Result:** PASS / FAIL 
**Explanation:** 
--- 
## Verification Test 2 
**Input:** 
```text 
Write the input here. 
``` 
**Expected Output:** 
```text 
Write the expected output here. 
``` 
**Actual Output:** 
```text 
Write the actual output here. 
``` 
**Result:** PASS / FAIL 
**Explanation:** 
--- 
## Verification Test 3 
**Input:** 
```text 
Write the input here. 
``` 
**Expected Output:** 
```text 
Write the expected output here. 
``` 
**Actual Output:**
```text 
Write the actual output here. 
``` 
**Result:** PASS / FAIL 
**Explanation:** 
--- 
# Reflection 
Answer briefly. 
### 1. Why should a program validate input before processing it? > Write your answer here. 
### 2. What is the difference between input validation and output verification? > Write your answer here. 
### 3. Which validation technique was easiest for you to implement? Why? > Write your answer here. 
### 4. Which validation technique was most challenging? Why? > Write your answer here. 
### 5. How did testing invalid inputs help you improve your program? > Write your answer here. 
--- 
# Files for This Activity 
- [`workshop_validator.py`](workshop_validator.py) 
- `input_validation.md` 
- `workshop_validator_flowchart.png` if a flowchart was used --- 
[← Back to Main Portfolio](../README.md) 


