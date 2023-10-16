def sieve_of_eratosthenes(n):
    # Create a boolean list to mark prime and non-prime numbers
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime
    
    p = 2
    while p**2 <= n:
        if is_prime[p]:
            for i in range(p**2, n + 1, p):
                is_prime[i] = False
        p += 1
    
    prime_numbers = [i for i in range(2, n + 1) if is_prime[i]]
    return prime_numbers

# Input the value of N
N = int(input("Enter the value of N: "))

prime_numbers = sieve_of_eratosthenes(N)
print(f"Prime numbers from 1 to {N}: {prime_numbers}")
