price_per_page = 3
pages = int(input("Enter the number of pages: "))
payment = float(input("Enter the payment amount: "))

def calculate_printing_cost(pages, price_per_page):
    return pages * price_per_page
  
total_cost = calculate_printing_cost(pages, price_per_page)

def calculate_balance(payment, total_cost):
    return payment - total_cost

payment_shortage = total_cost - payment

print("Total cost: ", calculate_printing_cost(pages, price_per_page))
if calculate_balance(payment, total_cost) >= 0:
  print("Change: ", calculate_balance(payment, total_cost))
else:
  print("Insufficient payment. Please provide enough funds. The payment shortage is: ",payment_shortage)
  
