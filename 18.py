def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid  # Element found, return its index
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1  # Element not found

# Example sorted list
my_list = [2, 5, 7, 12, 34, 45, 56, 67, 78, 89]

# Element to search for
target_element = int(input("Enter the element to search for: "))

# Call the binary search function
result = binary_search(my_list, target_element)

if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found in the list")
