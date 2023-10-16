# Input an integer
num = int(input("Enter an integer: "))

# Check if the number is less than 2
if num < 2:
    is_prime = False
else:
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

# Display the result
if is_prime:
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")
