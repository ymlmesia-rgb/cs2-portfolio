#The Canteen Purchase Calculator

price = float(input("Enter the price of the item: "))
quantity = int(input("Enter the quantity of the item: "))
payment = float(input("Enter the payment amount: "))


def calculate_total(price, quantity):
    return price * quantity

def calculate_change(payment, total):
    return payment - total

print("Total cost: ", calculate_total(price, quantity))
print("Change: ", calculate_change(payment, calculate_total(price, quantity)))

if calculate_change(payment, calculate_total(price, quantity)) < 0:
    print("Insufficient payment. Please provide enough funds.")
