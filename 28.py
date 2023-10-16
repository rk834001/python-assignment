# Input the number of terms in the Fibonacci series
N = int(input("Enter the number of terms: "))

# Initialize the first two terms
a, b = 0, 1

# Print the first N terms of the Fibonacci series
if N <= 0:
    print("Please enter a positive integer for the number of terms.")
elif N == 1:
    print(a)
else:
    print(a, end=" ")
    print(b, end=" ")
    for _ in range(2, N):
        a, b = b, a + b
        print(b, end=" ")
