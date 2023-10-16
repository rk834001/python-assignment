# Input the list of numbers
numbers = [int(x) for x in input("Enter numbers separated by spaces: ").split()]

# Input the number to insert
number_to_insert = int(input("Enter the number to insert: "))

# Input the position to insert the number
position = int(input(f"Enter the position (0 to {len(numbers)}): "))

# Check if the position is valid
if position < 0 or position > len(numbers):
    print("Invalid position. The number was not inserted.")
else:
    # Insert the number at the specified position
    numbers.insert(position, number_to_insert)

    # Display the updated list
    print("Updated list:", numbers)
