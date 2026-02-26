#The sum of the primes below 10 is 17.
#Find the sum of all the primes below two million.

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def sum_of_primes_below(limit):
    total = 0
    for num in range(2, limit):
        if is_prime(num):
            total += num
    return total

print(sum_of_primes_below(2000000))