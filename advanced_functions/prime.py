# Define is prime function
def is_prime(number: int) -> bool:
    # Easy way to check if a number is prime
    for i in range(2, number+1):
        # If the square of the index is greater than number
        # Then the number is a prime.
        # This line just help with time improvement.
        if i*i > number:
            return True
        # Just check if the index is not multiple of number
        if not number % i:
            return False
    # If the number <= 1 then is not a prime
    return False


def main():
    print(is_prime(101))

if __name__ == "__main__":
    main()