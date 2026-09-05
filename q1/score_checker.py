# PSHS_Student_Score_Checker

# Prompt user to enter the score

score = int(input("Enter the score (0-100):  "))

# Validate the score and determine the grade

if score < 0 or score > 100:
    print("Invalid score. Please enter a score between 0 and 100.")
else:
    if score >= 90:
        grade = "Outstanding"
    elif score >= 80:
        grade = "Very Satisfactory"
    elif score >= 75:
        grade = "Satisfactory"
    else:
        grade = "Needs Improvement"

# Output score and grade

    print(f"The grade for the score {score} is {grade}.")
