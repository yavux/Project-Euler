def gauss_sum_multiples(x, y):
    k = x // y
    return y * k * (k + 1) // 2

def prime_factors(n):
    factors = set() 
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors.add(d)
            n //= d 
        d += 1
    if n > 1: 
        factors.add(n)
        
    return list(factors)


def primes(n):
    numbers = []
    for i in range (2,n):
        is_prime = True
        for j in range(2,int(i**0.5)+1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            numbers.append(i)
    return numbers

