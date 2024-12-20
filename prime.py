def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

# Input from the user
num = int(input("Enter a number: "))

# Check and print whether the number is prime or not
if is_prime(num):
    print(num, "is a prime number.")
else:
    print(num, "is not a prime number.")
