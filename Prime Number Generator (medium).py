# Prime Number Generator using Sieve of Eratosthenes algorithm

def generate_primes(n):
    # Create a boolean array "prime[0..n]" and initialize all entries as true.
    prime = [True for _ in range(n + 1)]
    p = 2
    while p * p <= n:
        # If prime[p] is not changed, then it is a prime
        if prime[p]:
            # Updating all multiples of p to false
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1
    
    # Collect all prime numbers
    primes = []
    for p in range(2, n + 1):
        if prime[p]:
            primes.append(p)
    return primes

# Example usage
n = 50
print(f"Prime numbers up to {n}:", generate_primes(n))
