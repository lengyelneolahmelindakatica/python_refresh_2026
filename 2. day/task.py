"""
Ask the user to enter the values of side 'a' and side 'b'.
Calculate the perimeter and area of the rectangle.
Print the results to the console.
"""

#ask the user input
a = int(input("Please enter the side 'a' of the rectangle: "))
b = int(input("Please enter the side 'b' of the rectangle: "))

perimeter = 2 * (a + b)
area = a*b

print("The perimeter of the rectangle is " + str(perimeter) + ", and the area is " + str(area) + ".")

#Version 2:
print(f"The perimeter of the rectangle is {perimeter}, and the area is {area}.")

#Version 3:
print("The perimete of the rectangle is", perimeter, ", and the area is", area, ".")

"""
Calculate your age!
Ask the user for give his/her birth year as an input.
Deduct your birth year from current year and print it on screen!
"""

birth_year = int(input("What year were you born?\n"))
current_year= int(input("What year is today?\n"))

age = current_year - birth_year

print(f"You are {age} years old.")

