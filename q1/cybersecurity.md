# Fundamentals of Cybersecurity and Data Privacy 
**Activity:** PSHS Secure Club Registration System 
**Name:** Yuan Marcus L. Mesia
**Section:** Dahlia
**Quarter:** 1 
--- 
## Activity Overview 
In this activity, I analyzed a cybersecurity threat and developed secure data-capture rules for a simple PSHS Club Registration System. 
The goal is to create a program that collects only necessary information and accepts only correct, expected, and appropriate input. 
--- 
# Part A - Cybersecurity Threat Analysis 
## Assigned Case
**Case Number:** Case 1
**Case Title:** Fake Login Alert  
> It is a message that claims the the student's account will be disabled and asks them to click a link anf enter their username and password.
--- 
### 1. What cybersecurity threat is shown? 
> A phishing attack. It uses social engineering to fool people into revealing their authentication information.
### 2. What warning signs make the situation suspicious? 
> Number one, threatening to immediately delete account. This causes a sense of urgency and fear. Number two, asking for passwords in a direct link. This is an unusual request. And number three, directing users to enter sensitive information on an external site. (Unverified links)
### 3. What may be affected? 
Check or describe all that apply: 
[x] Data 
[x] Account 
- Application 
- Device 
- Network 
- Financial information 
> The attacker gets your login credentials, giving them full access to the account and all sensitive information attached to it.
### 4. What information could be exposed or misused? 
> School email contents, academic files, contact details, school systems/portals
### 5. What should the user do to reduce the risk? 
> Do not click the link or enter sensitive information.
> Report the sus message to a teacher. (sir Roffe)
--- 
# Part B - Data Privacy and Secure Data Capture 
| Data | Collect / Do Not Collect | Reason | 
|---|---|---| 
| Student Name | Collect | Needed to identify the registrant. | 
| Section | Collect | Needed for proper categorization. | 
| Club Choice | Collect | Needed for club placement.  | 
| School Email | Collect | Needed for official school communication. | 
| Attendance Status | Collect | Needed to track participation. | 
| Password | Do not collect | Unnecessary for club registration. | 
| OTP | Do not collect | Not needed for simple form submissions. | 
| Home Address | Do not collect | Personal information (like this) is not required for club activities. |
| Parent Bank Account | Do not collect | Unrelated to club sign-ups. | 
--- 
## Privacy Question 
Why is it safer to collect only information that the program actually needs? 
> It is safer because it limits potential danger/damage. If a system goes through a data breach, uncollected data cannot be stolen, leaked, or misused.
--- 
# Part C - Security-Focused Validation Rules 
| Data Captured | Expected Input | Possible Risk | Invalid Input Example | Validation Rule | Error Message | 
|---|---|---|---|---|---| 
| Student Name | String that is not empty. | Missing identity. |""| Name must not be blank. | Name cannot be empty. Please enter your name. | 
| Section | Grade 8 section with proper capitalization. |Invalid section or typos.| rosal | Must match correct section list. | Invalid Section. Please try again. | 
| Club Choice | Robotics, Science, Mathematics, Programming | Unapproved clubs or improper data  | robotics club, Gamin Club | Literal (advanced way of saying value😎) must exist in the options list. | Invalid club choice. Please enter a valid club name. | 
| School Email | Valid email containing "@" and "." | Wrong email address. | ymlmesia@brcpshsedu, ymlmesia.brc.pshs.edu | Must contain "@" and "." | Invalid school email address. Please try again. | 
| Attendance Status | Present, Absent, Late | Invlaid status literal(😎) | Excused | Must match one of three statuses. | Invalid attendance status. Please enter 'Present', 'Absent', or 'Late'. | 
--- 
## Secure Data Capture Questions 
### 1. What should your program accept? 
> Inputs that are complete, properly formatted, and match the options. 
### 2. What should your program reject? 
> Blank inputs, unknown?/unrecognized options, improperly formatted email addresses, and unsafe requests for sensitive information/data.
### 3. How do your validation rules help reduce incorrect or unsafe input? 
> They ensure consistency of data, prevent submissions that are incomplete, and rejects unexpected inputs before processing.
--- 
# Part D - Secure Program Implementation 
## Program 
Create a simple **PSHS Club Registration System**. 
The program should collect only: 
- Student Name 
- Section 
- Club Choice 
- School Email
- Attendance Status 
It should **not request passwords, OTPs, banking information, or unnecessary personal information**. 
--- 
## Source Code File 
[`secure_registration.py`](secure_registration.py) 
--- 
## Final Code 
```python 
# #PSHS Secure Club Registration System

#Collect Name Input

while True:
    name = input("Enter your name: ")
    if name == "":
        print("Name cannot be empty. Please enter your name.")
    else:
        break
print ("                                                    ")

#Collect Section Input

while True:
    section = input("Enter your section. Observe proper capitalization. Ex: Sampaguita, Dahlia, Rosal, Ilang-Ilang: ")
    if section not in ["Dahlia", "Sampaguita", "Rosal", "Ilang-Ilang"]:
        print("Invalid Section. Please try again.")
    else:
        break
print ("                                                    ")

#Collect Club Choice Input

while True:
    print("Available Clubs:")
    clubs = ["Robotics Club", "Science Club", "Mathematics Club", "Programming Club"]
    for index, club in enumerate(clubs, start=1):
        print(f"{index}. {club}")

    club_choice = input("Enter the name of your desired club with the first letter of ALL words capitalized: ")
    if club_choice not in clubs:
        print("                                                    ")
        print("Invalid club choice. Please enter a valid club name.")
        print("                                                    "                          )
    else:
        break
print ("                                                    ")

#Collect School Email Input

while True:
    school_email = input("Enter your school email address: ")
    if "@" not in school_email or "." not in school_email:
        print("Invalid school email address. Please try again.")
    else:
        break
print ("                                                    ")

#Collect Attendance Status\

attendance_status = ["Present", "Absent", "Late"]
attendance = input("Enter your attendance status (Present, Absent, Late): ")
if attendance not in attendance_status:
    print("Invalid attendance status. Please enter 'Present', 'Absent', or 'Late'.")
    print("                                               ")

#Final Output

print("-" * 30)
print("   Registration accepted!")
print("-" * 30)
print(f"Name: {name}")
print(f"Section: {section}")
print(f"Club Choice: {club_choice}")
print(f"School Email: {school_email}")
print(f"Attendance Status: {attendance}"). 
``` 
--- 
## Security Practices Applied 
### Required Input 
> Check if strings are empty/blank by using (if name == "":).
### Allowed Values 
> Used lists for Section, Club Choice, and Attendance Status.
### Format Check 
> Verifies if the email address entered contained the required characters "@" and ".". 
### Error Messages 
> Provides specific feedback to tell users what went wrong.
### Data Minimization 
> Excludes collection of inputs for passwords, OTPs, home addresses, and bank accounts to prevent collecting personal data that is not needed.
--- 
# Part E - Testing and Reflection 
## Testing 
| Test | Input Situation | Expected Output | Actual Output | Result | 
|---:|---|---|---|---| 
| 1 | All data valid | REGISTRATION ACCEPTED | REGISTRATION ACCEPTED | PASS | 
| 2 | Blank student name | Name cannot be empty. Please enter your name. | Name cannot be empty. Please enter your name. | PASS | 
| 3 | Invalid section | Invalid Section. Please try again. | Invalid Section. Please try again. | PASS |
| 4 | Invalid club choice | Invalid club choice. Please enter a valid club name. | Invalid club choice. Please enter a valid club name. | PASS | 
| 5 | Email missing `@` | Invalid school email address. Please try again. | Invalid school email address. Please try again. | PASS | 
| 6 | Email missing `.` |Invalid school email address. Please try again. | Invalid school email address. Please try again. | PASS | 
| 7 | Invalid attendance status | Invalid attendance status. Please enter 'Present', 'Absent', or 'Late'. | Invalid attendance status. Please enter 'Present', 'Absent', or 'Late'. | PASS | 
| 8 | Different valid inputs | REGISTRATION ACCEPTED | REGISTRATION ACCEPTED | PASS | 

--- 
# Reflection 
### 1. What is one cybersecurity threat that can affect an application or user?
> Phishing attacks. Malicious people impersonate real authorities to steal sensitive credentials. 
### 2. How can users reduce the risk of phishing or suspicious messages? 
> Checking sender addresses, avoiding links in urgent messages, turning on multi-factor authentication. 
### 3. How can validation rules improve the security of user input? 
> They enforce limitations/rules on entered data and ensuring safe, expected, and correct inputs.
### 4. Why should a program avoid collecting unnecessary personal information? 
> In order to minimize data, reducing impacts in a security breach.
### 5. How did SG7's input validation concepts become security practices in SG8? 
> SG7 focused on preventing errors through basic input checks. SG8 builds upon those checks into deliberate security checks.
--- 
# Files for This Activity 
- [`secure_registration.py`](secure_registration.py) 
- `cybersecurity.md` 
--- 
[← Back to Main Portfolio](../README.md)
