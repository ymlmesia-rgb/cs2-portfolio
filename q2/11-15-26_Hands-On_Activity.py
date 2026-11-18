#Programming-activity 1
secret_number = 7
guess = int(input("Guess the number: "))
attempts = 1

while guess != secret_number:
  attempts = attempts + 1
  print("Incorrect! Try again.")
  guess = int(input("Guess the number: "))

if attempts == 1:
  print("Correct! It took you 1 attempt!")
else:
  print("Correct! It took you", attempts,"attempts!" )
  
#Programming-activity 2
word = input("Enter the word: ")
while word != "YES":
  print("Word is incorrect. Please try again.")
  word = input("Enter the word: ")
print("The word is correct!")

#Programming-activity 3
for a in range(3, 31, 3):
  print(a,end=" ")
  
#Programming-activity 4
message = input("Enter a motivational message: ")
no_of_times = int(input("Enter how many times it should be displayed: "))

while no_of_times < 1:
  print("Enter a positive whole-number.")
  no_of_times = int(input("Enter how many times it should be displayed: "))

for a in range(no_of_times):
  print(message)
