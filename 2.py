import math

# Input the lengths of the three sides of the triangle
a = float(input("Enter the length of side 'a': "))
b = float(input("Enter the length of side 'b': "))
c = float(input("Enter the length of side 'c': "))

# Calculate the semi-perimeter of the triangle
s = (a + b + c) / 2

# Calculate the area using Heron's formula
area = math.sqrt(s * (s - a) * (s - b) * (s - c))

# Display the area
print(f"The area of the triangle is {area}")
