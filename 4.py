import math

# Input the radius of the circle
radius = float(input("Enter the radius of the circle: "))

# Calculate the circumference
circumference = 2 * math.pi * radius

# Calculate the area
area = math.pi * (radius ** 2)

# Display the results
print(f"The circumference of the circle is {circumference:.2f}")
print(f"The area of the circle is {area:.2f}")
