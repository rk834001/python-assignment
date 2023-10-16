# Input the list of elements
elements = [int(x) for x in input("Enter elements separated by spaces: ").split()]

# Input the index to delete
index = int(input(f"Enter the index to delete (0 to {len(elements) - 1}): "))

# Check if the index is valid
if index < 0 or index >= len(elements):
    print("Invalid index. The element was not deleted.")
else:
    # Delete the element at the specified index
    del elements[index]

    # Display the updated list
    print("Updated list:", elements)
