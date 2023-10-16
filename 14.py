def print_numbers_from_n_to_0(n):
    if n >= 0:
        print(n)
        print_numbers_from_n_to_0(n - 1)

# Input a number 'n'
n = int(input("Enter a number: "))

# Call the recursive function
print_numbers_from_n_to_0(n)
