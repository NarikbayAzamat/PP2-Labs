def isPrime(num):
    divisors = 2
    if num < 2:
        return False
    for i in (range(2, num)):
        if num % i == 0:
            return False
    return True

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

primeNumbers = list(filter(lambda x: isPrime(x), numbers))

print(primeNumbers)