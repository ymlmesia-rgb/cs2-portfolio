#PSHS Secure Club Registration System

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
print(f"Attendance Status: {attendance}")
