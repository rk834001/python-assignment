import math

# Input coefficients a, b, and c
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

# Calculate the discriminant
discriminant = b**2 - 4*a*c

# Check the discriminant for real roots
if discriminant > 0:
    root1 = (-b + math.sqrt(discriminant)) / (2*a)
    root2 = (-b - math.sqrt(discriminant)) / (2*a)
    print(f"Two real roots: {root1} and {root2}")
elif discriminant == 0:
    root = -b / (2*a)
    print(f"One real root: {root}")
else:
    real_part = -b / (2*a)
    imaginary_part = math.sqrt(abs(discriminant)) / (2*a)
    print(f"Complex roots: {real_part} + {imaginary_part}i and {real_part} - {imaginary_part}i")
