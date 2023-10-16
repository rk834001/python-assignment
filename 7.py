import math

# Input the number of values
n = int(input("Enter the number of values: "))

# Initialize a variable for the product of values
product = 1

# Input the values and calculate their product
for i in range(n):
    value = float(input(f"Enter value {i + 1}: "))
    product *= value

# Calculate the geometric mean
geometric_mean = math.pow(product, 1/n)

# Display the geometric mean
print(f"The geometric mean of the {n} values is {geometric_mean:.2f}")
