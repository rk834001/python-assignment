# Input the list of numbers
numbers = [int(x) for x in input("Enter numbers separated by spaces: ").split()]

# Initialize a variable to store the largest number
largest = numbers[0]

# Iterate through the list and find the largest number
for num in numbers:
    if num > largest:
        largest = num

# Display the largest number
print("The largest number in the list is:", largest)
