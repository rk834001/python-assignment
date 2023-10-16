# Define the range
start = 100
end = 200

# Iterate through the range and check the sum of digits
for number in range(start, end + 1):
    # Calculate the sum of digits
    digit_sum = sum(int(digit) for digit in str(number))
    
    # Check if the sum of digits is even
    if digit_sum % 2 == 0:
        print(number)
