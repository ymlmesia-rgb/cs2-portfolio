#The Canteen Purchase Calculator

def calculate_total(price, quantity):
    return price * quantity

def calculate_change(payment, total):
    return payment - total
   
    
price = float(input("Enter the price of the item: "))
quantity = int(input("Enter the quantity of the item: "))
payment = float(input("Enter the payment amount: "))
total_cost = calculate_total(price, quantity)

print("Total cost: ", total_cost)
print("Change: ", calculate_change(payment, total_cost))

if calculate_change(payment, total_cost) < 0:
    print("Insufficient payment. Please provide enough funds.")

