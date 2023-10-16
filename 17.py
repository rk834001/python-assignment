def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Return the index if found
    return -1  # Return -1 if not found

# Example list
my_list = [12, 45, 67, 89, 34, 2, 56, 78]

# Element to search for
target_element = int(input("Enter the element to search for: "))

# Call the linear search function
result = linear_search(my_list, target_element)

if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found in the list")
