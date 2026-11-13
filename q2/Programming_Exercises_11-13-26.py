#Programming Exercises 
#11-13-26
#sir roffe you can just copy nalang po individually yung each exercise and wag po itong buong file kazi po magulo po, thx po sir

#Exercise 1: Count Even Numbers
#Using a for loop, display all even numbers from 2 to 20.
#Hint: Use range() with a step of 2

#idk if the number 20 is supposed to be part of the even numbers from 2 to 20 because the range function does not include the last number in the range. so if i wanted to include 20 i would have to change the range to go up to 21 just so that 20 is inculded in the range.

#20 is not included
for n in range(2, 20, 2):
    print(n)

#okay so n is the name of the variable that is being used to iterate through the range of numbers. the range function starts at 2 and goes up to 20, with a step of 2. which means that it will only include even numbers in the range. the for loop will print each even number in the range. then n will be printed

#Exercise 2: The Countdown Timer
#Create a program that displays numbers from 10 down to 1. After the countdown, display "Time is up!" 
#Hint: Use a while loop

countdown = 10
while countdown > 0:
    print(countdown)
    countdown -= 1
print("Time is up!")

#okay so i set a variable "countdown" to 10 then i made a while loop that will keep going as long as countdown is larger than 0. then inside the while loop i printed the value of countdown and then subtracted 1 from countdown. (sir i did study what -= does) when countdown is not larger than 0 anymore the while loop will stop and after that "Time is up!" will be printed.

#Exercise 3: Skip Multiples
#Display numbers from 1 to 15, but skip every multiple of 3.
#Hint: Use the modulo (%) operator and continue

for n in range(1, 15):
    if n % 3 == 0:
        continue
    print(n)

#okay so i used n again as the name for the variable that is being used to iterate through the range of numbers. the range function starts at 1 and ends at 15. i made a for loop then i made an if statement that checks if n is a multiple of 3 by checking if the remainder of n/3 equals 0. if n/3 equals 0, then i will use continue statement to skip and move on. if n is not a multiple of 3, then it will be printed.

#Exercise 4. Multiplication Table Generator
#Create a function show_table(number) that prints the multiplication table of the given number from 1 to 10. Ask for a number, pass it as an argument, and call the function.
#Hint: Inside the function, use for i in range(1, 11). Multiply number by i

number = int(input("Enter a number:"))

def show_table(number):
    for i in range(1, 11):
        print(number * i)

show_table(number)

#okay so i asked for an input from the user to first define the parameter that will be passed to the function (sequential :D ). then i defined the function show_table with the parameter number. inside the function i made a for loop that iterates through the range of numbers from 1 to 10. then i printed the product of number and i. after defining the function, i called it and passed the argument number to it.
