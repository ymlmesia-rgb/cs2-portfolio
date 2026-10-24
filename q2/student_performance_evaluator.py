#Student Performance Evaluator

def calculate_average(score1, score2, score3):
    return (score1 + score2 + score3) / 3

def get_performance(average):
    if average >= 85:
        return "Mastery"
    if average < 85 and average >= 70:
        return "Developing"
    if average < 70:
        return "Needs Review"

def is_eligible(average, completed_tasks):
    if average >= 85 and completed_tasks >= 3:
        return True
    else:
        return False

score1 = float(input("Enter score 1 (between 1 and 100): "))
if score1 < 1 or score1 > 100:
        print("Invalid score. Please enter a score between 1 and 100.")
        exit()
score2 = float(input("Enter score 2 (between 1 and 100): "))
if score2 < 1 or score2 > 100:
        print("Invalid score. Please enter a score between 1 and 100.")
        exit()
score3 = float(input("Enter score 3 (between 1 and 100): "))
if score3 < 1 or score3 > 100:
        print("Invalid score. Please enter a score between 1 and 100.")
        exit()

completed_tasks = int(input("Enter the number of completed tasks: "))
average_score = calculate_average(score1, score2, score3)

print("Your average score is: ", average_score)
print("Your performance level is: ",get_performance(average_score))
print("Eligibility:", is_eligible(average_score, completed_tasks))
