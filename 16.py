# Input the number of values
n = int(input("Enter the number of values: "))

# Initialize an empty list to store the values
values = []

# Input the values and add them to the list
for i in range(n):
    value = float(input(f"Enter value {i + 1}: "))
    values.append(value)

# Calculate the sum of the values using the sum() function
total_sum = sum(values)

# Display the sum
print(f"The sum of the {n} values is {total_sum}")
