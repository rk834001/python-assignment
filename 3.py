# Initialize an empty list to store the real numbers
real_numbers = []

# Input the number of real numbers
n = int(input("Enter the number of real numbers: "))

# Input the real numbers and add them to the list
for i in range(n):
    num = float(input(f"Enter real number {i + 1}: "))
    real_numbers.append(num)

# Initialize the product to 1
product = 1

# Calculate the product of the real numbers
for num in real_numbers:
    product *= num

# Display the product
print(f"The product of the real numbers is {product}")
