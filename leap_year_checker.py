def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def legendre_conjecture(n):
    primes = []
    for i in range(n + 1, 2 * n):
        if is_prime(i):
            primes.append(i)
    return primes

def main():
    try:
        n = int(input("Enter a positive integer (n): "))
        if n <= 0:
            print("Please enter a positive integer.")
            return

        result = legendre_conjecture(n)
        if result:
            print(f"Prime numbers between {n} and {2 * n - 1}: {result}")
        else:
            print(f"No prime numbers found between {n} and {2 * n - 1}. Legendre's Conjecture holds!")
    except ValueError:
        print("Invalid input. Please enter a positive integer.")

if __name__ == "__main__":
    main()
