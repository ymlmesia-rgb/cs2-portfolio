destinations = ["Cebu", "Manila", "Davao", "Baguio", "Palawan"]

for i in (destinations[1:4]):
  print(i)

search_destination = input("Enter a destination to search for: ")

if search_destination in destinations:
  print("Valid destination.")
  
else:
  print("Destination not in the list of detinations.")
  search_destination = input("Enter a destination to search for: ")

destinations[2] = "Ilo-Ilo"
print("New list:")
for i in list(destinations):
  print(i)
