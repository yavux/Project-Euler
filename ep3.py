# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?
# A number can have at most one prime factor greater than its square root!
import time 
start = time.time()
def largest_prime_factor(n):
    d = 2
    while d * d <= n:
        if n % d == 0:
            n //= d
        else:
            d += 1
    return n


print(largest_prime_factor(600851475143))  

end = time.time()
print("Çalışma süresi: ", end - start, "saniye")    