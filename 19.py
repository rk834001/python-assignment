# Input the array of numbers
numbers = [int(x) for x in input("Enter numbers separated by spaces: ").split()]

# Initialize an empty list to store odd numbers
odd_numbers = []

# Iterate through the numbers and find the odd ones
for num in numbers:
    if num % 2 != 0:
        odd_numbers.append(num)

# Display the odd numbers
print("Odd numbers in the array:", odd_numbers)
