# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

import time 
start = time.time()
from utils import primes
def smallest_divisible(n):
    factors = primes(n)
    sum = 1
    for i in factors:
        exp = 1
        while i**exp < n:
            exp += 1    
        sum *= i**(exp-1)
    return sum

print(smallest_divisible(20))  
end = time.time()
print("Çalışma süresi: ", end - start, "saniye")    