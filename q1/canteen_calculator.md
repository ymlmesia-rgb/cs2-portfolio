# Documentation Questions

### 1. What does each function do?
> The function *calculate_total(price, quantity)* Takes the price and quantity parameters, multiplies them together, and returns the total cost of the purchase. The second function *calculate_change(payment, total)* takes the payment and total parameters, subtracts the total from the payment, and returns the resulting change.

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
