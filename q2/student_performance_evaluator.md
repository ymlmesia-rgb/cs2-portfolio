# Documentation Questions

### 1. Which function returns a number, which returns a string, and which returns a boolean?
> The function ***calculate_average(score1, score2, score3)*** returns a number, the function ***get_performance(average)*** returns a string, and the function ***is_eligible(average, completed_stasks)*** returns a boolean.
### 2. What is the difference between the parameters price and quantity and the actual arguments passed
to the function?
> Parameters are the placeholder variable defined in the function header.
> Arguments are the actual value or variable passed into the function when you call it.

### 3. Where is the returned total stored, and how is it reused?
> The returned total is stored in the *total_cost* variable.
> It is reused in three places:
> 1. When printing the total cost (print("Total cost: ", total_cost)).
> 2. As an argument passed into calculate_change(payment, total_cost) inside the print statement.
> 3. As an argument passed into calculate_change(payment, total_cost) inside the if condition to check for insufficient funds.

### 4. Why is it useful to separate total calculation from change calculation?
> Separating the two calculations makes the program much easier to maintain and update.
