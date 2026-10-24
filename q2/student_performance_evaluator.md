# Documentation Questions

### 1. Which function returns a number, which returns a string, and which returns a boolean?
> The function ***calculate_average(score1, score2, score3)*** returns a number, the function ***get_performance(average)*** returns a string, and the function ***is_eligible(average, completed_stasks)*** returns a boolean.
### 2. Explain how the average moves from ***calculate_average*** into ***get_performance***.
When the user enters their three scores those three scores are sent as arguments into the function ***calculate_average(score1, score2, score3)***. This function does the math. Gives the result back using the return statement. In the part of the program the value that comes back is saved into a variable named average_score. Then this average_score is sent as an argument into the function ***get_performance(average)***. This function looks at the number and finds out which performance category it belongs to.
### 3. What happens when a student has a high average but has completed fewer than 3 tasks?
The ***is_eligible(average, completed_tasks)*** function will evaluate the condition as false because both conditions must be met. They (the student) will not be eligible.
### 4. Why is return more appropriate than simply printing the result inside each function?
Using return makes your functions reusable. You would also be allowed to pass data in a variable into other functions (like explained in item 2).
