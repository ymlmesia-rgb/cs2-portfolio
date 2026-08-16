import math

x1 = float(input("Enter the first number: "))
x2 = float(input("Enter the second number: "))
y1 = float(input("Enter the third number: "))
y2 = float(input("Enter the fourth number: "))

diff_xs = math.pow(x2 - x1, 2)
diff_ys = math.pow(y2 - y1, 2)
distance = math.sqrt(diff_xs + diff_ys)
print("The distance between the two points is:", round(distance, 2))

#REFLECTION
#The Python math library simplified this activity by translating the distance formula directly into readable code.
#Using built-in functions saves time and avoids mistakes from writing math manually. 

