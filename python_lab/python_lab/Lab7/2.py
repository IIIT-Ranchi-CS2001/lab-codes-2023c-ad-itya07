import random
import math
import matplotlib.pyplot as plt

# Step 1: Generate K random numbers within limit N
K = int(input("Enter the number of random numbers (K, minimum 10): "))
N = int(input("Enter the limit (N): "))
if K < 10:
    raise ValueError("K should be at least 10.")

numbers = random.sample(range(1, N + 1), K)
print("Generated Numbers:", numbers)

# Step 2: Define functions to return prime and composite numbers
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

primes = [n for n in numbers if is_prime(n)]
composites = [n for n in numbers if not is_prime(n)]

print("Prime Numbers:", primes)
print("Composite Numbers:", composites)

# Step 3: Determine the square of primes and square root of composites
prime_squares = [p**2 for p in primes]
composite_sqrts = [math.sqrt(c) for c in composites]

print("Squares of Primes:", prime_squares)
print("Square Roots of Composites:", composite_sqrts)

# Step 4: Plot the results as scatterplots
plt.figure(figsize=(10, 5))

# Subplot for primes vs squares
plt.subplot(1, 2, 1)
plt.scatter(primes, prime_squares, color="blue", label="Primes")
plt.title("Primes vs Squares")
plt.xlabel("Prime Numbers")
plt.ylabel("Squares")
plt.grid(True)

# Subplot for composites vs square roots
plt.subplot(1, 2, 2)
plt.scatter(composites, composite_sqrts, color="red", label="Composites")
plt.title("Composites vs Square Roots")
plt.xlabel("Composite Numbers")
plt.ylabel("Square Roots")
plt.grid(True)

plt.tight_layout()
plt.show()
