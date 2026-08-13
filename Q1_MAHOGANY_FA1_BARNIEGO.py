import math

#Enter the required value

Value_of_x1 = float(input("Enter the value of x1: "))
Value_of_x2 = float(input("Enter the value of x2: "))
Value_of_y1 = float(input("Enter the value of y1: "))
Value_of_y2 = float(input("Enter the value of y2: "))

#Grouped points for the formula

Point1 = (Value_of_x1, Value_of_y1)
Point2 = (Value_of_x2, Value_of_y2)

#The formula to run the code and get the two points

Distance = math.sqrt(math.pow(Value_of_x2 - Value_of_x1, 2) + math.pow(Value_of_y2 - Value_of_y1, 2))
print("The distance between the two points is:", Distance)

# guide questions
"""
# It made it easier and helped me learn. It also guided us to complete our program and be better.
"""
"""
# The distance code was easy to put on because it was automatic but aside from that we learned how to use it. It made us finish our program faster and it was a great help.
"""
"""
# We would go into a lot of process and would take us longer. We would have never been able to complete and finish the program.
"""
